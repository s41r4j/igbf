<h1 align=center> [ igbf ]: Instagram Brute Force (login) </h1>
<h3 align=center> Brute Force Instargam accounts w/ dictionary attack and get the login password! </h3>

![igbf_demo_clear](https://user-images.githubusercontent.com/65067289/235079157-ce36bdd1-b2ea-45a0-86c1-6052db428fd1.png)

<br><br>

## Disclaimer :warning:
- [ igbf ]: is a __proof-of-concept__ & build for __educational purpose__
- You should have __explict__ permission for testing _account security_ from the _owner_ (remember)
- [dev](https://github.com/s41r4j) is not responsible for any illegal use (it is end user's responsibility)

<br>

## Usage :placard:

- ___Installation___

Just clone and start using, no need to install any requirements (but internet connection is essential)

`git clone https://github.com/s41r4j/igbf`   (`cd igbf`)

<br>

- ___Help Menu___

`python3 igbf.py` / `python3 igbf.py -h`

```
usage: igbf.py [-h] [-u USERNAME] [-w WORDLIST]

(s41r4j:igbf)> Instagram Brute Force

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        instagram username
  -w WORDLIST, --wordlist WORDLIST
                        password wordlist
```

<br>

- ___Example___

`python3 igbf.py -u USERNAME -w /PATH/TO/PASSWORD/WORDLIST`

<br>

### Wordlists

Those who are using hacking linux machine (like kali/parrot os, which has pre-installed stuff), can find password wordlist at `/usr/share/wordlists/` (mostly `rockyou.txt, if it is `rockyou.txt.gz` - unzip with `tar -xvzf rockyou.txt.gz`)

Download links (password wordlists):
- [praetorian-inc/Hob0Rules/__wordlists__](https://github.com/praetorian-inc/Hob0Rules/tree/master/wordlist)
- [danielmiessler/__SecLists__/Passwords/Common-Creden](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)

Find more @ [Kaggle](https://www.kaggle.com/search?q=Common+Password+List) (also [this](https://www.kaggle.com/search?q=Password+List))


