# GuitarPro-RPC

GuitarPro RPC is a python script that uses the pypresence library to put a status whenever you are editing your favorite tabs on Guitar Pro.


This script was only tested with the **version 5** of the software, and I do not have any idea on how this would eventually work on newer versions. 

## Installation 

First of all, you will need to get the inital configuration done, assuming that you have got python and pip installed.

- Get all the packages needed trough the ```pip install -r requirements.txt```
- Create an app in Discord's developper portal and make sure that
    - The name is corresponding to your Guitar Pro version.
    - You upload the ```guitarpro.png``` image into the Rich Presence > Art Assets tab.
    - Copy the APPLICATION ID from the General Information tab.
- Configure the app by specifying your discord app client ID you just copied, the Guitar Pro version and the name of the main executable in the ```.env``` file.
- Put the ```main.py``` and ```.env``` files in the root of your installation.

## Usage

Simply run the ```main.py``` file instead of the normal executable.