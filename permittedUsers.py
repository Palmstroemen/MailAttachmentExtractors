__author__ = 'oliver'
# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime
from base import Base
from datetime import datetime


class PermittedUser(Base):
    __tablename__ = 'permittedUsers'

    mailaddress = Column(String, primary_key=True, unique=True)

    def __init__(self, mailaddress):
        self.mailaddress = mailaddress


def checkUser(session, mail):
    """Checks if the sender of the mail is an user.
    :mail: the current email
    """
    sender: object = mail['sender']
    subject: object = mail['subject']
    mailreceived = mail['date']
    getsanswer = 0

    print('   sender :', sender)
    if PermittedUser(sender):
        print('   is accepted.')
        return 1
    else:
        print('   is NO user yet.')
        return 0

def addUser(session, mailAddress):
    session.add(mailAddress)
    session.flush()

