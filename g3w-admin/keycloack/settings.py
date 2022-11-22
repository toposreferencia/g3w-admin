# coding=utf-8
""""
Mozilla django oidc Keycloack openid connect settings

.. note:: This program is free software; you can redistribute it and/or modify
          it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'elpaso@itopen.it'
__date__ = '2021-10-19'
__copyright__ = 'Copyright 2021, Gis3W'


#########################################################
#

import urllib3
import os

KC_HOST = 'http://localhost:8080/'

# Keycloack
OIDC_RP_CLIENT_ID = 'myclient'
OIDC_RP_CLIENT_SECRET = 'YINgezDL3PRfJqss2nDpEEkwZe1hPdj6'
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/certs"
OIDC_RP_SIGN_ALGO = "RS256"

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following insecure options have been used for development
# DO NOT USE IN PRODUCTION
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

OIDC_VERIFY_SSL = False
OIDC_VERIFY_JWT = False
OIDC_VERIFY_KID = False
OIDC_ALLOW_UNSECURED_JWT = True
