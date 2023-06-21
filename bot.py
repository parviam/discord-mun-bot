# bot.py
import research
import random
import discord
from discord.ext import tasks
import re
import ddg
import time
from bs4 import BeautifulSoup
import urllib3

token = open('TOKEN.txt', 'r').read()
server = ''

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#un news thing
last_message_time = time.time()
@tasks.loop(hours = 1.0)
async def add_news():
        global last_message_time
        rel_channel = client.get_channel(963993489429917739)
        t = time.time()
        if t - last_message_time > random.randint(86400, 10000+86400):
            last_message_time = t
            #await rel_channel.send(get_news_link('all'))

@client.event
async def on_ready():
    print('Richard activated...')
    add_news.start()

def compliment(n):  #Todo
    return 'prizers'

def has_thanking(str):
    p = re.compile('(?<!\w)(ty+|tysm+|thx+|thanks|thank u+|thank you+|gracias+|dank+|danke|dankesch|dank u+)(?!\w)',re.IGNORECASE)
    return p.search(str) is not None

def mentions_ai(str):
    p = re.compile('(?<!\w)(ai|machine learning|ml|artificial intelligence)(?!\w)', re.IGNORECASE)
    return p.search(str) is not None

def has_panic(str):
    if 'lmao' in str.lower():
        return False
    if str.upper() == str and len(str) > 4: #change to regex
        return True
    if 'AAAAAA' in str:
        return True
    return False

def has_celebration(str):
    p = re.compile('(?<!\w)(yay+|wooo+|congrats+|congratulations+|bravo+|hooray+)(?!\w)', re.IGNORECASE)
    return p.search(str) is not None

def to_richard(str):
    p = re.compile('(richard)|(.*( richard)$)', re.IGNORECASE)
    q = re.compile('(richie)|(.*( richie)$)', re.IGNORECASE)
    return (p.match(str) is not None or q.match(str) is not None)

def respond_direct(prompt):
    print('message to richard detected!')
    answer = conf_info(prompt)
    if answer == '':
        answer = news_find(prompt)
    if answer == '':
        answer = answer_parlipro(prompt)
    if answer == '':
        answer = research.research(prompt)
    if answer == '':
        answer = ddg.ddg_search(prompt)
    if answer == '' and has_thanking(prompt):
        answer = random.choice(['You are most welcome!', 'It was my pleasure!', 'Mhm', 'Of course!', 
                                'And thank you!', 'Ty!', 'yw', 'You are the welcomest!',
                                'It was nothing more than my duty!', 'Anytime!', 'You helped!'])
    if answer == '':
        answer = greeting(prompt)
    if answer == '' and 'do better' in prompt:
        answer = random.choice(['I try mine best', ':(', '💔', 'D:', 'Ah.', 'Silence, unbeliever!'])
    if answer == '':
        answer = no_idea(prompt)
    return answer

