German: (see english Description below)

Ein paar Tools um auf einfache Weise Attachments aus Emails zu extrahieren und in bestimmte Ordner zu speichern.

Eines der Tools "Fotoextractor" dient z.B. dazu aus Emails in deren Anhang sich Fotos befinden genau diese Fotos in einen gewünschten Ordner auf dem Computer oder einem angeschlossenen NAS zu speichern. Anstatt im Mailclient irgendwo auf "Anhänge herunterladen" zu clicken und dann in einem Filebrowser den Zielordner zu suchen, wo man sich mitunter extra nochmal mit der Synology verbinden muss und sein Passwort nochmals eingeben muss ... genügt es bei diesem Tool das Mail an eine einmal eingerichtete eigene Mailadresse (z.B. fotosave@irgendeineeigenedomain.com) weiterzuleiten. Ein Cronprozess fragt alle paar Minuten diese Mailadresse ab, lädt allfällige Bildanhänge auf die Synology in einen vordefinierten Ordner (z.B. photos/Bilder_von_Emails/...), löscht dann das weitergeleitete Mail auf dem Mailserver und sendet ein Bestätigungsmail an meine original Mailadresse von der aus ich das Mail weitergeleitet habe ("3 Fotos from ... successfully saved to ..."). Das Originalmail wird dabei nicht angetastet. Mails, die nicht von mir (meiner Mailadresse, der meiner Frau, meiner Kinder usw. gesendet wurden) werden ignoriert und gelöscht.
Schreibe ich in den Betreff des weitergeleiteten Mails: "O: Hans", wird in meinem vordefinierten Ordner ein neuer Unter-Ordner mit dem Namen "Hans" angelegt und die Fotos darin gespeichert.
Schreibe ich in den Betreff des weitergeleiteten Mails: "O: Hans   allfrom: hans@mailadresse.xy", werden zukünftig alle Mails von dieser Mailadresse in dem Unter-Ordner "Hans" gespeichert auch ohne, dass ich den Betreff der Mail verändere.
Ein weiterer praktischer Vorteil: Ich habe zuletzt einige Fotos von "Hans" vergessen manuell zu sichern. Aber in welchem Mail waren die nur? Einfach im Mailclient nach den Mails von "Hans" filtern und die vom letzten Jahr an den Mailextractor weiterleiten. Schon sind mit sicherheit alle Fotos von "Hans" aus dem letzten Jahr gesichert. (Wesentlich einfacher als alle Mails manuell durchzugehen und überall "Anhänge sichern" anzuclicken.)
 
Das Selbe lässt sich mit Dokumenten oder Rechnungen im Anhang von Emails machen. Rechnungen werden aber vielleicht gleich mit einer Rechnungsnummer versehen und ausgedruckt. Allfällige als PDF-Anhang getarnte "rechnug.pdf.exe" files werden erkannt und gelöscht mit entsprechender Warnung im Bestätigungsmail.
 
Noch eleganter ließe sich das sicherlich machen, wenn man den Mailserver seines NAS dazu verwendet (was ich aktuell nicht mache). Dann müsste das weitergeleitete Mail den NAS möglicherweise gar nicht mehr verlassen.
Bei mir laufen diese Prozesse zur Zeit auch auf einem zusätzlichen RaspberryPi weil ich Skrupel habe, auf meinem NAS irgendwelche eigenen Scripts laufen zu lassen. 

English:
Extract mail attachments to folders by simply forwarding your mails to a dedicated mailaddress. A cronejob on a raspberryPi runs these scripts. They download the mails from the mail-account, and save the attachments to dedicated folders.
