
# Deploy

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/justteen/BUZZ-USERBOT)

# String

[![Run on Repl.it](https://repl.it/badge/github/KeinShin/Black-Lightning&theme=midnight-purple)](https://replit.com/@Paramatin/Lightning-Repl#main.py
)

# The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/justteen/BUZZ-USERBOT.git
cd BUZZ-USERBOT
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m BUZZ-USERBOT
```
# Mandatory Vars
```
[+] Only two of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    
[+] The Lightning Bot will not work without setting the mandatory vars.
```
