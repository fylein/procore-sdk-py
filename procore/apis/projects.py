from .api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""

    GET_PROJECTS = '/projects'

    def get(self, company_id: str):
        """
        Get Projects from Procore
        :param company_id: The unique company id
        :return: projects
        """
        return self._get_request({
            'company_id': company_id
        }, Projects.GET_PROJECTS)
