import os
import time
from colorama import Fore, Style
from pystyle import Colorate, Colors

def display_credits():
    
    ascii_art = """
     ██████ ██████  ███████ ██████  ██ ████████ ███████ 
    ██      ██   ██ ██      ██   ██ ██    ██    ██      
    ██      ██████  █████   ██   ██ ██    ██    ███████ 
    ██      ██   ██ ██      ██   ██ ██    ██         ██ 
     ██████ ██   ██ ███████ ██████  ██    ██    ███████ 
    """

    
    for line in ascii_art.splitlines():
        print(Fore.RED + line + Style.RESET_ALL)
        time.sleep(0.2)  

    
    credits_text = """
     Development Team  
        - Tropix - Lead Developer 
        - Dodex - Developer  
        - Relly - Junior Developer  

     Support  
        - NexoFast Team - Testing  
        - Glitched - Graphic Design  

    Special thanks to everyone who contributed to the development!
    """
    
    
    for line in credits_text.splitlines():
        
        gradient_credits = Colorate.Vertical(Colors.red_to_black, line)
        print(gradient_credits)
        time.sleep(0.3)  

    input(Fore.WHITE + "\nPress Enter to continue...")

    os.system("cls" if os.name == "nt" else "clear")


