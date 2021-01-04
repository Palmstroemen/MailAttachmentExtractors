__author__ = 'oliver'
"""
To generate and inject answers into the original message
"""

import Region, os
from Region import Answer, Replystrings
from bs4 import BeautifulSoup


class Results():
    att_mail= ""
    att_name= ""
    opener  = ""
    sender  = []
    subject = []
    text    = []
    track   = []
    mail    = []
    link    = []
    img     = []
    scipt   = []
    other_domains = []
    attach  = []
    bank    = False
    closer  = ""
    score_sender = 0
    score_subject = 0
    score_text = 0
    count_wired_mails = 0
    score_this_mail = 0
    score_all_mails = 0
    count_wired_links = 0
    count_tracked_links = 0
    score_this_link = 0
    score_this_link_tracking = 0
    score_all_links = 0
    count_all_domains = 0
    count_wired_img = 0
    score_this_img = 0
    score_all_imgs = 0
    count_wired_scripts = 0
    score_this_script = 0
    score_all_scripts = 0
    count_wired_attachments = 0
    score_this_attachment = 0
    score_all_attachments = 0
    score   = 0
    disclaimer = ""
    answer_html = 'No'
    answer_text = 'No'

    def __init__(self, art):
        self.att_mail = ""
        self.att_name = ""
        self.opener = Replystrings.opener1+art+Replystrings.opener2
        self.sender = [Replystrings.sender_title]
        self.subject= [Replystrings.subject_title]
        self.text   = [Replystrings.text_title]
        self.closer = Replystrings.closer1+art+Replystrings.closer2
        self.score_sender = 0
        self.score_all_mails = 0
        self.score_all_links = 0
        self.score_all_imgs = 0
        self.score_all_scripts = 0
        self.score_all_attachments = 0
        self.count_all_domains = 0
        self.count_wired_mails = 0
        self.count_wired_links = 0
        self.count_tracked_links = 0
        self.count_wired_imgs = 0
        self.count_wired_scripts = 0
        self.count_wired_attachments = 0
        self.score  = 0
        self.disclaimer = Replystrings.disclaimer
        self.bank = False
        self.track = []
        self.other_domains = []
        self.attach = []

class ShortAnswer():
    html = ''
    title   = ''
    subject = ''
    id   = ''
    text = ''

    def __init__(self):
        self.html      = ''
        self.title     = ''
        self.subject   = ''
        self.id        = ''
        self.text      = ''

def load_answer_HTML_template(path):
    """
    Loads the template for the full HTML-Answer
    :param path:
    :return:
    """
    path = Answer.templates_folder + 'de/' + path + '/index.html'
    with open(path, 'r') as file:
        return file.read()

def insert_warning_in_html(html, insertpoint, messagelist, severity, size = "40", show_always = False):
    """

    :param insertpoint:
    :param messagelist:
    :param severity:
    :return:
    """
    icon_file = 'https://clixecure.com/media/clixicons/Ganove.png'
    if severity > Answer.warning_score_high:
        icon_color = "#FF0000"
        back_color = "#FFDFDF"
    elif severity > Answer.warning_score_mid:
        icon_color = "#FFFF00"
        back_color = "#FFFFDF"
    elif severity > Answer.warning_score_low:
        icon_color = "#00FF00"
        back_color = "#DFFFDF"
    else:
        if show_always == False:
            return
        else:
            icon_file  = 'https://clixecure.com/media/clixicons/check_OK.png'
            icon_color = "#F3F3F3"
            back_color = "#F3F3F3"

    new_message = html.new_tag('div')
    new_message.append(html.new_tag('table'))
    new_message.table['style'] = "font-family: -webkit-system-font, Helvetica Neue"
    new_message.table['bgcolor'] = back_color
    new_message.table['border'] = "0"
    new_message.table['cellpadding'] = "0"
    new_message.table['cellspacing'] = "0"
    new_message.table.append(html.new_tag('tr'))
    new_message.tr.append(html.new_tag('td'))
    new_message.td['style'] = "vertical-align: top"
    new_message.td.append(html.new_tag('table'))

    iconfield = html.new_tag('td')
    iconfield['width'] = size
    iconfield['bgcolor'] = icon_color
    #iconfield['style'] = "bgcolor:rgba(100, 100, 0, 1.0)"
    iconfield['style'] = "vertical-align: top"
    iconfield['border'] = "0"
    new_message.td.table.append(iconfield)

    icon = html.new_tag('img')
    icon['src'] = icon_file
    icon['height'] = size
    icon['width'] = size
    iconfield.append(icon)
    # right area
    newcolumn = html.new_tag('td')
    newcolumn['width'] = "1000"
    new_message.tr.append(newcolumn)

    newlist = html.new_tag('table')
    newlist['cellpadding'] = "0"
    newlist['cellspacing'] = "0"
    newlist['style'] = "margin-top: 1px; margin-right: 7px; margin-bottom: 0px; margin-left: 7px "

    newcolumn.append(newlist)

    i = 0
    for m in messagelist:
        newlist.append(html.new_tag('tr'))
        textfeld = html.new_tag('td')
        if i == 0:
            newlist.append(html.new_tag('b'))
            textfeld['style'] = "font-size: 22pt"
        textfeld.string = str(m)
        newlist.append(textfeld)
        i += 1


    insertpoint.insert_after(new_message)

    #print(messagelist)
    #print(new_message.prettify())



