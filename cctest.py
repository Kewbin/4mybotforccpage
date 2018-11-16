import schedule
import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import urllib
import urllib.request as urllib2
import datetime
import re

print("bot started")

def job():
    #Google Spreadsheets
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.txt', scope)
    clienter = gspread.authorize(creds)
    
    sheet = clienter.open('CC Players').sheet1
    date = datetime.date.today().strftime("%Y/%m/%d")
    #print(date)
    time = datetime.datetime.now().time().strftime("%H:%M")
    #print(time)
    aResp = urllib2.urlopen("http://cubiccastles.com/")
    webpage = aResp.read()
    row_count = sheet.acell("E1").value
    
    nouo = re.findall(r'<br/>(.*?)<br/>',str(webpage))
    for eachA in nouo:
                nouo1 = eachA[26:]

    #print(nouo1)

    row = [date + " " + time, int(nouo1)]
    index = int(row_count) + 1
    sheet.insert_row(row, index)

schedule.every(30).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
