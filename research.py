import urllib3
from bs4 import BeautifulSoup
import re
import ddg

def research(str):
    print('looking for research request...', end = ' ')
    answer = give_committee_info(str)
    if 'research' not in str.lower():
        print('not found!')
        return answer
    print('found!', end = ' ')
    str = ddg.clean_question(str)
    country = find_country(str)
    if country is not None:
        answer = 'Thou shalst use the following links to guide thou:\n\n' + answer
        country = sanitize_nation(country)
        print('\ncountry:', country)
        answer += 'https://docs.google.com/document/d/1_33AteI8TpO2aypneuyNo0VWxopc801GAOI7Tspy5TE/edit?usp=sharing\n'
        answer += foreign_wiki(country) + '\n' + country_wiki(country)
    else:
        print('no country found!')
    return answer

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
        return soup.find('Url').get_text()
    except:
        return ''


def country_wiki(nation):
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=xml&search=' + nation.lower() 
    xml = urllib3.PoolManager()
    try:
        data = xml.request('GET', url).data
        soup = BeautifulSoup(data, 'xml')
        return soup.find('Url').get_text()
    except:
        return ''

def un_news_stories(nation): #das macht nicht
    url = 'https://www.unmultimedia.org/avlibrary/search/search.jsp?mediatype=&sort=cdate_desc&q=' + nation.lower()
    http = urllib3.PoolManager()
    print(url)
    try:
        data = http.request('GET', url).data
        soup = BeautifulSoup(data)
        for link in soup.find_all('a'):
            print(link.get('href'))
            #if '/en/story' in link.get('href'):
             #   print(link.get('href'))
    except:
        return ''
    soup = BeautifulSoup(data, 'xml')
    return soup.find('Url').get_text()

def sanitize_nation(nation):
    return ('+'.join(nation.split())).lower()


#print(un_news_stories('france'))