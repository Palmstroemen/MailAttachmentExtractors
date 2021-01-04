#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This script checks for new emails in a specified account, downloads
the emails and safes the attachments in a specified folder.
Then it responds to the senders of the mail with a confirmation mail.
Mails are accepted just from particular users. Others are rejected.
Users can be managed by simple commands in the subjectline of the mail.
Typical usage of this script is to forward mails to the specified account.

Author: Oliver Rafelsberger 2020
Version 0.1
"""
from datetime import datetime
import email

import imapclient
import pyzmail
from bs4 import BeautifulSoup

from Region import Region, Answer, Replystrings
from Results import generate_short_answer, load_answer_HTML_template
from permittedUsers import checkUser
from mail import Mail
# from userFolders import getFolder, setFolder

# Mailadressen: fotoextraktor@lass-es-geschehen.de, dokumentextraktor@lass-es-geschehen.de


imapclient._MAXLINE  = 10000000

myMailHostIn      = Region.MailHostIn
myMailHostInPort  = Region.MailHostInPort
myMailHostOut     = Region.MailHostOut
myMailHostOutPort = Region.MailHostOutPort
myMailAddress     = Region.MailAddress
myMailPasswd      = Region.MailPasswd
myMailSSL         = Region.MailSSL
myMailName        = Region.MailName
myMailCheckAll    = Region.MailCheckAll


class Mailaccount(object):
    """Responsible for downloading the emails."""

    def __init__(self):
        """Creating the downloader. """
        print('Trying to connect to IMAP client: ', myMailAddress)
        self.imap = imapclient.IMAPClient(myMailHostIn, ssl=myMailSSL)
        self.imap.login(myMailAddress, myMailPasswd)

    def get_emails(self, unseenOrAll = 'UNSEEN'):
        """Looks for new mails and saves them in memory as a list of
        dictionaries.
        :unseenOrAll: 'UNSEEN' or 'ALL' to fetch the respective mails.

        :returns: a list of parsed emails as dictionaries

        """
        try:
            self.imap.select_folder('INBOX', readonly=False)
            print('Opening INBOX and looking for %s mails.' % unseenOrAll)
            mails = self.imap.search([unseenOrAll])
            raw_messages = self.imap.fetch(mails, ['BODY[]'])
            messages = [pyzmail.PyzMessage.factory(raw_messages[n][b'BODY[]'])
                        for n in raw_messages]
            saveAttachments(messages)
#            self.imap.delete_messages(mails)

        finally:
            print('Logging out.')
            self.imap.expunge()
            self.imap.logout()

def saveAttachments(messages):
    """Saves information on the emails in a specified folder.
    :messages: a list of parsed emails
    """
    for m in messages:
        mail = {'sender': m.get_address('from')[1], 'name': m.get_address('from')[0], 'subject': m.get_subject()}
        mail['date'] = email.utils.parsedate_to_datetime(m.get('Date'))
        #mail['dispo'] = m.get_content_disposition() ist eine Bestätigung in der Art eines Eingeschriebenen Briefes
        mail['mType'] = m.get_content_maintype()
        mail['sType'] = m.get_content_subtype()
        mail['dType'] = m.get_default_type()

        #mail['header'] = m.get_decoded_header('name':'?')

        if m.text_part is not None:
            mail['text_content'] = m.text_part.get_payload().decode(
                m.text_part.charset)
        else:
            mail['text_content'] = "None"

        if m.html_part is not None:
            mail['html_content'] = m.html_part.get_payload().decode(
                m.html_part.charset)
        else:
            mail['html_content'] = "None"

        mail['attachments'] = []
        # Um Attachments auszulesen ....
        for mailpart in m.mailparts:
            print('    %sfilename=%r alt_filename=%r type=%s charset=%s desc=%s size=%d' % ( \
                '*' if mailpart.is_body else ' ', \
                mailpart.filename, \
                mailpart.sanitized_filename, \
                mailpart.type, \
                mailpart.charset, \
                mailpart.part.get('Content-Description'), \
                len(mailpart.get_payload())))
            if not mailpart.is_body:
                mail['attachments'].append([mailpart.filename, mailpart.sanitized_filename, mailpart.type])
            #if mailpart.type.startswith('text/'):
                # display first line of the text
                #payload, used_charset = pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
                #print('        >', payload.split('\\n')[0])
        mail['number_attachments'] = len(mail['attachments'])/2

        print()
    print('Number of processed attachments: ')


def mailprozessor():
    """Starts the script if run from the command line.
    """
    starttime = datetime.now()
    print()
    print('=== Documentextractor running ===')
    print()

    answer_html_raw = load_answer_HTML_template(Answer.template_html_fastanswer)

    mailaccount = Mailaccount()
    emails = mailaccount.get_emails(myMailCheckAll)


    i = 0
    for mail in emails:
        i += 1
        print()
        mailaddress = mail['sender']
        mailsubject = mail['subject'][4:].strip().replace('\n', '')

        if mailaddress.find('MAILER-DAEMON')<0 and mailsubject.lower().find('returned to sender')<0:

            mailreceived= mail['date']
            print("Processing mail ("+str(i)+")")
            print("   subject:", mailsubject)
            print("  received:", mail['date'])
            print(' main type:', mail['mType'])
            print('  sub type:', mail['sType'])
            print('deflt type:', mail['dType'])
            print('Attached  :', mail['number_attachments'])
            #print('header    :', mail['header'])

            # Check if sender is a permitted user
            if checkUser(session, mail):
                print('Du bekommst bald eine Antwort')
                ans = generate_short_answer(
                    answer_html_raw,
                    Replystrings.fastTitle_soon,
                    Replystrings.fastSubject_soon,
                    new_mail.mail_id,
                    Replystrings.fastReply_soon)

                # send answermail.
                send_answer(mail, ans)

            # write to database
            session.commit()

    session.close()
    engine.dispose()



    # Finally make a log entry
    with open(Answer.logs_folder + 'runDocumentExtractor.log', 'a') as log_file:
        duration = datetime.now()-starttime
        message = (str(starttime.strftime("%Y-%m-%d  %H:%M"))+
                            ' answered '+str(i)+' mails which took: '+
                            str(duration.seconds)+' seconds.\n')
        log_file.write(message)
        print(message)


def prepare_mail_for_analysis(mail, getsanswer):
    """Saves the emails to the database or in a new folder.
    :param mail: the recent mail to safe to the DB
    :param getsanswer: the type of answer the user gets for this mail
    """

    if (mail):
        print('preparing new mail for database (remove Names).')
        new_mail = Mail()
        names = mail['name'].split(' ')
        for name in names:
            name = name.strip(' ')
            if len(name) < 3:
                names.remove(name)
            else:
                mail['text_content'] = mail['text_content'].replace(name, 'NAME')
                mail['subject'] = mail['subject'].replace(name, 'NAME')
                if name not in ['html', 'body', 'head', 'div', 'span']:
                    mail['html_content'] = mail['html_content'].replace(name, 'NAME')

        new_mail.sender = encrypt(mail['sender'])
        new_mail.subject = encrypt(str(mail['subject'])[4:].strip())

        new_mail.received = mail['date']
        new_mail.text = encrypt(mail['text_content'])
        new_mail.html = mail['html_content']
        new_mail.attachments = mail['number_attachments']
        new_mail.getsanswer = getsanswer
        new_mail.category = 'new'
        new_mail.count = 0

        print('Saving new mail.')
        session.add(new_mail)
        return new_mail

def send_answer(mail, answer):
    """
    Sends a first response to the customer before he receives the result.
    :param mail: The mail he has sent
    :param answer: The answer-class
    :return:
    """

    recipient = [mail['sender']]

    prefered_encoding = 'iso-8859-1'
    text_encoding = 'iso-8859-1'
    html_encoding = 'iso-8859-1'

    payload, mail_from, rcpt_to, msg_id = pyzmail.compose_mail( \
        myMailAddress, \
        recipient, \
        answer.subject, \
        prefered_encoding, \
        (answer.text, text_encoding), \
        (answer.html.encode(html_encoding), html_encoding), \
        attachments=[])

    print()
    print('send_answer')
    #print(payload)

    ret = pyzmail.send_mail(payload, myMailAddress, recipient, myMailHostOut, \
                            smtp_port=myMailHostOutPort, smtp_mode='tls', \
                            smtp_login=myMailAddress, smtp_password=myMailPasswd)
    #ret = 'derzeit kein Mailversand'

    if isinstance(ret, dict):
        if ret:
            print('failed recipient:', ', '.join(ret.keys()))
        else:
            print('success')
    else:
        print('error:', ret)


def main():
   mailprozessor()

if __name__ == "__main__":
    main()
