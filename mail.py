__author__ = 'oliver'
# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime, Text, Table
from base import Base
from datetime import datetime




class Mail(Base):
    __tablename__ = 'mails'
    mail_id = Column(Integer, primary_key=True)
    sender = Column(String(100))
    subject = Column(String)
    received = Column(DateTime, nullable=True)
    getsanswer = Column(Integer)
    text = Column(Text)
    html = Column(Text)
    attachments = Column(Integer)
    category = Column(String)
    count = Column(Integer)
    danger = Column(Integer)

    def __init__(self):
        self.sender = ''
        self.subject = ''
        self.received = 0
        self.getsanswer = 0
        self.text = ''
        self.html = ''
        self.attachments = 0
        self.count = 0
        self.category = ''
        self.danger = 0
