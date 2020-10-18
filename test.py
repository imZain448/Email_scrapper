import pandas as pd
from main import parse_email_msg

HOST_NAME = "@your_host.name" # example @gmail.com
USER_ID = "username"+ HOST_NAME # example xyz123
PWD = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

data = parse_email_msg(USER_ID , PWD , SMTP_SERVER , SMTP_PORT)
#print(data.columns)
df = data.loc[data['Subject'].str.contains('Thank you for applying')]
df = df[['Date' , 'From' , 'Subject' , 'To']]
df.to_csv('scrapped_emails.csv')