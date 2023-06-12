# bot.py
import random
import discord
import re

token = 'MTExNzYyNTE3MTgyMjUxODI5Mw.GIqnfM.IKPXZEasORYFYBJxINcpIiT11Cmd1CL35bCwCE'
server = ''

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('yay')

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
             'Did you, a person of no doubt great stature, ask me' + str + '?',
             'Hmmm?',
             'What?',
             'Wherefore?',
             '...',
             'To answer or not to answer, that is the question.',
             'And what about it?'
             ]
    if '?' in str:
        ideas.append(prompt[:-1] + '???')
    return random.choice(ideas)

def respond_direct(prompt):
    return no_idea(prompt)

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
    response = ''

    if has_thanking(prompt):
        await message.add_reaction('🤍')

    if mentions_ai(prompt):
        await message.add_reaction(random.choice(['🦾', '👁️', '🤖']))

    if 'united nations' in prompt.lower():
        await message.add_reaction('\U0001F1FA\U0001F1F3')
    
    if 'sovereignty' in prompt.lower():
        if random.random() > 0.7:
            response = 'Quiet! If thou speakst with more energy, the ' + random.choice(['Chinese', 'Russians', 'North Koreans']) + 'may hear!'
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
                                  'Art not all great parlibros parlibros?',
                                  'Parlibro, parlibro, wherefore art thou parlibro?'
                                  ])

    if response != '':
        await message.channel.send(response)

client.run(token)
