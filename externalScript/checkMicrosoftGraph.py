#!/usr/bin/env python3
import requests, sys

try:
    requestType = sys.argv[1]
    tenantID    = sys.argv[2]
    appID       = sys.argv[3]
    secret      = sys.argv[4]
except:
    print("Missing arg - Requested : requestType - tenantID - appID - secret")
    exit()

requestURI = ""
if requestType == 'licences':
    requestURI = 'https://graph.microsoft.com/v1.0/subscribedskus'
elif requestType == 'organization':
    requestURI = 'https://graph.microsoft.com/v1.0/organization'
elif requestType == 'serviceHealth':
    requestURI = 'https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews'
else:
    print("Wrong requestType")
    print("Allowed values : licences / organization / serviceHealth")
    exit()

URL = "https://login.microsoftonline.com/{}/oauth2/v2.0/token".format(tenantID)
headers = { "Content-Type" : "application/x-www-form-urlencoded"}

body = {
    "scope"  : "https://graph.microsoft.com/.default",
    "grant_type" : "client_credentials", 
    "client_id" : appID,
    "client_secret" : secret
}
try:
    token_request = (requests.post(URL, headers = headers, data = body))

    if(token_request.status_code == 200):
        token = (token_request.json())["access_token"]
        url = requestURI
        headers = {'Authorization': 'Bearer ' + token}
        response = requests.get(url, headers=headers)
        if(response.status_code == 200):
            print(response.text)
        else:
            print("Erreur {} - {}".format(response.status_code,(response.json())["error"]["message"]))
    else:
        print("Echec de récupération du token : {} - {}".format(token_request.status_code,(token_request.json())["error_description"]))
except:
    print("Oups, un évènement imprévu s'est produit")