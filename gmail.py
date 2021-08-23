import smtplib
import time
import imaplib
import email
import traceback
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
from bs4 import BeautifulSoup


ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "pacteraedge111" + ORG_EMAIL
FROM_PWD = "9912277968"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993




def convertChar(char):
    if char >= 'A' and char <= 'Z':
        return chr(ord(char) + 32)
def toLowerCase(string):
    newString = []
    for char in string:
        newString.append(convertChar(char))
    return ''.join(newString)




def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    for payload in msg.get_payload():
                        print(payload.get_payload())

                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = msg['body']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    #print('body : ' + email_body + '\n')

    except Exception as e:
        traceback.print_exc()
        print(str(e))




# def read_email_from_gmail():
#     mail = imaplib.IMAP4_SSL(SMTP_SERVER)
#     mail.login(FROM_EMAIL, FROM_PWD)
#     mail.select('inbox')
#
#     data = mail.search(None, 'ALL')
#     print(data)
#     mail_ids = data[1]
#     print(mail_ids)
#     id_list = mail_ids[0].split()
#     print(id_list)
#     first_email_id = int(id_list[0])
#     print(first_email_id)
#     latest_email_id = int(id_list[-1])
#     print("latest_email_id{}".format(latest_email_id))
#     data = mail.fetch(str(2), '(RFC822)')
#     print(data)
#     arr = data[0]
#     print("arr{}".format(arr))
#
#     b = email.message_from_string(arr)
#     if b.is_multipart():
#         for payload in b.get_payload():
#             # if payload.is_multipart(): ...
#
#             print( payload.get_payload())
    #
    # if isinstance(arr, tuple):
    #     msg = email.message_from_string(str(arr[0], 'utf-8'))
    #     print(msg)
    #     email_subject = msg['subject']
    #     print('email_subject'.format(email_subject))
    #
    #




#
    # for i in range(latest_email_id, first_email_id, -1):
    #     data = mail.fetch(str(i), '(RFC822)')
    #     for response_part in data:
    #         arr = response_part[0]
    #         if isinstance(arr, tuple):
    #             msg = email.message_from_string(str(arr[1], 'utf-8'))
    #             print('msg')
    #             print(msg)
    #             email_subject = msg['subject']
    #             email_from = msg['from']
    #             emil_body = msg['body']
    #             print(emil_body)
    #             print('From : ' + email_from + '\n')
    #             print('Subject : ' + email_subject + '\n')





read_email_from_gmail()







