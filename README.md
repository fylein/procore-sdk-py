# Procore Python SDK

Python SDK for accessing Procore APIs.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install procore

## Usage

To use this SDK you'll need these Procore credentials used for OAuth2 authentication: **client ID**, **client secret** and **refresh token**. Visit https://developers.procore.com to setup Procore developer account

This SDK is very easy to use.
1. First you'll need to create a connection using the main class Procore.
```python
from procore import Procore, WrongParamsError

connection = Procore(
    login_url='LOGIN URL',
    base_url='BASE URL',
    client_id='PROCORE CLIENT ID',
    client_secret='PROCORE CLIENT SECRET',
    refresh_token='REFRESH TOKEN'
)

companies = connection.companies.get() # Get All Companies
company_id = companies[0]['id']

projects = connection.projects.get(company_id=company_id) # Get All Projects
```


See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details