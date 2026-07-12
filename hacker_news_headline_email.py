import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

#email content placeholder
content = ''

#extracting Hacker News Stories

def extract_news(url):
    # print('Extracting Hacker News Stories....')
    # cnt = '' 
    # cnt += ('<b>HN Top Stories:</b>\n' + '<br>'+ '-'*50+'<br>')

    # response = requests.get(url)
    # content = response.content
    # soup = BeautifulSoup(content, 'html.parser')
    # for i, tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
    #     cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
    # return cnt
    print("Extracting Hacker News Stories...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    cnt = "<b>HN Top Stories:</b><br><br>"

    titles = soup.select("span.titleline > a")

    for i, title in enumerate(titles[:10], start=1):
        headline = title.get_text()
        link = title.get("href")

        cnt += f"{i}. <a href='{link}'>{headline}</a><br><br>"

    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

#Send email
SERVER = 'smtp.gmail.com' #smtp server
PORT = 587
FROM = 'maheshwariinamadar28@gmail.com'
TO = 'maheshwariinamadar28@gmail.com'
PASS = 'dvzy ogjf ocwc urcf' #password

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' +str(now.day) + '-' +str(now.month) + '-' +str(now.year)

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')
server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()
