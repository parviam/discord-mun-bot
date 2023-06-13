# bot.py
import random
import discord
from discord.ext import tasks
import re

import time
from bs4 import BeautifulSoup
import lxml
import urllib3

token = 'MTExNzYyNTE3MTgyMjUxODI5Mw.GIqnfM.IKPXZEasORYFYBJxINcpIiT11Cmd1CL35bCwCE'
server = ''

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#un news thing
def get_news_link(str):
    if str == 'all':
        url = 'https://news.un.org/feed/subscribe/en/news/all/rss.xml'
    elif str == 'middle east':
        url = 'https://news.un.org/feed/subscribe/en/news/region/middle-east/feed/rss.xml'
    data = urllib3.request('GET', url).data
    soup = BeautifulSoup(data, 'xml')
    links = soup.find_all('link')
    all_news = []
    for link in links:
        all_news.append(link.get_text())
    all_news = [link for link in all_news if 'story' in link]
    return(random.choice(all_news))

last_message_time = time.time()
@tasks.loop(seconds = 15.0)
async def add_news():
        global last_message_time
        rel_channel = client.get_channel(1116911241697443840)
        print(rel_channel)
        t = time.time()
        if t - last_message_time > random.randint(86400, 10000+86400):
            last_message_time = t
            await rel_channel.send(get_news_link('all'))

@client.event
async def on_ready():
    print('yay')
    add_news.start()

def compliment(n):
    return 'prizers'

def to_richard(str):
    p = re.compile('(richard)', re.IGNORECASE)
    q = re.compile('.*( richard)$', re.IGNORECASE)
    return (p.match(str) or q.match(str))

def no_idea(str):
    ideas = ['Your words are incomprehensible to me.', 
             'Speak clearly or speak not at all!', 
             'I\'d prefer not to answer', 
             'You confuse me.',
             'You befuddle the mind and frustrate the spirit',
             'Perhaps it is true that I am deaf, for surely your words could not be so badly phrased',
             'I sometimes wonder whether you think before you speak',
             'Please speak once more',
             'Begone, speaker of befuddling words!',
             'Your lack of elucidity is disturbing',
             'I question your teachers of writing.',
             'Please rephrase, fool.',
             'I can find, despite great effort, no clarity in you.',
             'May your elucidate upon that?',
             '??',
             'Did you, a person of no doubt great stature, ask me ' + str + '?',
             'Hmmm?',
             'What?',
             'Wherefore?',
             '...',
             'To answer or not to answer, that is the question.',
             'And what about it?'
             ]
    if '?' in str:
        ideas.append(str[:-1] + '???')
    return random.choice(ideas)

