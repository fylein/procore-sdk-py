from .api_base import ApiBase


class Companies(ApiBase):
    """Class for Companies APIs."""

    GET_COMPANIES = '/companies'

    def get(self):
        """
        Get all companies
        :return: returns all companies
        """
        return self._get_request({}, Companies.GET_COMPANIES)
