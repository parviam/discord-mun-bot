import urllib3
from bs4 import BeautifulSoup
import re
import ddg
import topics
import countries
import foreign_ministries

#todo: https://support.discord.com/hc/en-us/articles/206342858--How-do-I-disable-auto-embed-

def give_committee_info(str):
    ans = ''
    if 'ga1' in str.lower():
        ans += 'General Assembly First Committee (DISEC) considers all disarmament and international security matters: '
        ans += '\nhttps://www.un.org/en/ga/first/'
    if 'ga2' in str.lower():
        ans += 'General Assembly Second Committee considers all global financial and sustainable development questions, and some other issues: '
        ans += '\nhttps://www.un.org/en/ga/second/'
    if 'ga3' in str.lower():
        ans += 'GA3 (SOCHUM) considers social and humanitarian affairs: '
        ans += '\nhttps://www.un.org/en/ga/third/index.shtml'
    if 'ga4' in str.lower():
        ans += 'GA4 deals with special decolonization, polticial issues, and outer space, and some other issues: '
        ans += '\nhttps://www.un.org/en/ga/fourth/index.shtml'
    if 'ga5' in str.lower():
        ans += 'GA5 deals with the administration and budget of other UN bodies: '
        ans += '\nhttps://www.un.org/en/ga/fifth/index.shtml'
    if 'ga6' in str.lower():
        ans += 'GA6 deals with legal questions: '
        ans += '\nhttps://www.un.org/en/ga/sixth/index.shtml'
    if 'security council' in str.lower() or 'unsc' in str.lower():
        ans += 'The Security Council has primary responsibility for global peace and security. They may place sanctions and deploy peacekeepers: '
        ans += '\nhttps://www.un.org/securitycouncil/'
        ans += '\nSC containth altered rules and reg\'tions. Feast your eyes upon this resource: '
        ans += '\nhttps://bestdelegate.com/five-tips-on-how-to-succeed-in-the-security-council/'
    if 'iaea' in str.lower() or 'international atomi' in str.lower():
        ans += 'The IAEA promotes the safe use of atomic energy and nuclear non-proliferation: '
        ans += '\nhttps://www.iaea.org/about/overview/history'
    return ans

def find_country(str):
    countries = ['Afghanistan',
                'Albania',
                'Algeria',
                'Andorra',
                'Angola',
                'Antigua and Barbuda',
                'Argentina',
                'Armenia',
                'Australia',
                'Austria',
                'Azerbaijan',
                'Bahamas',
                'Bahrain',
                'Bangladesh',
                'Barbados',
                'Belarus',
                'Belgium',
                'Belize',
                'Benin',
                'Bhutan',
                'Bolivia',
                'Bosnia and Herzegovina',
                'Botswana',
                'Brazil',
                'Brunei',
                'Bulgaria',
                'Burkina Faso',
                'Burundi',
                'Cabo Verde',
                'Cambodia',
                'Cameroon',
                'Canada',
                'Central African Republic',
                'Chad',
                'Chile',
                'China',
                'Colombia',
                'Comoros',
                'Congo',
                'Costa Rica',
                'Cote d\'Ivoire',
                'Croatia',
                'Cuba',
                'Cyprus',
                'Czech Republic',
                'Democratic People\'s Republic of Korea',
                'Democratic Republic of the Congo',
                'Denmark',
                'DPRK',
                'Korea',
                'North Korea',
                'South Korea',
                'Djibouti',
                'Dominica',
                'Dominican Republic',
                'Ecuador',
                'Egypt',
                'El Salvador',
                'Equatorial Guinea',
                'Eritrea',
                'Estonia',
                'Eswatini',
                'Ethiopia',
                'Fiji',
                'Finland',
                'France',
                'Gabon',
                'Gambia',
                'Georgia',
                'Germany',
                'Ghana',
                'Greece',
                'Grenada',
                'Guatemala',
                'Guinea',
                'Guinea-Bissau',
                'Guyana',
                'Haiti',
                'Honduras',
                'Hungary',
                'Iceland',
                'India',
                'Indonesia',
                'Iran (Islamic Republic of)',
                'Iraq',
                'Ireland',
                'Israel',
                'Italy',
                'Jamaica',
                'Japan',
                'Jordan',
                'Kazakhstan',
                'Kenya',
                'Kiribati',
                'Kuwait',
                'Kyrgyzstan',
                'Lao People\'s Democratic Republic',
                'Latvia',
                'Lebanon',
                'Lesotho',
                'Liberia',
                'Libya',
                'Liechtenstein',
                'Lithuania',
                'Luxembourg',
                'Madagascar',
                'Malawi',
                'Malaysia',
                'Maldives',
                'Mali',
                'Malta',
                'Marshall Islands',
                'Mauritania',
                'Mauritius',
                'Mexico',
                'Federated States of Micronesia',
                'Monaco',
                'Mongolia',
                'Montenegro',
                'Morocco',
                'Mozambique',
                'Myanmar',
                'Namibia',
                'Nauru',
                'Nepal',
                'Netherlands',
                'New Zealand',
                'Nicaragua',
                'Niger',
                'Nigeria',
                'North Macedonia',
                'Norway',
                'Oman',
                'Pakistan',
                'Palau',
                'Panama',
                'Papua New Guinea',
                'Paraguay',
                'Peru',
                'Philippines',
                'Poland',
                'Portugal',
                'Qatar',
                'Republic of Korea',
                'Republic of Moldova',
                'Romania',
                'Russian Federation',
                'Rwanda',
                'Samoa',
                'San Marino',
                'Sao Tome and Príncipe',
                'Saudi Arabia',
                'Senegal',
                'Serbia',
                'Seychelles',
                'Sierra Leone',
                'Singapore',
                'Slovakia',
                'Slovenia',
                'Solomon Islands',
                'Somalia',
                'South Africa',
                'South Sudan',
                'Spain',
                'Sri Lanka',
                'St. Kitts and Nevis',
                'St. Lucia',
                'St. Vincent and the Grenadines',
                'Sudan',
                'Suriname',
                'Sweden',
                'Switzerland',
                'Syria',
                'Tajikistan',
                'Tanzania',
                'Thailand',
                'Timor-Leste',
                'Togo',
                'Tonga',
                'Trinidad and Tobago',
                'Tunisia',
                'Turkey',
                'Turkmenistan',
                'Tuvalu',
                'Uganda',
                'Ukraine',
                'United Arab Emirates',
                'United Kingdom',
                'United States of America',
                'Uruguay',
                'Uzbekistan',
                'Vanuatu',
                'Venezuela',
                'Vietnam',
                'Yemen',
                'Zambia',
                'Zimbabwe']
    for country in countries:
        if country.lower() in str.lower():
            return country