def conf_info(prompt):
    GSMSTMUNC = {
        'name': 'GSMSTMUNC',
        'website': 'https://sites.google.com/view/gsmstmunc/home',
        'date': 'Saturday, September 30th',
        'committees': ['GA1', 'GA6', 'SC', 'The War of the Roses', 'UNESCO'],
        'awards': ['Outstanding Delegate', 'Honorable Mention', 'Commendable Position Paper'],
        'rules': ['https://docs.google.com/document/d/11iKWptlU39CySy4vLO6aDhx9CMaWHsZBTUqgPLmt8aE/edit?usp=sharing'],
        'delegation_awards': True
    }
    GTMUNC = {
        'name': 'GTMUNC',
        'website': 'https://gtmun.gatech.edu/gtmun-hs/',
        'date': 'October 9th and 10th',
        'committees': ['GA Plenary', 'GA1', 'GA2', 'GA3' , 'GA6', 'UNEP', 'CSTD', 'IAEA', 'African Union', 'WHO', 'Ad-Hoc', 'UNESCO', 'Press Corps', 'Meta Oversight Board'],
        'awards': ['Best Delegate', 'Outstanding Delegate', 'Honorable Delegate'],
        'rules': ['http://www.gtmun.gatech.edu/wp-content/uploads/2021/03/Delegate-Guide-2021.pdf'],
        'delegation_awards': False
    }
    GSUMUNC = {
        'name': 'GSUMUNC Fall',
        'website': 'http://gsumun.org/index.html',
        'date': 'November',
        'committees': ['The fools at GSU have refused to reveal their committees!'],
        'awards': ['GSU fails to provide induvidual awards - a show of cowardice!'],
        'rules': ['http://gsumun.org/Resources.html'],
        'delegation_awards': True        
    }
    KSUMUNC = {
        'name': 'KSUMUNC',
        'website': 'https://conference.kennesaw.edu/hsmun/index.php',
        'date': 'an unknown time',
        'committees': ['The fools at KSU have refused to reveal their committees!'],
        'awards': ['With fortune I endeavor to inform thou that I know not of the awards provided.'],
        'rules': ['https://conference.kennesaw.edu/hsmun/delegate-preparation.php'],
        'delegation_awards': False        
    }
    answer = ''
    if 'gsmstmun' in prompt.lower():
        print('gsmstmunc')
        conference = GSMSTMUNC
    if 'gtmun' in prompt.lower():
        conference = GTMUNC
    if 'gsumun' in prompt.lower():
        conference = GSUMUNC
    if 'ksumun' in prompt.lower():
        conference = KSUMUNC
    else:
        return answer
    if 'when' in prompt.lower():
        answer += random.choice([conference['name'] + ' shall take place within ' + conference['date'] + '. ', 
                                 'The conference shalt be held within ' + conference['date'] + '. ',
                                 'As the world is my witness, the conference has been foretold to occur within ' + conference['date'] + '. '])
    if 'committees' in prompt.lower():    
        answer += random.choice(['Thy ' + str(len(conference['committees'])) + ' choices of committee be:',
                                 'In the hallowed halls of ' + conference['name'] + ' thou choices shall be few:',
                                 'Thou hast some fair choice upon which to exhaust the capacities of your wit:'])
        for committee in conference['committees']:
            answer += '\n- ' + committee
        answer += '\n'
    if 'awards' in prompt.lower():
        answer += random.choice(['If thou keep your wit and fill thy mind with determination, thou may recieve: ',
                                 'There are naught but ' + str(len(conference['awards'])) + ' awards: ',
                                 'Sate your appetite for awards at ' + conference['name'] + ' with these and these alone:'])
        for award in conference['awards']:
            answer += '\n- ' + award
        answer += '\n'
        if conference['delegation_awards']:
            answer += random.choice(['Our great team may also be bestowed awards as a unit. ',
                                     'But despair not! Your blumbering incompetence may be covered, for our team may win awards. ',
                                     'The great trophy cases of our school may also be made whole from delegation awards won. '])
    if 'rules' in prompt.lower():
        answer += random.choice(['For your pleasure, the rules of procedure: ',
                                 'When thou willst, the rules upon which proceedings occur: ',
                                 'Under the roofes of ' + conference['name'] + ', the following rules shalt apply: '
                                 'Gaze upon this majestic document of procedure and cower in acceptance: ',
                                 'Behold! Rules! '])
        answer += conference['rules'] + '\n'

    answer += random.choice(['Behold! The website of the ' + compliment(2) + ' at ' + conference['name'],
                             'Be amazed by the site on the web: ',
                             'O what wonders of technology! Here, gaze thine eyes upon the beauty of progress! Observe thine site! ',
                             'I hadh\'t endow upon ye thine information: ',
                             'I bring you tales of the fabled meeting of minds: '])
    answer += conference['website']
    print(answer)
    return answer

def news_find(str):
    p = re.compile("(?<!\w)(story|stories|news)(?!\w)", re.IGNORECASE)
    if not p.match(str):
        return ''
    return get_news_link('all')

def respond_direct(prompt):
    answer = conf_info(prompt)
    if answer == '':
        answer = news_find(prompt)
    if answer == '':
        answer = no_idea(prompt)
    return answer

