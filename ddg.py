import urllib3
from bs4 import BeautifulSoup
import re

def ddg_search(str):
    print('searching duckduckgo...', end='')
    s = sanitize_phrases(str)
    url = 'https://api.duckduckgo.com/?format=xml&pretty=1&q=' + s.lower() 
    xml = urllib3.PoolManager()
    data = xml.request('GET', url).data
    soup = BeautifulSoup(data, 'xml')
    try:
        if soup.find('Abstract').get_text() == '':
            print('not found!')
            return ''
        print('found!')
        return soup.find('Abstract').get_text() + '\nMore: ' + soup.find('AbstractURL').get_text()
    except:
        print('not found!')
        return ''

def sanitize_phrases(q):
    s = re.sub('(?<!\w)(richard)(?!\w)', '', q, re.IGNORECASE).lower()
    s = re.sub('(?<!\w)(what|who|where|who\'s|who\'re|what\'s|what\'re|what\'s)(?!\w)', '', s, re.IGNORECASE)
    s = re.sub('(?<!\w)(tell me about|find info about)(?!\w)', '', s, re.IGNORECASE)
    s = re.sub('(?<!\w)(do you know)(?!\w)', '', s, re.IGNORECASE)
    s = re.sub('(?<!\w)(can you)(?!\w)', '', s, re.IGNORECASE)
    s = re.sub('(?<!\w)(is|are|was|were)(?!\w)', '', s, re.IGNORECASE)
    s = re.sub('(?<!\w)(research)(?!\w)', '', s, count=1, flags=re.IGNORECASE)
    s = s.strip().strip('?.!').lower()
    s = re.sub(' +', ' ', s)
    return s