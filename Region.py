__author__ = 'oliver'
"""
This file serves to regionalize the system
"""

class Answer():
    #this_folder      = '/home/clixpi/cliXecure/checkThis/'      # für Raspberry
    this_folder      = ''                                       # für Mac
    templates_folder = this_folder + 'Templates/'
    answer_folder    = this_folder + 'Antworten/'
    logs_folder      = this_folder + 'logs/'

    template_html_fastanswer  = ''
    template_html_mainanswer  = 'Hauptantwort_de'
    fastanswer = '-FASTANSWER-'
    title    = '-TITLE-'
    subject  = '-SUBJECT-'
    mailID   = '-MAILID-'
    date     = '-DATE-'
    time     = '-TIME-'
    warning  = '-WARNING-'
    warntext = '-WARNTEXT-'
    mailtext = '-MAILTEXT-'
    attachment = '-ATTACHMENT-'
    warning_high = ["!! GEFÄHRLICH !!", "Reagiere NICHT auf dieses Mail!"]
    warning_mid  = ["!Bedenklich!", "Sei VORSICHTIG mit diesem Mail!"]
    warning_low  = ["Unbedenklich", "Wir konnten nichts Verdächtiges", "an diesem Mail finden."]
    warning_score_high = 50
    warning_score_mid  = 30
    warning_score_low  = 10
    answer_total_high = 50
    answer_total_mid  = 30
    answer_total_low  = 10


class Region():
    MailHostIn = 'imap.gmx.net'
    MailHostInPort = 993
    MailHostOut = 'mail.gmx.net'
    MailHostOutPort = 587
    MailAddress = 'dokumentextraktor@lass-es-geschehen.de'
    MailPasswd  = 'r5e4vgi9lplpo0'
    MailName    = 'Dokumenten Extraktor'
    MailSSL = True
    MailCheckAll = 'UNSEEN'  # 'UNSEEN' or 'ALL'


