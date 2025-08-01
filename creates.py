#!/usr/bin/env python3
#──────────────{ OWNER/ADMIN }──────────────#
#【OWNER/ADMIN : Gul Bahar Pitafi】
#【TOOL TYPE : AUTOMATIC CREATE FACEBOOK】
#【ENJOY SUCCESSFULLY!😅】

"""
Author: Gul Bahar Sajan
Developed by: Gul Bahar Sajan
Facebook: Gul Bahar
WhatsApp: 03093642661
All Color best and dynamic best fancy
Logo: GB auto create tool
Banner: GUL BAHAR PITAFI
"""

import requests
import random
import string
import hashlib
import os
import time
import re
from datetime import datetime
from faker import Faker
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console

class FacebookAccountCreator:
    def __init__(self):
        self.fake = Faker()
        self.console = Console()
        self.api_key = '882a8490361da98702bf97a021ddc14d'
        self.secret = '62f8ce9f74b12f84c123cc23437a4a32'
        self.oks = []
        self.cps = []
        
    def display_banner(self):
        logo = """
   [green1]███████╗██████╗ ██████╗  ██████╗ ██████╗ 
   [spring_green2]██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
   [medium_spring_green]█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
   [cyan2]██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
   [cyan1]███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
   [cyan1]╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    [cyan][bold]VERSION/1.0
          [green_yellow]MY [dark_olive_gre]SYSTEM[pale_green1] IS[dark_sea_green…] DIFFERENT BROTHER
"""
        hari = datetime.now().strftime("%A")
        tanggal = datetime.now().strftime("%d %B %Y")
        info = f"""
  [bold green1]OWNER/ADMIN[medium_purple1]   ➙ [cyan][bold]Gul Bahar Pitafi
  [bold green1]TOOL TYPE[medium_purple1]     ➙ [green][bold]AUTOMATIC CREATE FACEBOOK
  [bold green1]STATUS[medium_purple1]        ➙ [green][bold]PREMIUM
  [bold green1]TODAY DATE[medium_purple1]    ➙ [green][bold]{hari}, {tanggal}
"""
        rprint(Panel(logo, subtitle="[bold red]❏ [bright_yellow]❏ [green1]❏", 
               subtitle_align='left', title="[bold red]❏ [bright_yellow]❏ [green1]❏", 
               title_align='right', width=102, padding=0, style="bold purple"))
        rprint(Panel(info, width=100, padding=0, style="bold purple"))

    def generate_random_string(self, length=32):
        """Generate a random alphanumeric string of given length"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_facebook_signature(self, params):
        """Generate Facebook API signature"""
        sorted_params = sorted(params.items(), key=lambda x: x[0])
        sig = ''.join(f'{k}={v}' for k, v in sorted_params)
        return hashlib.md5((sig + self.secret).encode()).hexdigest()

    def register_facebook_account(self, email, password, first_name, last_name, birthday):
        """Register a new Facebook account"""
        gender = random.choice(['M', 'F'])
        
        params = {
            'api_key': self.api_key,
            'attempt_login': True,
            'birthday': birthday.strftime('%Y-%m-%d'),
            'client_country_code': 'US',
            'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
            'fb_api_req_friendly_name': 'registerAccount',
            'firstname': first_name,
            'format': 'json',
            'gender': gender,
            'lastname': last_name,
            'email': email,
            'locale': 'en_US',
            'method': 'user.register',
            'password': password,
            'reg_instance': self.generate_random_string(32),
            'return_multiple_errors': True
        }
        
        params['sig'] = self.generate_facebook_signature(params)
        api_url = 'https://b-api.facebook.com/method/user.register'
        headers = {'User-Agent': self.generate_user_agent()}
        
        try:
            response = requests.post(api_url, data=params, headers=headers)
            result = response.json()
            
            if 'new_user_id' in result:
                user_id = result['new_user_id']
                token = result['session_info']['access_token']
                self.save_account_details(email, password, first_name, last_name, birthday, gender, user_id, token)
                self.display_success(email, password, first_name, last_name, birthday, gender, user_id, token)
                self.oks.append(user_id)
                return True
            self.cps.append("Failed")
            return False
        except Exception as e:
            self.cps.append("Error")
            return False

    def generate_user_agent(self):
        """Generate random user agent"""
        fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
        fbbv = str(random.randint(111111111, 999999999))
        device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
        carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
        return f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;FBRV/0;FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

    def save_account_details(self, email, password, first_name, last_name, birthday, gender, user_id, token):
        """Save account details to a file"""
        with open('accounts.txt', 'a') as f:
            f.write(f"""
