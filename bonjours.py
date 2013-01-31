from bs4 import BeautifulSoup
from urlparse import urljoin
from subprocess import call
import pycurl
import cStringIO
import smtplib
import datetime
import time

list = list()
sleep_wait = 60
timeout_value = 20
max_try = 10
fileSexyLady = './heySexyLady'
fileSexyBoys = './toSexyBoys'
gmail_account = "you@gmail.com"
gmail_passwd = "yourPass"
debug = 1

#
# This class is just a custom Exception for Connection problems
#

class ConnectionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#
# This is my object that store the url, the title, the tag (class or id), and the name of the tag
#

class BonneMeuf:
    def __init__(self, url, title, tag, flag):
        self.url = url
        self.title = title
        self.tag = tag
        self.flag = flag
        self.img = ''

#
# get the source code of the page
#
    def getData(self, url) :
        data = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, data.write)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.setopt(c.CONNECTTIMEOUT, timeout_value)
        c.setopt(c.TIMEOUT, timeout_value)
        try:
            c.perform()
        except pycurl.error:
            raise ConnectionError("connexion error")
        return data


#
# get the image link
#
    def getImg(self) :
        data = self.getData(self.url)
        soup = BeautifulSoup(data.getvalue())
        results = soup.find_all('div', attrs={self.tag : self.flag})
        try:
            self.img = urljoin(self.url, results[0].img['src'])
        except IndexError, e:
            raise IndexError("Out of bounds")


#
# Debug function
#
def log(string):
    if (debug == 1):
        print string

#
# send the mail with the list of links
#
def sendMail(list) :
    msg = ''
    for meuf in list:
        msg += "<div><b>"
        msg += meuf.title
        msg += " (" + meuf.url + ")" 
        msg += "</b><br/><a href="
        msg += meuf.img
        msg += "><img width=\"600\" src="
        msg += meuf.img
        msg += "></a></div><br/><br/><br/>"
    msg += "<br/>Bisous!"
    sender = gmail_account
    recipient = ['']
    for line in open(fileSexyBoys, 'r'):
        recipient.append(line.rstrip('\n'))
    subject = 'Jolies choses!'
    body = 'Miam miam, a taaaable !<br/><br/>'
    body = "" + body + msg + ""
    
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: "+sender,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(gmail_account, gmail_passwd)
    log("sent to :")
    log(recipient)
    server.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    now = datetime.datetime.now()
    log(now.strftime("%d-%m-%Y %H:%M:%S"))
    log("----------------------\n\n")
    server.quit()

def bonjours():
    log("\n\n----------------------")
    now = datetime.datetime.now()
    log(now.strftime("%d-%m-%Y %H:%M:%S"))
    for line in open(fileSexyLady, 'r').readlines() :
        tab = line.split('|')
        tab[len(tab)-1] = tab[len(tab)-1].rstrip('\n')
        uneMeuf = BonneMeuf(tab[0], tab[1], tab[2], tab[3])
        list.append(uneMeuf)
    for meuf in list:
        try:
            meuf.getImg()
            log(meuf.img)
        except IndexError, e:
            raise IndexError("Out of bounds")
    sendMail(list)

def main():
    i = 0;
    while i < max_try:
        okay = 0
        try:
            if (okay == 0):
                bonjours()
            okay = 1
            break
        except IndexError, e:
            time.sleep(sleep_wait)
            log('index error')
        except ConnectionError, e:
            log('connexion error')
            time.sleep(sleep_wait)
        except:
            log('other except')
            time.sleep(sleep_wait)
        finally:
            i = i + 1

if __name__ == '__main__':
    main()
