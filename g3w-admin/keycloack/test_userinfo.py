import requests
import sys
import json
from getpass import getpass
from urllib.parse import urlparse

KC_HOST = 'http://172.20.0.1:8080/'

# Keycloack
OIDC_RP_CLIENT_ID = 'myclient'
OIDC_RP_CLIENT_SECRET = 'YINgezDL3PRfJqss2nDpEEkwZe1hPdj6'
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{KC_HOST}realms/myrealm/protocol/openid-connect/certs"
OIDC_RP_SIGN_ALGO = "RS256"


kc_server = KC_HOST
client_id = OIDC_RP_CLIENT_ID
client_secret = OIDC_RP_CLIENT_SECRET

keycloak_endpoint = OIDC_OP_TOKEN_ENDPOINT
userinfo_endpoint = OIDC_OP_USER_ENDPOINT


username = 'myuser'
password = 'admin'

token_resp = requests.post(
    keycloak_endpoint,
    data={
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": 'openid',
        "password": password,
        "username": username
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"},
)
print(token_resp.json())
token = token_resp.json()['access_token']

print("##########################")
print("###### Access Token ######")
print("##########################")
print(token)


userinfo = requests.get(
    userinfo_endpoint,
    headers={"Authorization": "Bearer {}".format(token)},
)

print("##########################")
print("######## Userinfo ########")
print("##########################")
print(userinfo.json())
