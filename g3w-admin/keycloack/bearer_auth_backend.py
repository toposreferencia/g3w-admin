
from .settings import *
import requests
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class KeycloackBearerAB:

    def authenticate(self, request, **kwargs):

        auth_header = ''

        try:
            auth_header = kwargs['authorization']
        except Exception as e:
            try:
                auth_header = request.headers("Authorization")
            except Exception as ex:
                pass

        if auth_header.startswith("Bearer"):

            # TODO Cache tokens!
            try:
                token = auth_header[7:]
                userinfo = requests.get(
                    OIDC_OP_USER_ENDPOINT,
                    headers={"Authorization": "Bearer {}".format(token)},
                ).json()
                user_id = userinfo['sub']
                return User.objects.get(username=user_id)

            except Exception as e:

                logger.debug(e)

        return None
