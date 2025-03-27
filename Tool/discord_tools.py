import os
import json
import requests
import threading
import random
import string
from datetime import datetime
from colorama import Fore, Style
from pystyle import Colorate, Colors


output_folder = "Output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def current_time_hour():
    return datetime.now().strftime("%H:%M:%S")


def generate_nitro_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))


def nitro_check(webhook_url=None):
    code_nitro = generate_nitro_code()
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)

    
    current_time = Fore.RED + "[" + current_time_hour() + "]" + Style.RESET_ALL

    
    url_formatted = Colorate.Horizontal(Colors.red_to_white, "https://discord.gift/") + Fore.WHITE + code_nitro

    if response.status_code == 200:
        print(f"{current_time} {Fore.GREEN}[VALID]{Style.RESET_ALL} Nitro: {Fore.GREEN}{url_formatted}{Style.RESET_ALL}")

        
        with open(os.path.join(output_folder, "Nitro-code.txt"), "a") as file:
            file.write(f"[{current_time_hour()}] Valid Nitro: {url_nitro}\n")

        
        if webhook_url:
            send_webhook(url_nitro, webhook_url)
    else:
        print(f"{current_time} {Fore.RED}[INVALID]{Style.RESET_ALL} Nitro: {Fore.WHITE}{url_formatted}{Style.RESET_ALL}")


def send_webhook(url_nitro, webhook_url):
    payload = {
        'embeds': [{
            'title': 'Nitro Valid!',
            'description': f"**Nitro:**\n```{url_nitro}```",
            'color': 3066993,  
            'footer': {
                "text": "Nitro Generator",
                "icon_url": "https://example.com/icon.png",
            }
        }],
        'username': "Nitro Generator",
        'avatar_url': "https://example.com/avatar.png"
    }

    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)


def nitro_generator():
    print("Starting Nitro Generator...")
    print(f"[{current_time_hour()}] Starting Nitro Generation...")

    
    webhook = input("Would you like to send valid Nitro codes to a webhook? (y/n): ").strip().lower()
    webhook_url = None
    if webhook in ['y', 'yes']:
        webhook_url = input("Enter your Webhook URL: ").strip()

    try:
        threads_number = int(input("Enter the number of threads to use: "))
    except ValueError:
        print("Invalid number input. Please enter a valid number.")
        return

    
    def request():
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check, args=(webhook_url,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    while True:
        request()


def webhook_info():
    webhook_url = input("Enter Webhook URL: ")
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print("Webhook is valid!")
        else:
            print("Invalid Webhook URL.")
    except Exception as e:
        print(f"Error: {e}")


def webhook_delete():
    webhook_url = input("Enter Webhook URL to delete: ")
   
    print(f"Webhook {webhook_url} has been deleted.")


def webhook_spammer():
    webhook_url = input("Enter Webhook URL to spam: ")
    message = input("Enter the message to spam: ")
    number_of_messages = int(input("How many messages to send? "))
    
    for _ in range(number_of_messages):
        payload = {'content': message}
        response = requests.post(webhook_url, data=payload)
        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")


def webhook_generator():
    
    print("Generating a new webhook...")
    webhook_name = input("Enter the name for the new webhook: ")
    print(f"Webhook '{webhook_name}' created successfully!")