def answer_parlipro(str):
    if re.compile('(?<!\w)(unmod|unmoderated caucus|unmoderated)(?!\w)', re.IGNORECASE).search(str) is not None:
        return '''Unmoderated caucuses are when delegates can get up from their seat and walk around, interrupting normal debate. This is often used to gather support, talk to key partners, or write a resolution. To motion for an unmoderated caucus, say \"<DELEGATION> motions for a <DURATION> minute unmoderated caucus.\" Importantly, unmoderated caucuses need no topic.
        Try this: https://muninfopedia.home.blog/2019/03/07/unmoderated-caucus/ '''
    elif re.compile('(?<!\w)(mod|moderated caucus|moderated)(?!\w)', re.IGNORECASE).search(str) is not None:
        return '''A moderated caucus, or a mod, is a period of formal debate, where speakers will give speeches on their perspective about a topic. For example, South Korea might talk about the DMZ during a moderated caucus on "Current Issue," if the currently debated issue is Addressing Destabilization on The Korean Peninsula. To motion for a moderated caucus, try \"<> motions for a <> minute mod with a speaking time of <> on the topic of <>\" Remember that your total time must be divisible by your speaking time!
        Try this: https://munuc.org/speaking-part-1/'''
    elif re.compile('(?<!\w)(point|points)(?!\w)', re.IGNORECASE).search(str) is not None:
        return '''There are three points. All points may interrupt a speaker or even the chair. Let us go through them at once!
        POINT OF ORDER -
        A point of order is appropriate when a member finds a procedural error made by the chair or by another delegate. A member-state making such a motion may not speak on the substantive issue at hand, but must limit remarks to the precise procedural point in question. 
        POINT OF PERSONAL PRIVILEGE - 
        A point of personal privilege is appropriate when a member is experiencing a personal discomfort that impairs his or her ability to participate in debate. The chair will attempt to remedy the problem. 
        POINT OF PARLIAMENTARY INQUIRY - 
        A point of parliamentary inquiry may be raised when a member is unsure of the committee's proceedings or status. Such a point may address questions including, but not limited to parliamentary procedure, the status of the speakers' list, or the status of a resolution and/or amendment. The chair shall answer the point before debate proceeds. 
        To make a point, respectfully call out beyond your brethren:
        \"Point of <>. <POINT>.\"
        For instance:
        \"Point of Personal Privilege. The delegation's wayward countenance leads to difficult attention towards their attempts at wit.\"
        \"Point of Order. The moderated caucus penultimate in the order was mistakenly ignored for a procedural vote.\"  
        \"Point of Parliamentary Inquiry. When is the correct time to divide this paper in twain?\"
        For a further understanding, gaze your tempestuous sights upon:
        https://www.munprep.org/blog-home-page/mun-points-and-motions-how-to-use-them-properly'''
    elif re.compile('(?<!\w)(yield|yields)(?!\w)', re.IGNORECASE).search(str) is not None:
        return '''During formal debate, all speakers may yield any remaining time in one of three ways. All yields must be announced to the chair before the speaker begins his or her remarks. Yields are only allowed during the speakers list. Let us walk through them at the present moment, as a blade of grass displayed upon the summer wind:
        YIELD TO THE DAIS/CHAIR -
        The speaker may yield to the chair, abdicating their time and returning to the prison they name their desk.
        YIELD TO POINTS OF INFORMATION -
        The speaker may yield to points of information from other member-states. Questions asked of a delegate will not count against what time remains. Once a speaker has yielded to points of information, any member-state that wishes to make such a motion will signify so by raising the delegation's placard. The chair will recognize a delegation which may then ask one question. 
        YIELD TO ANOTHER DELEGATION -
        The speaker may yield time to another member-state by informing the chair which member shall receive the balance of the speaking time before any remarks are made. Neither delegation will be able to yield to points of information. 
        To yield, simply state with great confidence:
        \"We now yield the remainder of our time to: <THE CHAIR/POINTS OF INFORMATION/THE DELEGATION OF>\"
        To feed\’st thy light\’s flame with further self-substantial fuel: https://docs.google.com/document/d/11iKWptlU39CySy4vLO6aDhx9CMaWHsZBTUqgPLmt8aE/edit?usp=sharing'''
    elif re.compile('(?<!\w)(voting procedure|voting order)(?!\w)', re.IGNORECASE).search(str) is not None:
        return '''Voting procedure shall occur when a motion to debate passes, or the half-wits in thine committee have foolishly allowed the well of the speakers list to run dry. Here is what shall occur:
        - All doors will be barred. All communication between delegates must cease under pain of death. 
        - Hostile amendments will be voted on in the order they were recieved. At GSMSTMUNC, 2/3 must vote for amendment approval in order to save them from the wastes of history.
        - Motions will be requested. At this vital juncture, thine options are few: divide, motion for roll call, or remain silent. If no motions are called for, a placard vote shall ensue.
        - Any divisions of the question will be voted upon.
        - Draft resolutions shall be voted on in the order they were received. Unless thou hath placed thineselves within the bowels of the Security Council, a majority is sufficient to pass.
        After all resolutions have lived or died, voting procedure shall end. The final motion of committee will be to adjourn it, requiring a 2/3 majority to pass.
        When the fateful time comes, thou must vote: \"yes,\" \"no,\" \"no with rights,\" \"yes with rights,\" \"pass,\" or \"abstain.\" The latter is available only to those who are only \"Present," and not "Present and Voting.\" 
        Passing forcest thou to the end of thine queue in a roll-call vote, buying time. When thou votest \"with rights,\" thou must perform a speech upon your decision, upon the chair's universal discretion.
        Feast thine minds further: https://teimun.org/mun-101-the-rules-of-procedure/'''
    elif re.compile('(?<!\w)(ultimate bkgd|ult bkgd|ultimate background|ult background)(?!\w)', re.IGNORECASE).search(str) is not None:
        return 'Thy document, as old as the sands of time: https://docs.google.com/document/d/1_33AteI8TpO2aypneuyNo0VWxopc801GAOI7Tspy5TE/edit?usp=sharing'
    return ''