def has_thanking(str):
    p = re.compile('(?<!\w)(ty+|tysm+|thx+|thanks|thank u+|thank you+|gracias+|dank+|danke|dankesch|dank u+)(?!\w)',re.IGNORECASE)
    return p.match(str) 

def mentions_ai(str):
    p = re.compile('(?<!\w)(ai|machine learning|ml|artificial intelligence)(?!\w)', re.IGNORECASE)
    return p.search(str)

def has_panic(str):
    if 'lmao' in str.lower():
        return False
    if str.upper() == str and len(str) > 4:
        return True
    if 'aaaa' in str.lower():
        return True
    return False

def has_celebration(str):
    p = re.compile('(?<!\w)(yay+|wooo+|congrats+|congratulations+|bravo+|hooray+)(?!\w)', re.IGNORECASE)
    return p.match(str)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    prompt = message.content
    print(prompt)
    response = ''
    global last_message_time
    last_message_time = time.time()

    if has_thanking(prompt):
        await message.add_reaction('🤍')

    if mentions_ai(prompt):
        await message.add_reaction(random.choice(['🦾', '👁️', '🤖']))

    if 'united nations' in prompt.lower():
        await message.add_reaction('\U0001F1FA\U0001F1F3')
    
    if 'sovereignty' in prompt.lower():
        if random.random() > 0.7:
            response = 'Quiet! If thou speakst with more energy, the ' + random.choice(['Chinese', 'Russians', 'North Koreans']) + ' may hear!'
        else:
            response = random.choice(['Full many a glorious morning have I seen flatter the mountain-tops with sovereign eye',
                                      'In nature, sovereign mistress over wrack, As thou goest onwards still will pluck thee back,She keeps thee to this purpose, that her skillMay time disgrace, and wretched minute kill.',
                                      'These sovereign thrones, are all supplied, and filled Her sweet perfections with one self king!',
                                      'A guide, a goddess, and a sovereign, A counsellor, a traitress, and a dear; His humble ambition, proud humility,cHis jarring concord, and his discord dulcet, faith, his sweet disaster',
                                      'You know my father left me some prescriptions Of rare and proved effects, such as his reading And manifest experience had collected For general sovereignty',
                                      'Look here, and at thy sovereign leisure sovereign read',
                                      'And top of sovereignty?',
                                      'Like many nations foreign, my soul consents not to give sovereignty.',
                                      'Tongue-tied ambition, not replying, yielded To bear the golden yoke of sovereignty',
                                      'For I have given here my soul\'s consent To undeck the pompous body of a king; Made glory base and sovereignty a slave'])

    if has_panic(prompt):
        if random.random() > 0.4:
            await message.add_reaction(random.choice(['❗', '\U0000203C', '😱', '🤯']))
        else:
            response = random.choice(['!!!!!', prompt + '!!!!!!' + '😱😱😱' + 'FR?????????', 'VERILY!!!!', 'WHEREFORE!?!?!?????'])

    if has_celebration(prompt):
        await message.add_reaction(random.choice(['🎉', '🎊', '🦾', '🍾' ,'🥂', '🧁', '🎆',]))
        response = random.choice(['Yay!', 'YAY', 'Whoo!', 'A hearty congratulations to you all.', 'Celebrations!', 'Well done!', 'What an accomplishment!', 'A toast in your honor!',
                                  'I commend you!', 'I\'m proud of you', 'Felicitations.'])

    if to_richard(prompt):
        response = respond_direct(prompt)

    if 'parlibro' in prompt.lower():
        response = random.choice(['Thou art my parlibro <3',
                                  'Parlibro!',
                                  'Parlibro: brother in parlimentary procedure.',
                                  'The greatest parlibros art also parlipros',
                                  'Art not all great parlibros parlipros?',
                                  'Parlibro, parlibro, wherefore art thou parlibro?'
                                  ])

    if not (response == ''):
        await message.channel.send(response)

client.run(token)

