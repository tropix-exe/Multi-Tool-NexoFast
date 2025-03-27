import os
import sys
from colorama import Fore, Style, init
from pystyle import Center, Colorate, Colors


init(autoreset=True)


sys.path.append(os.path.join(os.getcwd(), "Tool"))


def MainColor(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


from Tool import discord_tools
from Tool import ip_pinger
from Tool.ip_info import get_ip_info
from Tool import ip_port_scanner
from Tool.all_credits import display_credits


os.system("title NexoFast Multi Tool")

def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    ascii_art = """
                             ███▄    █ ▓█████ ▒██   ██▒ ▒█████    █████▒▄▄▄        ██████ ▄▄▄█████▓
                             ██ ▀█   █ ▓█   ▀ ▒▒ █ █ ▒░▒██▒  ██▒▓██   ▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒
                            ▓██  ▀█ ██▒▒███   ░░  █   ░▒██░  ██▒▒████ ░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░
                            ▓██▒  ▐▌██▒▒▓█  ▄  ░ █ █ ▒ ▒██   ██░░▓█▒  ░░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ 
                            ▒██░   ▓██░░▒████▒▒██▒ ▒██▒░ ████▓▒░░▒█░    ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ 
                            ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒ ░ ░▓ ░░ ▒░▒░▒░  ▒ ░    ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   
                            ░ ░░   ░ ▒░ ░ ░  ░░░   ░▒ ░  ░ ▒ ▒░  ░       ▒   ▒▒ ░░ ░▒  ░ ░    ░    
                              ░   ░ ░    ░    ░    ░  ░ ░ ░ ▒   ░ ░     ░   ▒   ░  ░  ░    ░      
                                   ░    ░  ░ ░    ░      ░ ░               ░  ░      ░
                        [0] Exit                                                            [C] Credits
        
        [1] Discord Nitro Generator    |      [6] IP Info
        [2] Discord Webhook Info       |      [7] IP Port Scanner
        [3] Discord Webhook Delete     |      [8] IP Pinger
        [4] Discord Webhook Spammer    |     
        [5] Discord Webhook Generator  |         
                                       |        
    """
    gradient_colors = Colorate.Vertical(Colors.red_to_yellow, ascii_art)
    print(gradient_colors)

def main():
    while True:
        show_menu()
        choice = input(MainColor("user@nexofast [~] $ ")).strip().upper()

        if choice == "1":
            discord_tools.nitro_generator()
        elif choice == "2":
            discord_tools.webhook_info()
        elif choice == "3":
            discord_tools.webhook_delete()
        elif choice == "4":
            discord_tools.webhook_spammer()
        elif choice == "5":
            discord_tools.webhook_generator()
        elif choice == "6":
            ip = input(MainColor("[?] Enter IP address: "))
            get_ip_info(ip)
        elif choice == "7":
            ip_port_scanner.scan()
        elif choice == "8":
            ip_pinger.ping()
        elif choice == "C":
            display_credits()
        elif choice == "0":
            print(MainColor("[!] Exiting..."))
            break
        else:
            print(MainColor("[!] Invalid choice!"))
        
        input(MainColor("\n[Press Enter to continue..."))
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()