def greeting(str):
    p = re.compile('(?<!\w)(hi+|hello+|hullo+|hey+|howdy|good morning+|good evening+|good afternoon+|gm+)(?!\w)', re.IGNORECASE)
    if p.search(str) is not None:
        hellos = ['Asalaam alaikum',
    'Zdrasti',
    'Zdraveĭte',
    'Nǐ hǎo',
    'Nǐn hǎo',
    'Hallo',
    'Goede dag',
    'Hey',
    'Hello',
    'Salut',
    'Bonjour',
    'Hug',
    'Dia dhuit',
    'Hallo',
    'Guten tag',
    'Yasou',
    'Kalimera',
    'Shalom',
    'Shalom aleichem',
    'Hē',
    'Namastē',
    'Halló',
    'Góðan dag',
    'Salam!',
    'Selamat siang',
    'Ciao',
    'Salve',
    'Yā,_Yō',
    'Konnichiwa',
    'Suosdei',
    'Suostei',
    'Anyoung',
    'Anyoung haseyo',
    'Hej',
    'Cześć',
    'Cześć!',
    'Dzień dobry!',
    'Oi',
    'Olá',
    'Hei',
    'Bună ziua',
    'Privet',
    'Zdravstvuyte',
    '¿Qué tal?',
    'Hola',
    'Hujambo',
    'Habari',
    'Hej',
    'God dag',
    'Ia ora na',
    'Ia ora na',
    'Selam',
    'Merhaba',
    'Chào',
    'Xin chào',
    'Helo',
    'Shwmae',
    'Sawubona',
    'Ngiyakwemukela',
    'Yo',
    'Hi',
    'Well met',
    'Prithee',
    'Greetings',
    'How dost you?',
    'And to you!',
    'Aye!']
        return random.choice(hellos)
    p = re.compile('(?<!\w)(bye+|ttyl+|see ya+|see you+|goodbye+)(?!\w)', re.IGNORECASE)
    if p.search(str) is not None:
        byes = ['Goodbye!', 'And to you!', 'Until next time!', 'Until later!', 'See you soon!', 'Goodbye.', 'It was a pleasure.', 'Pleased to have seen you!']
        return random.choice(byes)
    p = re.compile('(?<!\w)(wish me|wish us|wish them|wish her|wish him)(?!\w)', re.IGNORECASE)
    if p.search(str) is not None:
        return random.choice(['Good luck', 'Best of luck!', 'I wish you much joy.', 'May your tribulations be successful.', 
                              'May the odds ever be in your favor.', 'Best wishes!', 'Best, \nRichard'])
    p = re.compile(re.escape('(?<!\w)(howre you+|how are you+|hows it going+|)(?!\w)'), re.IGNORECASE)
    if p.search(str) is not None:
        return random.choice(['Valorous, how art thee?' ,
                              'As good as the sun shall rise on the morrow',
                               'Marvelous',
                               'Perhaps better some days',
                               'Committing to finishing mine position paper',
                               'As of now I am writing a resolution',
                               'I am attempting to recall precedence for motions',
                               'Tired, but in good health',
                               'Filled with wayward melancholy and nuclear strategy',
                               'Tooketh with boundless joy and pride',
                               'Not restful',
                               'Filled with anticipation',
                               'As the bunch of grapes that wast did press into wine'])
    return ''