def foreign_wiki(nation):
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&format=xml&search=foreign+relations+' + nation.lower() 
    xml = urllib3.PoolManager()
    try:
        data = xml.request('GET', url).data
        soup = BeautifulSoup(data, 'xml')
        return soup.find('Url').get_text() + '\n'
    except:
        return ''

def country_wiki(nation):
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=xml&search=' + nation.lower() 
    xml = urllib3.PoolManager()
    try:
        data = xml.request('GET', url).data
        soup = BeautifulSoup(data, 'xml')
        return soup.find('Url').get_text() + '\n'
    except:
        return ''

def un_news_stories(nation): #das macht nicht
    url = 'https://news.un.org/en/search/' + nation.lower()
    http = urllib3.PoolManager()
    answer = ''
    try:
        data = http.request('GET', url).data
        soup = BeautifulSoup(data, features='lxml')
        for link in soup.find_all('a'):
            if 'story' in str(link.get('href')):
                answer += 'https://news.un.org' + link.get('href') + ' (' + link.get_text().strip() + ')\n'
    except:
        return answer
    return answer 
def sanitize_nation(nation):
    return ('+'.join(nation.split())).lower()

def research(question):
    answer = 'Let us embark on some research together:\n\n'
    answer += give_committee_info(question) + '\n'
    question = componetize(question)
    print(question)
    for country in question['countries']:
        answer += get_country_links(country)
    if question['countries'] is not []:
        answer += 'ultimate background guide: \n'
        answer += 'https://docs.google.com/document/d/1_33AteI8TpO2aypneuyNo0VWxopc801GAOI7Tspy5TE/edit?usp=sharing\n\n'
    answer += get_topic_links(question['topics'])
    return answer

def get_country_links(nation):
    answer = 'about ' + nation + ':\n'
    answer += foreign_wiki(nation)
    answer += country_wiki(nation)
    answer += foreign_ministry(nation)
    answer += '\n' + nation + ' news:\n'
    answer += un_news_stories(nation)
    return answer + '\n'

def foreign_ministry(nation):
    ministries = foreign_ministries.ministries
    for country in ministries:
        p = re.compile('(?<!\w)'+country[1].lower()+'(?!\w)', re.IGNORECASE)
        if re.search(p, nation) is not None:
            return country[0] + '\n'
    return ''
    
def get_topic_links(topic_list):
    answer = ''
    for topic in topic_list:
        answer += '\nnews about '+ topic.lower() + ':\n'
        answer += un_news_stories(topic)
    return answer

def componetize(question):
    components = {
        'countries': [],
        'topics': [],
        'committees': []
    }
    question = ddg.sanitize_phrases(question)
    components['countries'] = find_all_countries(question)
    components['topics'] = find_all_topics(question)
    return components

def find_all_countries(str):
    found_countries = []
    all_countries = countries.countries
    for country in all_countries:
        p = re.compile('(?<!\w)'+country.lower()+'(?!\w)', re.IGNORECASE)
        if re.search(p, str) is not None:
            if country == 'US' or country == 'USA':
                found_countries.append('United States of America')
            elif country == 'UK':
                found_countries.append('United Kingdom')
            else:
                found_countries.append(country)
    return found_countries

def find_all_topics(str):
    all_topics = topics.topics
    found_topics =[]
    for topic in all_topics:
        p = re.compile('(?<!\w)'+topic+'(?!\w)', re.IGNORECASE)
        if re.search(p, str) is not None:
            found_topics.append(topic)
    return sorted(found_topics, reverse=True, key=len)

def research_worse(str):
    print('looking for research request...', end = ' ')
    answer = give_committee_info(str)
    if 'research' not in str.lower():
        print('not found!')
        return answer
    print('found!', end = ' ')
    str = ddg.sanitize_phrases(str)
    country = find_country(str)
    if country is not None:
        answer = 'Thou shalst use the following links to guide thou:\n\n' + answer + '\n'
        country = sanitize_nation(country)
        print('\ncountry:', country)
        answer += 'https://docs.google.com/document/d/1_33AteI8TpO2aypneuyNo0VWxopc801GAOI7Tspy5TE/edit?usp=sharing\n'
        answer += foreign_wiki(country) + '\n' + country_wiki(country)
    else:
        print('no country found!')
    return answer
