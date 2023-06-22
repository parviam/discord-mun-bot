import urllib3
from bs4 import BeautifulSoup
import re

def ddg_search(str):
    print('searching duckduckgo...', end='')
    s = clean_question(str)
    url = 'https://api.duckduckgo.com/?format=xml&pretty=1&q=' + s.lower() 
    xml = urllib3.PoolManager()
    data = xml.request('GET', url).data
    soup = BeautifulSoup(data, 'xml')
    try:
        if soup.find('Text').get_text() == '':
            print('not found!')
            return ''
        print('found!')
        return soup.find('Abstract').get_text() + '\nMore: ' + soup.find('AbstractURL').get_text()
    except:
        print('not found!')
        return ''

def clean_question(q):
    s = re.sub('(?<!\w)(richard)(?!\w)', '', q).lower()
    s = re.sub('(?<!\w)(what|who|where|who\'s|who\'re|what\'s|what\'re|what\'s)(?!\w)', '', s)
    s = re.sub('(?<!\w)(tell me about|find info about)(?!\w)', '', s)
    s = re.sub('(?<!\w)(do you know)(?!\w)', '', s)
    s = re.sub('(?<!\w)(can you)(?!\w)', '', s)
    s = re.sub('(?<!\w)(is|are|was|were)(?!\w)', '', s)
    s = re.sub('(?<!\w)(research)(?!\w)', '', s)
    s = s.strip().strip('?.!').lower()
    return s