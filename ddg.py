import urllib3
from bs4 import BeautifulSoup
import re

def ddg_search(str):
    s = re.sub('(?<!\w)(richard)(?!\w)', '', str, re.IGNORECASE).lower()
    s = re.sub('(?<!\w)(what|who|where|who\'s|who\'re|what\'s|what\'re|what\'s)(?!\w)', '', s)
    s = re.sub('(?<!\w)(tell me about)(?!\w)', '', s)
    s = re.sub('(?<!\w)(do you know)(?!\w)', '', s)
    s = re.sub('(?<!\w)(can you)(?!\w)', '', s)
    s = re.sub('(?<!\w)(is|are)(?!\w)', '', s)
    s = s.strip().strip('?.!')
    url = 'https://api.duckduckgo.com/?format=xml&pretty=1&q=' + s.lower() #need to sanitize nation
    xml = urllib3.PoolManager()
    data = xml.request('GET', url).data
    soup = BeautifulSoup(data, 'xml')
    if soup.find('Abstract').get_text() == '':
        return ''
    return soup.find('Abstract').get_text() + '\n' + soup.find('AbstractURL').get_text()