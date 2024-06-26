<h1 align="center">
  AuthorizGrapher
  <br>
</h1>

<h4 align="center">Check which users can interact with a query or mutation from an introspection.</h4>

<h6 align="center">Coded with 💙 by phor3nsic</h6>

<p align="center">

<br>
  <!--Tweet button-->
  <a href="https://twitter.com/intent/tweet?text=AuthorizGrapher%20-%20Check%20which%20users%20can%20interact%20with%20query%20or%20mutation%20from%20an%20introspection.%20https%3A%2F%2Fgithub.com%2Fphor3nsic%2Fauthorizgrapher%20%23bash%20%23graphql%20%23bugbounty%20%23bugbountytips%20%23infosec" target="_blank">Share on Twitter!</a>
</p>

<p align="center">
  <a href="#install-">Install</a> •
  <a href="#examples-">Examples</a> •
  <a href="#contributing-">Contributing</a> •
  <a href="#license-">License</a>
</p>

## Install 📡

### Installation

#### Safe Mode
```console
git clone https://github.com/phor3nsic/authorizgrapher.git
cd authorizgrapher
python3 -m venv venv
source ./venv/bin/activate
pip install requests
```

#### Normal Mode
```console
git clone https://github.com/phor3nsic/authorizgrapher.git
cd authorizgrapher
pip install requests
```

## Examples 💡

### Help
```bash
➜  python3 authorizgrapher.py -h
usage: authorizgrapher.py [-h] -u URL [-H HEADERS] -i INTROSPECTION_FILE

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to make tests. Ex: https://test.com/graphql
  -H HEADERS, --headers HEADERS
                        Headers for the request in JSON format or "Key: Value, Key2: Value2"
  -i INTROSPECTION_FILE, --introspection_file INTROSPECTION_FILE
                        Introspection file to get query/mutation
```

#### Create the Credentials File

You need to create a `creds.json` file like this:

```json
{"Admin":{"user":"admin@example.com","token":"eyJhbGciOiJ..."}}
{"Editor":{"user":"editor@example.com","token":"eyJhbGciOiJ..."}}
{"Normal":{"user":"normal@example.com","token":"eyJhbGciOiJ..."}}
```

#### Usage

With one introspection file and `creds.json`, make the requests like this:

```bash
python3 authorizgrapher.py --headers "Authorization: Bearer %AUTH%, Content-Type: application/json" -u https://example.com/graphql -i introspection.json 
```

> Note: You need to send the `%AUTH%` flag in the header or cookie for the script to use the authentication token from `creds.json`.

You get results like:

```bash
[status: Work] [query: getUsers] Admin
[status: Work] [query: getLogins] Admin
[status: Work] [query: testString] Admin
[status: Work] [query: getFailedTransactions] Admin
[status: Work] [query: forgotPassword] Admin
[status: Work] [query: testString] Editor
[status: Work] [query: forgotPassword] Editor
[status: Work] [query: getLogins] Normal
[status: Work] [query: testString] Normal
[status: Work] [query: forgotPassword] Normal
```

## Contributing 🛠

Just open an [issue](https://github.com/phor3nsic/reflectparams/issues) or a [pull request](https://github.com/phor3nsic/reflectparams/pulls).

## License 📝

This repository is under the [MIT License](https://github.com/phor3nsic/reflectparams/blob/master/LICENSE).  
Contact me at [ph0r3nsic@wearehackerone.com](mailto:ph0r3nsic@wearehackerone.com).
