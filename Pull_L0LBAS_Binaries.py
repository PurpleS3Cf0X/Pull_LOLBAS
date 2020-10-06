import requests
from bs4 import BeautifulSoup
import csv
from os import getcwd

print('\n'*3)
print("         /~________~\  .----------. (| L0L Pull |) '----------'  \_~~~~~~~~_/ ")
print('\n'*3)
print("                                                 .: Author- Jean Paul :.      ")
print('\n'*3)

current_directory=getcwd() 
print("               Your Current Working Directory is  : \n",current_directory)
outpath=current_directory+"\\l0lB@S_Output.csv"
myFile = open(outpath, 'a+',newline='')
csv_out = csv.writer(myFile)
csv_out.writerow(["Name","BInary_Link","Function","Code(s)"])
url="https://lolbas-project.github.io"
r=requests.get(url)
print('_'*60)
print("Connected to LOLBAS: ",url)
print('\n'*3)
soup=BeautifulSoup(r.content)

for tag in soup.find_all('a','bin-name'):
    hrefs=tag['href'].replace("//","")
    urls=url+hrefs
    for ur in [urls]:
        nr=requests.get(ur)
        sups=BeautifulSoup(nr.content, "html.parser")
        print('_'*60)
        funclist=[[t.text for t in f.find_all('a')] for f in sups.find_all('ul','function-list')]
        code=[i.text for i in sups.find_all('code')]
        print("Working on binary",tag.text," at location ",ur," ::::Contains ",funclist)
    csv_out.writerow([tag.text,urls,funclist,code])