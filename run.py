from email_utils import getLabels
from email_utils import  connectGmail
from email_utils import getMessages
from email_utils import ListMessagesWithLabels
# connecting to Gmail account
service = connectGmail()
# function that print and return labels ,if not labels return None
labels = getLabels(service=service)

# function return list of 5 last messages . function can return more by changing max_results parameter
messages = ListMessagesWithLabels(service=service)

# below example of calling last 10 mails from SPAM label
# label=[]
# label.append('SPAM')
# messages = ListMessagesWithLabels(service=service, max_results=5, label_ids=label)
# print(messages)
for message in messages:
    getMessages(service=service, msg_id=message['id'])