"""
Procore SDK Exceptions
"""


class ProcoreError(Exception):
    """The base exception class for Procore.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(ProcoreError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class NotFoundClientError(ProcoreError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(ProcoreError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(ProcoreError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(ProcoreError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(ProcoreError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(ProcoreError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(ProcoreError):
    """Not found the item from URL, 404 error."""
    pass
    

class InternalServerError(ProcoreError):
    """The rest Procore errors, 500 error."""
    pass
