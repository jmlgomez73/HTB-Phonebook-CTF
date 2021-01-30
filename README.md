# HTB-Phonebook-CTF
Script used in the Capture The Flag (CTF) "Phonebook" challenge of the webside Hack The Box

You can find this challenge in www.hackthebox.eu

The Phonebook challenges will appeas like that:

![Challenge](https://i.ibb.co/VMYx6B4/descarga.png)

When you press "Start" they will provide you an instance ip:port.

![Web](https://i.ibb.co/5Mp7NWC/descarga-1.png)

We will find a vulnerability to exploit, if you enter "*" as username and "*" as password, you can bypass the login, but with this you still won't be able to get the flag.

This script takes advantage of this vulnerability by loading as a payload each character with "*" in each field until access is achieved, decoding the user and password (this will be the flag :) ).

## Requirements
* Linux

* [Python3](https://www.python.org/download/releases/3.0/).

* Libraries: 
    *Requests : ```pip install request```

## Execution

* Valid format: ```python3 HTB_Phonebook_CTF.py ip:port/login```, example of a valid execution : ```python3 HTB_Phonebook_CTF.py http://167.99.88.216:31427/login```

![Demostration](http://g.recordit.co/7VKLSOsXos.gif)
![Result](https://i.ibb.co/QQRXKG1/descarga-1.png)

## Author ✒️

* **Jorge Manuel Lozano Gómez**