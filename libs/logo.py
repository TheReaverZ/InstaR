# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = f"""
{Fore.CYAN}
 ___  _         ___                          ____
|_ _|| |_  ___ | . \ ___  ___  _ _  ___  _ _|_  /
 | | | . |/ ._>|   // ._><_> || | |/ ._>| '_>/ / 
 |_| |_|_|\___.|_\_\\___.<___||__/ \___.|_| /___|
                                                 
 {Fore.RESET}
{Fore.MAGENTA}Team_Member: Aqtic0l, Warhammr, S4IT4M402, 

"""



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "Code by 500 Sec Team"+ Style.RESET_ALL + Style.BRIGHT)
    
