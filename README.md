<h1 align=center> [ igbf ]: Instagram Brute Forcer </h1>
<h3 align=center> Brute Force Instargam account logins w/ dictionary attack! </h3>


<!-- <p align="center">
    <a href="#" alt="version">
        <img src="https://img.shields.io/badge/dynamic/json?color=blue&label=version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fs41r4j%2Figbf%2Fmain%2F.media%2Fmaintainer.json" /></a>
    <a href="#" alt="language">
        <img src="https://img.shields.io/badge/dynamic/json?color=blue&label=language&query=%24.language&url=https%3A%2F%2Fraw.githubusercontent.com%2Fs41r4j%2Figbf%2Fmain%2F.media%2Fmaintainer.json" /></a>
  <a href="https://github.com/s41r4j/igbf/releases" alt="latest release">
        <img src="https://img.shields.io/badge/dynamic/json?color=success&label=latest release&query=%24.release&url=https%3A%2F%2Fraw.githubusercontent.com%2Fs41r4j%2Figbf%2Fmain%2F.media%2Fmaintainer.json" /></a>
    <a href="#" alt="Stars">
        <img src="https://img.shields.io/github/stars/s41r4j/igbf.svg" /></a>
    <a href="https://github.com/s41r4j/igbf" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/s41r4j/igbf" /></a>
    <a href="https://twitter.com/intent/follow?screen_name=s41r4j">
        <img src="https://img.shields.io/twitter/follow/s41r4j?style=social&logo=twitter"
            alt="follow on Twitter"></a>
</p> -->


![igbf demo](./.media/igbf_demo_compress.gif)



<br><br>

## Disclaimer :warning:
- This [project](https://github.com/s41r4j/igbf/) is only a __proof-of-concept__ & build for __educational purpose__
- You should have __explict__ permission for testing _account security_ from the _owner_ 
- [developer](https://github.com/s41r4j) is not responsible for any illegal use, it is end user's responsibility
>  _“With great power comes great responsibility”_

<br>

## Usage :placard:

- ___Installation___

    - Just clone and start using, no need of installing any requirements.
    - Internet connection is essential
    - To use proxy, a library (`pip install beautifulsoup4`) is required; The program installs it for you while running (if not present)
    - Also you can get the latest version from [releases](https://github.com/s41r4j/igbf/releases)
    

```bash
git clone https://github.com/s41r4j/igbf
cd igbf
```

<br>

- ___Help Menu___

```bash
python3 igbf.py
```

``` bash
usage: igbf.py [-h] [-u USERNAME] [-w WORDLIST PATH] [-t TIMEOUT] [-v] [-p] [-l PROXY_LIMIT]

(s41r4j:igbf)> Instagram Brute Forcer

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
  -l PROXY_LIMIT, --proxy-limit PROXY_LIMIT
                        limit the number of proxies to use (default: 300; max: 300; min: 1)

```

<br>

- ___Example___

```bash
python3 igbf.py -u USERNAME -w /PATH/TO/PASSWORD/WORDLIST -v
```

<br>

### Wordlists :page_with_curl:

Those who are using linux/hacking machines (like kali/parrot os, which has pre-installed stuff), can find password wordlist at `/usr/share/wordlists/` (mostly `rockyou.txt`, if it is `rockyou.txt.gz` - unzip with `tar -xvzf rockyou.txt.gz`)

Download links for password wordlists:
- [praetorian-inc/Hob0Rules/__wordlists__](https://github.com/praetorian-inc/Hob0Rules/tree/master/wordlist)
- [danielmiessler/__SecLists__/Passwords/Common-Creden](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)

Find more @[Kaggle](https://www.kaggle.com/search?q=Common+Password+List) & @[Github](https://github.com/search?q=passwords%20wordlists&type=repositories)


<br>

### Note :bookmark_tabs:
    - It only supports single username (currently) & a wordlist file
    - I tried to integrate proxy ip rotating for every request, but there are some issues at the moment
    - If you're not using proxy, instagram blocks/bans your ip (temporarily, dw) after 7-8 attempts
    - Supports: Windows, Mac, Unix/Linux (Termux)
    
- If you have any quries/issues/errors, open an issue [here](https://github.com/s41r4j/igbf/issues)
- I'm open to all contributions, clone and do a pull request



<!-- ![starchart](https://starchart.cc/s41r4j/igbf.svg) -->