Email: {email}
Password: {password}
Name: {first_name} {last_name}
Birthday: {birthday}
Gender: {gender}
User ID: {user_id}
Access Token: {token}
{"="*40}
""")

    def display_success(self, email, password, first_name, last_name, birthday, gender, user_id, token):
        """Display successful account creation"""
        success_msg = f'''
\x1b[38;5;22m⋘▬▭▬▭▬▭▬﴾𓆩GB IDS TOOL  SUCCESS 𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ EMAIL: {email}
﴾𝐕𝐈𝐏﴿ ID: {user_id}
﴾𝐕𝐈𝐏﴿ PASSWORD: {password}
﴾𝐕𝐈𝐏﴿ NAME: {first_name} {last_name}
﴾𝐕𝐈𝐏﴿ BIRTHDAY: {birthday} 
﴾𝐕𝐈𝐏﴿ GENDER: {gender}
⋘▬▭▬▭▬▭▬﴾𓆩 GB IDS TOOL TOKEN 𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ {token}
⋘▬▭▬▭▬▭▬﴾𓆩GB IDS TOOL DONE 𓆪﴿▬▭▬▭▬▭▬⋙
'''
        rprint(Panel(success_msg, style="bold green"))

    def show_menu(self):
        """Display main menu"""
        menu = Panel("""    [green_yellow][[bold cyan1]1[green_yellow]][bold green] AUTO CREATE FACEBOOK
    [green_yellow][[bold cyan1]2[green_yellow]][bold green] CONTACT OWNER
    [green_yellow][[bold cyan1]3[green_yellow]][bold red] EXIT TOOL""", 
        title="[reverse purple] TOOL MENU", style="bold purple")
        rprint(Panel(menu, subtitle="[bold purple]┌─", subtitle_align='left', style="bold purple"))
        return self.console.input("   [bold purple]└──> ")

    def get_account_details(self):
        """Get account creation parameters from user"""
        self.display_banner()
        num_accounts = int(self.console.input("[+] How Many Accounts You Want to Create: "))
        delay = int(self.console.input("[+] Enter Delay Between Creations (seconds): "))
        
        # Generate fake details
        accounts = []
        for _ in range(num_accounts):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            email = f"{first_name.lower()}{last_name.lower()}{random.randint(100,999)}@gmail.com"
            password = f"{first_name}{last_name}{random.randint(1000,9999)}"
            birthday = self.fake.date_of_birth(minimum_age=18, maximum_age=45)
            accounts.append((email, password, first_name, last_name, birthday))
        
        return accounts, delay

    def run_creation(self, accounts, delay):
        """Run the account creation process"""
        for idx, (email, password, first_name, last_name, birthday) in enumerate(accounts, 1):
            self.display_banner()
            rprint(Panel(f"[bold white] Creating Account {idx}/{len(accounts)}", style="bold purple"))
            time.sleep(1)
            
            if self.register_facebook_account(email, password, first_name, last_name, birthday):
                time.sleep(delay)
            else:
                time.sleep(2)
                
        self.show_results()

    def show_results(self):
        """Display final results"""
        results = Panel(f"""
[bold white] FINAL RESULTS
[bold green] SUCCESS : {len(self.oks)}
[bold red] FAILED  : {len(self.cps)}
[bold white] Results are saved to accounts.txt
""", style="bold purple")
        rprint(results)
        time.sleep(3)

    def main(self):
        """Main program flow"""
        while True:
            self.display_banner()
            choice = self.show_menu()
            
            if choice in ["1", "01"]:
                accounts, delay = self.get_account_details()
                self.run_creation(accounts, delay)
            elif choice in ["2", "02"]:
                self.console.print("[bold green]Contacting owner...", style="bold purple")
                time.sleep(2)
            elif choice in ["3", "03"]:
                self.console.print("[bold red]Exiting tool...", style="bold purple")
                break
            else:
                self.console.print("[bold yellow]Invalid choice, please try again", style="bold purple")
                time.sleep(1)

if __name__ == "__main__":
    try:
        creator = FacebookAccountCreator()
        creator.main()
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user")
    except Exception as e:
        print(f"[!] An error occurred: {str(e)}")