def insert_reply_in_html(html, insertpoint, messagelist, severity, size = "40", show_always = False):
    """

    :param insertpoint:
    :param messagelist:
    :param severity:
    :return:
    """
    if severity > Answer.warning_score_high:
        icon_color = "#FF0000"
        back_color = "#FFDFDF"
    elif severity > Answer.warning_score_mid:
        icon_color = "#FFFF00"
        back_color = "#FFFFDF"
    elif severity > Answer.warning_score_low:
        icon_color = "#00FF00"
        back_color = "#DFFFDF"
    elif severity < 0:  # for Tracking Message at the end of Mail
        icon_color = "#0000FF"
        back_color = "#DFDFFF"
    else:
        if show_always == False:
            return
        else:
            icon_color = "#F3F3F3"
            back_color = "#F3F3F3"

    new_message = html.new_tag('div')
    new_message['class'] = "cliX"
    new_message.append(html.new_tag('table'))
    #new_message.table['style'] = "font-family: -webkit-system-font, Andale Mono"
    new_message.table['style'] = "font-family: -webkit-system-font, PT Mono"
    new_message.table['bgcolor'] = back_color
    new_message.table['border'] = "0"
    new_message.table['cellpadding'] = "0"
    new_message.table['cellspacing'] = "0"
    new_message.table.append(html.new_tag('tr'))
    new_message.tr.append(html.new_tag('td'))
    new_message.td['style'] = "vertical-align: top"
    new_message.td.append(html.new_tag('table'))

    iconfield = html.new_tag('td')
    iconfield['width'] = size
    iconfield['bgcolor'] = icon_color
    #iconfield['style'] = "bgcolor:rgba(100, 100, 0, 1.0)"
    iconfield['style'] = "vertical-align: top"
    iconfield['border'] = "0"
    new_message.td.table.append(iconfield)

    icon = html.new_tag('img')
    icon['src'] = 'https://clixecure.com/media/clixicons/Ganove.png'
    icon['height'] = size
    icon['width'] = size
    iconfield.append(icon)
    # right area
    newcolumn = html.new_tag('td')
    #newcolumn['width'] = "1000"
    new_message.tr.append(newcolumn)

    newlist = html.new_tag('table')
    newlist['cellpadding'] = "0"
    newlist['cellspacing'] = "0"
    newlist['style'] = "margin-top: 3px; margin-right: 7px; margin-bottom: 3px; margin-left: 7px "

    newcolumn.append(newlist)

    i = 0
    for m in messagelist:
        textfeld = html.new_tag('tr')
        textfeld.append(html.new_tag('td'))
        textfeld.td.string = str(m)
        #textfeld['margin-top'] = "0"
        #textfeld['margin-bottom'] = "0"
        if i == 0:
            textfeld['style'] = "font-weight: bold"
            newlist.append(textfeld)
        else:
            newlist.append(textfeld)
        i += 1

    new_message.append(html.new_tag('br'))

    insertpoint.insert_after(new_message)

    #print(messagelist)
    #print(new_message.prettify())


def insert_tracking_in_html(html, insertpoint, type, message):
    """

    :param insertpoint:
    :param messagelist:
    :param severity:
    :return:
    """

    if type == 'lnk':
        frame_color = "#00AAFF"
    elif type == 'img':
        frame_color = "#0000FF"
    else:
        frame_color = "#A0A0A0"

    insertpoint.wrap(html.new_tag('table'))
    new_table = insertpoint.parent
    new_table['style'] = "border-collapse: collapse; padding = 2"
    insertpoint.wrap(html.new_tag('tr'))
    insertpoint.wrap(html.new_tag('td'))
    insertpoint.parent['style'] = "border: 3px solid blue"
    new_text = html.new_tag('td')
    new_table.tr.append(new_text)
    new_text.string = message
    new_text['bgcolor'] = frame_color
    #new_text['style'] = "border: 3px solid blue; vertical-align: bottom; color: white; font: Helvetica; font-size: 10; max-width: 30"
    new_text['style'] = "border: 3px solid blue; vertical-align: bottom; color: white; font: Helvetica; font-size: 10"

    #print(messagelist)
    #print(new_message.prettify())

def generate_short_answer(html_raw, title, subject, mailID, text1, userExpireDate):
    """
    Injects Textsegments into the answer template.
    :param sender:
    :param subject:
    :param html_raw:
    :param reply:
    :return:
    """
    #print()
    #print('Generate answer______________________')

    html = BeautifulSoup(html_raw, 'html.parser')
    answer = ShortAnswer()

    # Title of the original mail
    #print('Search for:', Answer.title)
    insertpoint = html.body.find(text = Answer.title).parent
    insertpoint.string = title
    answer.title = title

    # Subject of the original mail
    #print('Search for:', Answer.subject)
    insertpoint = html.body.find(text = Answer.subject).parent
    insertpoint.string = subject
    answer.subject = subject

    # ID of the original mail
    #print('Search for:', Answer.subject)
    insertpoint = html.body.find(text = Answer.mailID).parent
    ID = 'CTDE-'+str(mailID)
    insertpoint.string = ID
    answer.id = ID

    # Text
    #print('Search for:', Answer.fastanswer)
    insertpoint = html.body.find(text = Answer.fastanswer).parent
    insertpoint.string = text1
    answer.text = text1

    # And safe it into the folder.
    #print('Safe answer to file:', '"F_'+subject+'.html"')
    #analysisHTML.safe_file('F_'+subject, html)

    answer.html = html
    return answer

