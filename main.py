import smtplib
import time
import email
import imaplib
import pandas as pd


def parse_email_msg( USER_ID , PWD , SMTP_SERVER='imap.gmail.com' , SMTP_PORT=993 ,last_n=0):
    """
    a function to parse email contents
    USER_ID - (str) user email id
    PWD - (str) your email Id password
    SMTP_SERVER - (str)your smtp server - default : 'imap.gmail.com'
    SMTP_PORT - (int) smtp port - default : 993
    last_n - (int) last n number of emails to be taken into consideration - default : 0(checks all the mails)


    returns a dataframe containing the email contents
    """
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(USER_ID , PWD)

    mail.select('inbox')
    Type , data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    first_id = int(id_list[0])
    last_id = int(id_list[-1])

    df = pd.DataFrame(columns=['MIME-Version', 'x-no-auto-attachment', 'Received', 'Date', 'Message-ID', 'Subject', 'From', 'To', 'Content-Type'])
    if last_n != 0:
        id_list = id_list[len(id_list) - last_n :]
    for i in id_list:
        Type , data = mail.fetch(i , "(RFC822)")
        for r in data:
            if isinstance(r , tuple):
                msg = email.message_from_bytes(r[1])
                df = df.append({
                    key:msg[key] for key in msg.keys()
                }, ignore_index=True)
    
    return df