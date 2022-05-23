#Streamlab-Chatbot-Python-MoreCommandAndAction
Streamlab chatbot script. This script add additional command and action for viewers 

##### ================ Script Information =====================
- ScriptName:   MC&A
- Website:      https://twitch.tv/stachopl
- Description:  Now your viewers has new interaction and commands
- Creator:      StachoPL
- Version:      1.0.0.1

##### ================= Script Instalation ======================

 To use this addon you must have installed python 2.7 and Streamlab Chatbot
 
 Link to python: https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi

- Download release script from github
- Open Streamlab Chatbot
- Go to scripts tab
- On right site click ``Import``
- Now select ZIP file what you get from Release  

##### ================= Command list ======================

- followage - User can check how long time follow your channel
- game - users can check stream category(game, etc)
- upstream - user can check how long you stream
- gamble - Mini game, user can win or loss points
- throw - Mini game, user can throw point to another user


##### ================= Command Config ======================

_All cammand has similar config. First you have MA&A Core. There you mast
put the currency name and select language(English or Polish)._ 

_Next other command has fields like Command active, Command, Permission, Info, Cooldown, response_

- _Command active - Field for define command active_
- _Command - Field for define whats user must write to run command_
- _Permission - Field for define who can use command_
- _Info - Field for feature function (unused)_
- _Cooldown - Field for define how long time must past to use again time this command_
- _Response - Field for define command response._

_All command has special variables._

1. Followage:
    - $username - Display user name
    - $followage - Time how long time is following
2. Game:
    - $game - Display current game
3. Upstream:
    - $uptime - display uptime your stream
4. Gamble:
    - $username - display user name
    - $amount - display how many user win or loss
    - $currency_name - display currency name(this name is set in MA&A Core)
5. Throw:
    - $username - display target user name
    - $amount - display how many user win or loss
    - $currency_name - display currency name(this name is set in MA&A Core) 
    
##### ================= Bug report ======================
If you find any bugs or you have some suggestion use github issus page or
join to my discord: https://discord.com/invite/4aY9yKxTut