# From http://lists.jboss.org/pipermail/keycloak-user/2016-April/005869.html

KC_REALM=myrealm
KC_CLIENT=myclient
KC_CLIENT_SECRET=YINgezDL3PRfJqss2nDpEEkwZe1hPdj6
KC_SERVER=172.20.0.1:8080

# Request Tokens for credentials
KC_RESPONSE=$( \
   curl -k -v -X POST \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d 'grant_type=client_credentials' \
        -d "client_id=$KC_CLIENT" \
        -d "client_secret=$KC_CLIENT_SECRET" \
        "http://$KC_SERVER/realms/$KC_REALM/protocol/openid-connect/token" | jq .
)

KC_ACCESS_TOKEN=$(echo $KC_RESPONSE| jq -r .access_token)
KC_ID_TOKEN=$(echo $KC_RESPONSE| jq -r .id_token)
KC_REFRESH_TOKEN=$(echo $KC_RESPONSE| jq -r .refresh_token)
#
## Show all keycloak env variables
set | grep KC_*
#
## Introspect Keycloak Request Token
curl -k -v \
     -X POST \
     -u "$KC_CLIENT:$KC_CLIENT_SECRET" \
     -d "token=$KC_ACCESS_TOKEN" \
     "http://$KC_SERVER/realms/$KC_REALM/protocol/openid-connect/token/introspect"