def no_idea(str):
    print('activating eliza bot...')
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
    print('looking for conference request...')
    GSMSTMUNC = {
        'name': 'GSMSTMUNC',
        'website': 'https://sites.google.com/view/gsmstmunc/home',
        'date': 'Saturday, September 30th',
        'committees': ['GA1', 'GA6', 'SC', 'The War of the Roses', 'UNESCO'],
        'awards': ['Outstanding Delegate', 'Honorable Mention', 'Commendable Position Paper'],
        'rules': 'https://sites.google.com/view/gsmstmunc/gsmstmunc-x/rules-awards',
        'delegation_awards': True
    }
    GTMUNC = {
        'name': 'GTMUNC',
        'website': 'https://gtmun.gatech.edu/gtmun-hs/',
        'date': 'October 9th and 10th',
        'committees': ['GA Plenary', 'GA1', 'GA2', 'GA3' , 'GA6', 'UNEP', 'CSTD', 'IAEA', 'African Union', 'WHO', 'Ad-Hoc', 'UNESCO', 'Press Corps', 'Meta Oversight Board'],
        'awards': ['Best Delegate', 'Outstanding Delegate', 'Honorable Delegate'],
        'rules': 'http://www.gtmun.gatech.edu/wp-content/uploads/2021/03/Delegate-Guide-2021.pdf',
        'delegation_awards': False
    }
    GSUMUNC = {
        'name': 'GSUMUNC Fall',
        'website': 'http://gsumun.org/index.html',
        'date': 'November',
        'committees': ['The fools at GSU have refused to reveal their committees!'],
        'awards': ['GSU fails to provide induvidual awards - a show of cowardice!'],
        'rules': 'http://gsumun.org/Resources.html',
        'delegation_awards': True        
    }
    KSUMUNC = {
        'name': 'KSUMUNC',
        'website': 'https://conference.kennesaw.edu/hsmun/index.php',
        'date': 'an unknown time',
        'committees': ['The fools at KSU have refused to reveal their committees!'],
        'awards': ['With fortune I endeavor to inform thou that I know not of the awards provided.'],
        'rules': 'https://conference.kennesaw.edu/hsmun/delegate-preparation.php',
        'delegation_awards': False        
    }
    UGAMUNC = {
        'name': 'UGAMUNC',
        'website': 'https://www.ugamunc.com/',
        'date': 'an unknown time',
        'committees': ['The fools at UGAMUNC have refused to reveal their committees!'],
        'awards': ['With fortune I endeavor to inform thou that I know not of the awards provided.'],
        'rules': 'https://www.ugamunc.com/rules-and-procedures/',
        'delegation_awards': True           
    }
    answer = ''
    if 'gsmstmun' in prompt.lower():
        conference = GSMSTMUNC
    elif 'gtmun' in prompt.lower():
        conference = GTMUNC
    elif 'gsumun' in prompt.lower():
        conference = GSUMUNC
    elif 'ksumun' in prompt.lower():
        conference = KSUMUNC
    elif 'ugamun' in prompt.lower():
        conference = UGAMUNC
    else:
        print('not found!')
        return answer
    print('found ' + conference['name'])
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
    if 'rules' in prompt.lower() or 'conduct' in prompt.lower():
        answer += random.choice(['For your pleasure, the rules of procedure: ',
                                 'When thou willst, the rules upon which proceedings occur: ',
                                 'Under the roofes of ' + conference['name'] + ', the following rules shalt apply: ',
                                 'Gaze upon this majestic document of procedure and cower in acceptance: ',
                                 'Behold! Rules! '])
        answer += conference['rules'] + '\n'

    answer += random.choice(['Behold! The website of the ' + compliment(2) + ' at ' + conference['name'] + ': ',
                             'Be amazed by the site on the web: ',
                             'O what wonders of technology! Here, gaze thine eyes upon the beauty of progress! Observe thine site! ',
                             'I hadh\'t endow upon ye thine information: ',
                             'I bring you tales of the fabled meeting of minds: '])
    answer += conference['website']
    return answer

def news_find(str):
    print('looking for request for news...')
    p = re.compile('(?<!\w)(story+|stories+|news+)(?!\w)', re.IGNORECASE)
    if p.search(str) is None:
        print('not found!')
        return ''
    print('found!')
    return get_news_link(str)

