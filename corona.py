import urllib.request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

t = ToastNotifier()
toast = ''
html = None
lst = list()
url = 'https://www.mohfw.gov.in/' 

try:
    handle = urllib.request.urlopen(url)
    html = handle.read()
except urllib.error.HTTPError :
    print("could not open")
    exit
else:
    if html is None: print("server not found")

soup = BeautifulSoup(html,'html.parser')
stat = soup.find('div',{'class':'site-stats-count'}).find_all('li')
for item in stat:
    
    '''
    try/except block is used to avoid error caused by 
    a different element with different set of attributes placed inside the same div
    in the website. it does nothing when encountered the unnecessary element
    '''

    try:
        toast = toast + item.find('span').text +' : '+ item.find('strong').text + '\n'
    except:     
        None
t.show_toast('CORONA STATS IN INDIA',toast,duration=5)
