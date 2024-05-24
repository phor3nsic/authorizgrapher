import requests
import json
import argparse

credentials_file = "creds.json"

def parse_creds():
    creds = {}
    with open(credentials_file) as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line.strip())
            creds.update(data)
    return creds

def parse_headers(header_string, token):
    header_string = header_string.replace("%AUTH%",token)
    headers = {}
    try:
        headers = json.loads(header_string)
    except json.JSONDecodeError:
        for item in header_string.split(','):
            key, value = item.split(':', 1)
            headers[key.strip()] = value.strip()
    return headers

def generate_graphql_operations(introspection):
    with open(introspection, 'r') as file:
        data = json.load(file)

    operations = []

    for type in data['data']['__schema']['types']:
        if type['kind'] == 'OBJECT' and type['name'] == 'Query':
            for field in type['fields']:

                field_name = field['name']
                field_args = ', '.join([f"{arg['name']}:{arg['type']['name']}" for arg in field['args']])
                field_args = f"({field_args})" if field_args else ""
                query = f"query x{{{field_name}{field_args}{{{field_name}}}}}"
                operations.append({field_name: {"query": query}})
        elif type['kind'] == 'OBJECT' and type['name'] == 'Mutation':
            for field in type['fields']:

                field_name = field['name']
                field_args = ', '.join([f"{arg['name']}:{arg['type']['name']}" for arg in field['args']])
                field_args = f"({field_args})" if field_args else ""
                mutation = f"mutation x {{{field_name}{field_args}{{{field_name}}}}}"
                operations.append({field_name: {"query": mutation}})

    return operations

def req(url, action, token):
    s = requests.session()
    
    data = {
        "query":action
    }

    req_headers = parse_headers(headers, token)
    res = s.post(url, json=data, headers=req_headers)
    return res


def main():
    operations = generate_graphql_operations(introspection_file)
    for user in credentials:
    
        # Test queries
        for operation in operations:
            data = json.dumps(operation)
            data_dict = json.loads(data)
            for key, value in data_dict.items():
                res = req(url, value['query'], credentials[user]['token'])
                if res.status_code != 401:
                    print(f"[status: Work] [query: {key}] User: {user}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-u','--url', type=str, required=True, help="Url to make tests. Ex: https://test.com/graphql")
    parser.add_argument('-H', '--headers', type=str, help='Headers for the request in JSON format or "Key: Value, Key2: Value2"')
    parser.add_argument('-i','--introspection_file', required=True, help="Introspection file to get query/mutation")
    args = parser.parse_args()

    credentials = parse_creds()

    if args.headers:
        headers = args.headers
    else:
        headers = ""
    
    introspection_file = args.introspection_file
    url = args.url

    main()

    
