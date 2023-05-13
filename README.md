<h1 align=center> [ igbf ]: Instagram Brute Forcer </h1>
<h3 align=center> Brute Force Instargam account logins w/ dictionary attack! </h3>

![igbf_demo_clear](https://user-images.githubusercontent.com/65067289/235207665-62c45b02-223f-4bb3-8304-d8736d8b36ea.png)

<br><br>

## Disclaimer :warning:
- [ igbf ]: is a __proof-of-concept__ & build for __educational purpose__
- You should have __explict__ permission for testing _account security_ from the _owner_ (remember _“With great power comes great responsibility”_)
- [developer](https://github.com/s41r4j) is not responsible for any illegal use (it is end user's responsibility)

<br>

## Usage :placard:

- ___Installation___

Just clone and start using, no need to install any requirements (but internet connection is essential)

`git clone https://github.com/s41r4j/igbf`   (`cd igbf`)

<br>

- ___Help Menu___

`python3 igbf.py` / `python3 igbf.py -h`

```
usage: igbf.py [-h] [-u USERNAME] [-w WORDLIST PATH] [-t TIMEOUT] [-v] [-p] [-pl PROXY_LIMIT]

(s41r4j:igbf)> Instagram Brute Force

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        instagram username (*required)
  -w WORDLIST PATH, --wordlist WORDLIST PATH
                        password wordlist (*required)
  -t TIMEOUT, --timeout TIMEOUT
                        timeout between each request in secs (default: 2)
  -v, --verbose         verbose mode (displays failed logins and more)
  -p, --proxy           use ip rotating proxy (additinal library required)
  -pl PROXY_LIMIT, --proxy-limit PROXY_LIMIT
                        limit the number of proxies to use (default: 300; max: 300; min: 1)

```

<br>

- ___Example___

`python3 igbf.py -u USERNAME -w /PATH/TO/PASSWORD/WORDLIST`

<br>

### Wordlists :page_with_curl:

Those who are using hacking linux machine (like kali/parrot os, which has pre-installed stuff), can find password wordlist at `/usr/share/wordlists/` (mostly `rockyou.txt`, if it is `rockyou.txt.gz` - unzip with `tar -xvzf rockyou.txt.gz`)

Download links (password wordlists):
- [praetorian-inc/Hob0Rules/__wordlists__](https://github.com/praetorian-inc/Hob0Rules/tree/master/wordlist)
- [danielmiessler/__SecLists__/Passwords/Common-Creden](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)

Find more @ [Kaggle](https://www.kaggle.com/search?q=Common+Password+List) (also [this](https://www.kaggle.com/search?q=Password+List))


<br>

### Note :bookmark_tabs:
- It only supports single username (currently) & a wordlist file.
- I tried to integrate proxy ip rotating for every request, but currently it's not working
- __Language__: Python3; __OS__: Win, Mac, Unix/Linux (also Termux ig)
- If you have any quries/issues/errors, open an issue [here](https://github.com/s41r4j/igbf/issues)

