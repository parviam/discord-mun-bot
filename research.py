def research(str):
    print('looking for research request...')
    answer = give_committee_info(str)
    if 'research' not in str.lower() and 'info' not in str.lower():
        print('not found!')
        return answer
    print('found!')
    answer += '\nThou forebearers hath created a great research document, to best all other guides: '
    answer += '\nhttps://docs.google.com/document/d/1_33AteI8TpO2aypneuyNo0VWxopc801GAOI7Tspy5TE/edit?usp=sharing'
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
        ans += 'https://www.un.org/en/ga/third/index.shtml'
    if 'ga4' in str.lower():
        ans += 'GA4 deals with special decolonization, polticial issues, and outer space, and some other issues: '
        ans += '\nhttps://www.un.org/en/ga/fourth/index.shtml'
    if 'ga5' in str.lower():
        ans += 'GA5 deals with the administration and budget of other UN bodies: '
        ans += '\nhttps://www.un.org/en/ga/fifth/index.shtml'
    if 'ga6' in str.lower():
        ans += 'GA6 deals with legal questions: '
        ans += 'https://www.un.org/en/ga/sixth/index.shtml'
    if 'security council' in str.lower() or 'unsc' in str.lower():
        ans += 'The Security Council has primary responsibility for global peace and security. They may place sanctions and deploy peacekeepers: '
        ans += '\nhttps://www.un.org/securitycouncil/'
        ans += '\nSC containth altered rules and reg\'tions. Feast your eyes upon this resource: '
        ans += '\nhttps://bestdelegate.com/five-tips-on-how-to-succeed-in-the-security-council/'
    if 'iaea' in str.lower() or 'international atomi' in str.lower():
        ans += 'The IAEA promotes the safe use of atomic energy and nuclear non-proliferation: '
        ans += '\nhttps://www.iaea.org/about/overview/history'
    return ans
