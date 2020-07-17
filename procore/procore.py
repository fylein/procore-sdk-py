from .exceptions import *
from .apis import *
import requests
import json


class Procore:
    """The main class which creates a connection with Procore APIs using OAuth2 authentication (refresh token grant type).

    Parameters:
        client_id (str): Client ID for Procore API.
        client_secret (str): Client secret for Procore API.
        refresh_token (str): Refresh token for Procore API.
    """

    TOKEN_URL = '{}/oauth/token'

    def __init__(self, login_url, base_url, client_id, client_secret, refresh_token):
        """
        Constructor to initialize the SDK
        :param base_url: Procore Base URL
        :param client_id:
        :param client_secret:
        :param refresh_token:
        """
        self.__login_url = login_url
        self.__base_url = base_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token
        self.access_token = None

        # create an object for each api
        self.companies = Companies()
        self.projects = Projects()

        # get the access token
        self.update_access_token()
        self.set_server_url()

    def update_access_token(self):
        """Update the access token and change it in all API objects."""

        access_token = self.__get_access_token()

        self.companies.change_access_token(access_token)
        self.projects.change_access_token(access_token)

    def set_server_url(self):
        """Set the Base URL in all API objects."""

        base_url = self.__base_url

        self.companies.set_server_url(base_url)
        self.projects.set_server_url(base_url)

    def __get_access_token(self):
        """Get the access token using a HTTP post.

        Returns:
            A new access token.
        """

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }

        token_url = Procore.TOKEN_URL.format(self.__login_url)
        response = requests.post(token_url, data=api_data)

        if response.status_code == 200:
            access_token = json.loads(response.text)['access_token']
            self.access_token = access_token
            return access_token

        elif response.status_code == 401:
            raise UnauthorizedClientError('Wrong client secret or/and refresh token', response.text)

        elif response.status_code == 404:
            raise NotFoundClientError('Client ID doesn\'t exist', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise ProcoreError('Error: {0}'.format(response.status_code), response.text)