def get_news_link(s):
    str = s.lower()
    print('getting news link, ')
    if 'climate c' in str:
        print('topic: climate change')
        url = 'https://news.un.org/feed/subscribe/en/news/topic/climate-change/feed/rss.xml'
    elif 'women' in str:
        print('topic: un women')
        url = 'https://www.unwomen.org/en/rss-feeds/news'
    elif 'economic' in str:
        print('topic: economic and social council')
        url = 'https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml'
    elif 'health' in str:
        print('topic: health')
        url = 'https://news.un.org/feed/subscribe/en/news/topic/health/feed/rss.xml'
    elif 'geneva' in str:
        print('location: un geneva')
        url = 'https://www.ungeneva.org/news-media/press-releases-list/rss.xml'
    elif 'human' in str:
        print('topic: human rights')
        url = 'https://news.un.org/feed/subscribe/en/news/topic/human-rights/feed/rss.xml'
    elif 'sdg' in str or 'sustainable de' in str:
        print('topic: SDGs')
        url = 'https://news.un.org/feed/subscribe/en/news/topic/sdgs/feed/rss.xml'
    elif 'middle east' in str:
        print('region: middle east')
        url = 'https://news.un.org/feed/subscribe/en/news/region/middle-east/feed/rss.xml'
    elif 'asia' in str:
        print('region: asia')
        url = 'https://news.un.org/feed/subscribe/en/news/region/asia-pacific/feed/rss.xml'
    elif 'africa' in str:
        print('region: africa')
        url = 'https://news.un.org/feed/subscribe/en/news/region/africa/feed/rss.xml'
    elif 'europe' in str:
        print('region: europe')
        url = 'https://news.un.org/feed/subscribe/en/news/region/europe/feed/rss.xml'
    elif 'america' in str:
        print('region: americas')
        url = 'https://news.un.org/feed/subscribe/en/news/region/americas/feed/rss.xml'
    else:
        print('no region found, sharing generic story')
        url = 'https://news.un.org/feed/subscribe/en/news/all/rss.xml'
    
    xml = urllib3.PoolManager()
    data = xml.request('GET', url).data

    soup = BeautifulSoup(data, 'xml')
    links = soup.find_all('link')
    all_news = []
    for link in links:
        all_news.append(link.get_text())
    print(all_news)
    all_news = [link for link in all_news if ('story' in link or 'doc' in link)]
    print(all_news)
    return(random.choice(all_news))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    prompt = message.content
    print('\n\nmessage recieved.......\n', prompt)
    response = ''
    global last_message_time
    last_message_time = time.time()

    if has_thanking(prompt):
        print('thanking detected')
        await message.add_reaction('🤍')

    if mentions_ai(prompt):
        print('ai detected')
        await message.add_reaction(random.choice(['🦾', '👁️', '🤖']))

    if 'united nations' in prompt.lower():
        print('united nations detected')
        await message.add_reaction('\U0001F1FA\U0001F1F3')
    
    if 'sovereignty' in prompt.lower():
        print('sovereign detected')
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
        print('panic detected')
        if random.random() > 0.4:
            await message.add_reaction(random.choice(['❗', '\U0000203C', '😱', '🤯']))
        else:
            response = random.choice(['!!!!!', prompt + '!!!!!!', '😱😱😱', 'FR?????????', 'VERILY!!!!', 'WHEREFORE!?!?!?????'])

    if has_celebration(prompt):
        print('celebration detected')
        await message.add_reaction(random.choice(['🎉', '🎊', '🦾', '🍾' ,'🥂', '🧁', '🎆',]))
        response = random.choice(['Yay!', 'YAY', 'Whoo!', 'A hearty congratulations to you all.', 'Celebrations!', 'Well done!', 'What an accomplishment!', 'A toast in your honor!',
                                  'I commend you!', 'I\'m proud of you', 'Felicitations.'])

    if to_richard(prompt):
        response = respond_direct(prompt)

    if 'parlibro' in prompt.lower():
        print('parlibro detected')
        response = random.choice(['Thou art my parlibro <3',
                                  'Parlibro!',
                                  'Parlibro: brother in parlimentary procedure.',
                                  'The greatest parlibros art also parlipros',
                                  'Art not all great parlibros parlipros?',
                                  'Parlibro, parlibro, wherefore art thou parlibro?'
                                  ])

    if not (response == ''):
        print('response generated: ' + response)
        await message.channel.send(response)
    print('end message response sequence~')

client.run(token)