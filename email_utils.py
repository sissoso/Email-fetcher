from __future__ import print_function

import apiclient
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools


def connectGmail():
    # Setup the Gmail API
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('./json files/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = apiclient.discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    return service


def getLabels(service):
    gmail_user = service.users().labels().list(userId='me').execute()
    labels = gmail_user.get('labels', [])
    if not labels:
        print('No labels found.')
        return None
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
        return labels


def ListMessagesWithLabels(service, user_id='me', label_ids=[], max_results=5):
    try:
        response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids, maxResults=max_results).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
        return messages
    except errors.HttpError as e:
        print('An error occurred: ' + str(e))


def getMessages(service, msg_id, user_id='me'):
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        print('Message : '+message['snippet'])

        return message
    except errors.HttpError as e:
        print('An error occurred: %s' + str(e))