class Replystrings():
    fastTitle_soon = "Willkommen bei"
    fastSubject_soon = "cliXecure analysiert jetzt dein Mail"
    fastReply_soon = "In Kürze erhältst du ein weiteres Mail von uns mit dem Ergebnis unserer Analyse."

    fastTitle_no   = "Danke für dein Vertrauen"
    fastSubject_no = "cliXecure ist nicht umsonst"
    fastReply_no   = "Leider ist dein Testzeitraum abgelaufen. Du kannst erst wieder um %s " \
                     "eine Gratisanalyse durchführen."
    fastReply_no_2 = "Du kannst bis zu 3 gratis Analysen innerhalb von 3h abrufen. " \
                     "Danke für dein Verständnis."

    sorryTitle     = "SORRY"
    sorrySubject   = "Sorry. Dein Mail hat unser System verwirrt."
    sorryReply     = "Hier ist cliXecure. Es tut uns leid. Bei der Analyse deines Mails ist leider ein Problem aufgetreten. " \
                     "Aber deshalb testen wir ja. Wir sehen uns die Sache an und versuchen dir sobald wie möglich ein Ergebnis zu senden. " \
                     "Dein cliXecure-Team."

    opener1 = "Hier ist das Ergebnis der cliXecure "
    opener2 = "-Analyse:"
    closer1 = "Aufgrund unserer "
    closer2 = "-Analyse betrachten wir dieses Mail zu"
    closer3 = "% als gefährlich."
    disclaimer = "Bitte betrachte unsere Analysen als Hinweise und urteile selbst!"
    text = 'Text'
    html = 'HTML'

    sender_title  = 'Analyse des Absenders: '
    sender_domain = '* achte auf dieDomain: '  #
    sender_domain_ok = '* die Domain des Senders scheint unverdächtig.'
    sender_name   = '. Er bezeichnet sich selbst als: '  #
    sender_mail   = '... mit der Mailadresse: %s'  #
    sender_discl1 = '. !!! Prüfe selbst ob das für dich plausibel ist!'  #
    sender_discl2 = '. !!! Seriöse Unternehmen haben eine Domain mit ihrem eigenen Namen.'  #
    sender_discl3 = '. !!! Achte insbesondere auf Tricks, wie: \"rnicrosoft\"!'  #
    sender_quotes = '* Seriöse Menschen verwenden keine Anführungszeichen in der Bezeichnung von Mailadressen.'
    sender_wired  = '* Die Mailadresse enthält merkwürdige Nummern.'
    sender_bank   = '* In der Adresse findet sich zumindest ein Geld-Begriff, nicht aber in der Domain.'

    subject_title = 'Analyse des Betreffs_______:'
    subject_wired = '* Der Betreff enthält kryptische Ziffern.'
    subject_bank  = '* Im Betreff findet sich zumindest ein Geld-Begriff, nicht aber in der Domain.'

    text_title    = 'Analyse des Inhalts____________:'
    text_banking1 = '* In dem Text scheint es um Geldangelegenheiten zu gehen.'
    text_banking2 = '. !!! Sei besonders achtsam!'
    text_urgent1  = '* Der Text versucht dich zeitlich unter Druck zu setzen.'
    text_urgent2  = '. !!! Lass dich nicht stressen! Stay calm and save your money!'
    text_link     = '* In dem Text gibt es folgenden verdächtigen Link: ---> '
    text_tracking = '. Wenn du diesem Link folgst, wirst du selbst verfolgt! '
    text_img      = '* Dieses Mail enthält Trackingbilder (-pixel).'
    text_all_links1 = '* In diesem Mail haben wir '
    text_all_links2 = ' verdächtige Links gefunden.'
    text_all_imgs1  = '* In diesem Mail haben wir '
    text_all_imgs2  = ' Bilder aus merkwürdigen Quellen gefunden.'
    text_all_domains1 = '* Insgesamt verweisen Links aus diesem Mail auf '
    text_all_domains2 = ' verschiedene Domains.'
    text_all_domains3 = '. Und zwar: '

    text_all_tracking0 = 'Tracking___________________:'
    text_all_tracking1 = '* Wir haben insgesamt '
    text_all_tracking2 = ' Versuche dich zu verfolgen gefunden.'
    text_all_tracking3 = '.     Tracking ist kein Hinweis auf unseriöse Machenschaften,'
    text_all_tracking4 = '.     Wir wollen dir aber zeigen, WO du im Netz verfolgbar bist.'
    text_no_script_check = 'ACHTUNG! Wir prüfen derzeit noch nicht auf gefährliche Scripts!'
    text_no_attach_check = 'ACHTUNG! Dieses Mail enthält Anhänge. Wir prüfen derzeit noch nicht auf gefährliche Anhänge! Öffne im Zweifelsfall NICHT die Anhänge dieses Mails!'

    mail_title  = 'Analyse der Mailadresse: '
    mail_domain = '* Stammt von der Domain: '  #
    mail_name   = '  und bezeichnet sich selbst als: '  #
    mail_discl1 = '. !!! Prüfe selbst ob das für dich plausibel ist!'  #
    mail_discl2 = '. !!! Die im Text einer Mail auftretenden Mailadressen'  #
    mail_discl3 = '. !!! sollten von der gleichen Domain stammen.'  #
    mail_quotes = '* Seriöse Menschen verwenden keine Anführungszeichen in der Bezeichnung von Mailadressen.'
    mail_wired  = '* Die Mailadresse enthält merkwürdige Nummern.'
    mail_bank   = '* In der Adresse findet sich zumindest ein BANK-Begriff, nicht aber in der Domain.'

    link_no_http  = '* Der Link beginnt nicht mit http - das ist sehr suspekt.'
    link_no_https = '* Keine verschlüsselte Seite, daher sicher keine Bank.'
    link_strange_domain = '* Dieser Link führt zu einer fremden Domain!'
    link_tracking = '. Wenn du diesem Link folgst, wirst du selbst verfolgt!'

    img_strange_domain = '* Dieses Bild kommt von einer fremden Domain!'
    img_tracking1 = '. Wenn du dieses Bild siehst, wurdest du bereits verfolgt.'
    img_tracking2 = '. D.h. der Absender der Mail weiß zumindest, dass du das Mail geöffnet hast.'



