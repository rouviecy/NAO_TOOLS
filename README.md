NAO_TOOLS
=========

Some tools in order to play with NAO robots


Client-server
-------------

1. On server (computer) :
    * Plug your joystick (if you have any)
    * `python Infos_commandes.py` to grab keys for remote control
    * Enter yours keys in `Configuration.py`
    * Choose a port PPPP (for example : 4242)  
    * Identify your IP_SERVER
    * `python main_serveur.py PPPP`  

2. On clients (NAOs) :
    * Enter in SSH
    * `python main_client.py IP_SERVER PPPP`

3. Control chain :  
    * `GUI.py` Listeners on keyboard and joystick
    * `Interface_serveur.py` Sender from computer to NAOs
    * `Interface_client.py` Receivers on NAOs from computer
    * `Actionneur.py` Actions you can perform
    * `Mouvements.py` Interface between the program and NAO hardware