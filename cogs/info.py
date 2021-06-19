import discord 
import logging
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import time
import asyncio
from discord.ext.commands.core import check
import gspread
from datetime import date, datetime
from datetime import timedelta
from discord import Intents
import psycopg2
from psycopg2 import OperationalError
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component

# Necessary Variables

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("redacted",
"redacted",
"redacted",
"redacted",
"redacted")

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return cursor

gc = gspread.service_account(filename = "redacted")
wks = gc.open_by_key("redacted")
worksheet = wks.sheet1

sgrep = int(worksheet.acell("E36").value)
slrep = int(worksheet.acell("E37").value)
mprep = int(worksheet.acell("E35").value)
cicrep = int(worksheet.acell("E34").value)

if int(sgrep) <= 340:
    sgrep = "Hated"
elif 341 <= int(sgrep) <= 444:
    sgrep = "Disliked"
elif 445 <= int(sgrep) <= 650:
    sgrep = "Mixed"
elif 651 <= int(sgrep) <= 850:
    sgrep = "Neutral"
elif 851 <= int(sgrep) <= 1184:
    sgrep = "Favoured"
else:
    sgrep = "Loved"

if int(slrep) <= 340:
    slrep = "Hated"
elif 341 <= int(slrep) <= 444:
    slrep = "Disliked"
elif 445 <= int(slrep) <= 650:
    slrep = "Mixed"
elif 651 <= int(slrep) <= 850:
    slrep = "Neutral"
elif 851 <= int(slrep) <= 1184:
    slrep = "Favoured"
else:
    slrep = "Loved"

if int(mprep) <= 340:
    mprep = "Hated"
elif 341 <= int(mprep) <= 444:
    mprep = "Disliked"
elif 445 <= int(mprep) <= 650:
    mprep = "Mixed"
elif 651 <= int(mprep) <= 850:
    mprep = "Neutral"
elif 851 <= int(mprep) <= 1184:
    mprep = "Favoured"
else:
    mprep = "Loved"

if int(cicrep) <= 340:
    cicrep = "Hated"
elif 341 <= int(cicrep) <= 444:
    cicrep = "Disliked"
elif 445 <= int(cicrep) <= 650:
    cicrep = "Mixed"
elif 651 <= int(cicrep) <= 850:
    cicrep = "Neutral"
elif 851 <= int(cicrep) <= 1184:
    cicrep = "Favoured"
else:
    cicrep = "Loved"

class Commanders:

    def __init__(self,sgc="",slc="",mpc="",cic="",hti=""):
        self.sgc = sgc
        self.slc = slc
        self.mpc = mpc
        self.cic = cic
        self.hti = hti

    def getinfo(self,sgc="",slc="",mpc="",cic="",hti=""):

        self.sgc = ""
        self.slc = ""
        self.mpc = ""
        self.cic = ""
        self.hti = ""
    
        selectCMDs = """
        SELECT * from commanders
        """
        cmds = execute_query(connection,selectCMDs)

        cmdlist = []

        for c in cmds:
            cmdlist.append(c)

        for c in cmdlist:
            if c[0] == "SG":
                self.sgc = c[1]
            elif c[0] == "SL":
                self.slc = c[1]
            elif c[0] == "MP":
                self.mpc = c[1]
            elif c[0] == "CiC":
                self.cic = c[1]
            elif c[0] == "HTI":
                self.hti = c[1]


commanders = Commanders()
commanders.getinfo()

whitelist = [channel ids]

defaultcolor = 0x352852




# Actual Commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self,ctx, arg=None):
        if arg != None:
            arg = arg.lower()

        author = ctx.message.author

        
        if ctx.message.channel.id in whitelist or ctx.message.channel.id == redacted or ctx.message.channel.id == redacted:
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return


        if arg == None:
            embed=discord.Embed(title="Info Command", description="Use these to learn more about AoT:U (ex. `.info trainee`)", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="`.info getstarted`", value="Information on getting started in AoT:U", inline=False)
            embed.add_field(name="`.info getpd`", value="Information on how to get a PD hosted", inline=False)
            embed.add_field(name="`.info rules`", value="A link to our rulesets", inline=False)
            embed.add_field(name="`.info economy`", value="Get started in AoT:U's economy", inline=False)
            embed.add_field(name="`.info wall`", value="Talk directly to the Game Owner", inline=False)
            embed.add_field(name="`.info sg`", value="Learn more about the Stationary Guard", inline=False)
            embed.add_field(name="`.info sl`", value="Learn more about the Scouting Legion", inline=False)
            embed.add_field(name="`.info mp`", value="Learn more about the Military Police", inline=False)
            embed.set_footer(text="Bot made by Marzooq ")
            await author.send(embed=embed)
            if isinstance(ctx.channel, discord.channel.DMChannel):
                pass
            else:
                messagesent=discord.Embed(color=defaultcolor)
                messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
                msg = await ctx.send(embed=messagesent)
                await msg.delete(delay=5.0)
        elif arg == "getstarted" or arg == "tc":
            embed=discord.Embed(title="Info | Getting Started", description="Join the links below to get started in AoT:U", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="AoT:U Main Roblox group", value="https://www.roblox.com/groups/1214373/Attack-on-Titan-Universe#!/about", inline=False)
            embed.add_field(name="Trainee Camp Roblox group", value="https://www.roblox.com/groups/4758464/AoT-U-Trainee-Corps#!/about", inline=False)
            embed.add_field(name="Trainee Camp Discord server", value="https://discord.gg/5UBdyRbjFX", inline=False)
            embed.set_footer(text="Bot made by Marzooq ")
            await ctx.send(embed=embed)
        elif arg == "getpd":
            embed=discord.Embed(title="Info | Getting a PD", description="Follow the instructions below on getting a PD", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Ticket command", value="Use `.ticket` to open a ticket to get a PD.", inline=False)
            embed.add_field(name="More About PDs", value="https://aotuniverse.net/guidelines/about-pd/", inline=False)
            embed.set_footer(text="Bot made by Marzooq ")
            await ctx.send(embed=embed)
        elif arg == "rules":
            embed=discord.Embed(title="Info | Rules", description="Below is a link to different versions of the rules", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Simplified Ruleset ", value="https://aotuniverse.net/guidelines/simplified-rules/", inline=False)
            embed.add_field(name="Binding Ruleset", value="https://aotuniverse.net/guidelines/binding-ruleset/", inline=False)
            embed.set_footer(text="Bot made by Marzooq ")
            await ctx.send(embed=embed)
        elif arg == "economy":
            embed=discord.Embed(title="Info | Economy", description="Join the Lore Econ server and learn more about how to navigate AoT:U's economy system.", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Lore Economy Discord Server", value="https://discord.gg/kE3TkBn ", inline=False)
            embed.add_field(name="Basic Economy Info", value="https://docs.google.com/document/d/1qcY1mvYz4CLlKa1cdHrXT86mbRH2u-oG7TuFvdoScRU/edit?usp=sharing", inline=False)
            embed.add_field(name="Treasury Info", value="https://docs.google.com/document/d/1Ocoq1-jazHuq6IJv4La8ZkhhkUbjGI0m9RVb94zeAXY/edit?usp=sharing", inline=False)
            embed.set_footer(text="Bot made by Marzooq ")
            await ctx.send(embed=embed)
        elif arg == "wall":
            embed=discord.Embed(title="Info | Wall", description="Talk directly to Wall, the game owner, and more on his job", color=defaultcolor)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/747522043658109053/762415207670087691/unknown.png")
            embed.add_field(name="Inbox Discord Server", value="https://discord.gg/JWTWUH6", inline=False)
            embed.add_field(name="Role for AoT:U", value="Wall scripts for the game and also helps deal with the top-level cases in AoT:U. He directs the staff team and also deals with the most important matters regarding scripting, the website, and the game.", inline=False)
            embed.add_field(name="College", value="Wall is currently away at college and can only get involved every so often. Refer to the server above to talk with him about **important** matters that only he can deal with.", inline=False)
            embed.set_footer(text="bot made by marzooq")
            await ctx.send(embed=embed)
        elif arg == "sg" or arg == "stationary guard":
            embed=discord.Embed(title="Info | Stationary Guard ", description="The Stationary Guard deals with defending the walls and maintaining them.", color = 0x7a1f1d)
            embed.set_thumbnail(url="https://t3.rbxcdn.com/cac2eb784b0ec47b69759a20ae7a4af0")
            embed.add_field(name="Commander", value=commanders.sgc)
            embed.add_field(name="How to Join", value="In order to graduate into the Stationary Guard, you must graduate TC. The Stationary Guard usually accepts those with the minimum passing requirement. This is usually 60-70.", inline=False)
            embed.add_field(name="Reputation", value=sgrep)
            embed.set_footer(text="made by marzooq :)")
            await ctx.send(embed=embed)
        elif arg == "ti" or arg == "trainee instructor":
            embed=discord.Embed(title="Info | Trainee Instructors", description="The Trainee Instructors teach and vet cadets up until they join a branch.", color = 0x493c38)
            embed.set_thumbnail(url="https://t6.rbxcdn.com/1113899ea987fea0e47b7b574e7374f0")
            embed.add_field(name="Head Trainee Instructor", value=commanders.hti)
            embed.add_field(name="How to Join", value="In order to graduate into the Trainee Instructors, you must graduate TC. The Head Instructor usually accepts those with the high written scores. This is usually 50+ on the written and an overall passing score.", inline=False)
            embed.set_footer(text="made by marzooq :)")
            await ctx.send(embed=embed)
        elif arg == "sl" or arg == "scouting legion":
            embed=discord.Embed(title="Info | Scouting Legion", description="The Scouting Legion goes beyond the walls and discovers the secrets of the world.", color=0x282c52)
            embed.set_thumbnail(url="https://t3.rbxcdn.com/403d75a1c5c806d740a05e537cfe1cef")
            embed.add_field(name="Commander", value=commanders.slc)
            embed.add_field(name="How to Join", value="In order to join the Scouting Legion, you need to graduate from TC. Usually, the minimum points needed for SL is 85.", inline=False)
            embed.add_field(name="Reputation", value=slrep)
            embed.set_footer(text="made by marzooq :)")
            await ctx.send(embed=embed)
        elif arg == "mp" or arg == "military police":
            embed=discord.Embed(title="Info | Military Police", description="The Military Police fights crime within the walls and ensures peace among the people.", color=0x306c4c)
            embed.set_thumbnail(url="https://t0.rbxcdn.com/417f84cfe9a0d912b2fec4d4eb07c61a")
            embed.add_field(name="Commander", value=commanders.mpc)
            embed.add_field(name="How to Join", value="In order to join the Military Police, you need to graduate from TC as a top cadet.", inline=False)
            embed.add_field(name="Reputation", value=mprep)
            embed.set_footer(text="made by marzooq :)")
            await ctx.send(embed=embed)
        elif arg == "cic":
            embed=discord.Embed(title="Info | Commander-in-Chief", description="The CiC is in charge of leading all the branches, ensuring the civil cooperation of the military's forces.", color=0xdde63e)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/800431515024490506/850762408976580656/latest.png")
            embed.add_field(name="CiC", value=commanders.cic,inline=False)
            embed.add_field(name="Reputation",value=cicrep,inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: Option not recognised. Use `.info` to see all options.", inline=False)
            await ctx.send(embed=embed)


    @commands.command()
    async def setcommander(self,ctx):

        author = ctx.message.author
        marzooq = await self.bot.fetch_user(redacted)

        if author == marzooq or author.guild_permissions.administrator:
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: Missing Permissions: Cannot use command", inline=False)
            await ctx.send(embed=embed)   
            return

        embed=discord.Embed(title="AoT:U | Set Commander", description="Select which commander to set:",color=defaultcolor)
        msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.grey,label="SG"), Button(style=ButtonStyle.grey,label="SL"), Button(style=ButtonStyle.grey,label="MP")],[Button(style=ButtonStyle.grey,label="CiC"), Button(style=ButtonStyle.grey,label="HTI"), Button(style=ButtonStyle.red,label="Exit")]])

        res = await self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)

        if res.component.label == "SG":
            embed=discord.Embed(title="AoT:U | Set Commander", description="Send the new SGC's username below:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.red,label="Exit")]])

            done, pending = await asyncio.wait([
                self.bot.wait_for("message", check= lambda message: message.author == author),
                self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)
            ], return_when=asyncio.FIRST_COMPLETED)

            done = done.pop().result()

            for task in pending:
                task.cancel()

            if isinstance(done, discord.Message):
                newsgc = done.content
                await done.delete()
                await ctx.send("SGC updated.")
                await msg.delete()
            else:
                await msg.delete()
                return

            setSGC = f"""
            UPDATE commanders
            SET name = '{newsgc}'
            WHERE branch = 'SG'
            """
            execute_query(connection,setSGC)

            commanders.getinfo()

        elif res.component.label == "SL":
            embed=discord.Embed(title="AoT:U | Set Commander", description="Send the new SLC's username below:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.red,label="Exit")]])

            done, pending = await asyncio.wait([
                self.bot.wait_for("message", check= lambda message: message.author == author),
                self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)
            ], return_when=asyncio.FIRST_COMPLETED)

            done = done.pop().result()

            for task in pending:
                task.cancel()

            if isinstance(done, discord.Message):
                newslc = done.content
                await done.delete()
                await ctx.send("SLC updated")
                await msg.delete()
            else:
                await msg.delete()
                return

            setSGC = f"""
            UPDATE commanders
            SET name = '{newslc}'
            WHERE branch = 'SL'
            """

            execute_query(connection,setSGC)

            commanders.getinfo()

        elif res.component.label == "MP":
            embed=discord.Embed(title="AoT:U | Set Commander", description="Send the new MPC's username below:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.red,label="Exit")]])

            done, pending = await asyncio.wait([
                self.bot.wait_for("message", check= lambda message: message.author == author),
                self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)
            ], return_when=asyncio.FIRST_COMPLETED)

            done = done.pop().result()

            for task in pending:
                task.cancel()

            if isinstance(done, discord.Message):
                newmpc = done.content
                await done.delete()
                await ctx.send("MPC updated.")
                await msg.delete()
            else:
                await msg.delete()
                return

            setSGC = f"""
            UPDATE commanders
            SET name = '{newmpc}'
            WHERE branch = 'MP'
            """
            execute_query(connection,setSGC)

            commanders.getinfo()

        elif res.component.label == "CiC":

            embed=discord.Embed(title="AoT:U | Set Commander", description="Send the new CiC's username below:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.red,label="Exit")]])

            done, pending = await asyncio.wait([
                self.bot.wait_for("message", check= lambda message: message.author == author),
                self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)
            ], return_when=asyncio.FIRST_COMPLETED)

            done = done.pop().result()

            for task in pending:
                task.cancel()

            if isinstance(done, discord.Message):
                newcic = done.content
                await done.delete()
                await ctx.send("CiC updated.")
                await msg.delete()
            else:
                await msg.delete()
                return

            setSGC = f"""
            UPDATE commanders
            SET name = '{newcic}'
            WHERE branch = 'CiC'
            """

            execute_query(connection,setSGC)

            commanders.getinfo()

        elif res.component.label == "HTI":

            embed=discord.Embed(title="AoT:U | Set Commander", description="Send the new HTI's username below:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.red,label="Exit")]])

            done, pending = await asyncio.wait([
                self.bot.wait_for("message", check= lambda message: message.author == author),
                self.bot.wait_for("button_click", check=lambda res: res.user == author and res.channel == ctx.channel)
            ], return_when=asyncio.FIRST_COMPLETED)

            done = done.pop().result()

            for task in pending:
                task.cancel()

            if isinstance(done, discord.Message):
                newhti = done.content
                await done.delete()
                await ctx.send("HTI updated.")
                await msg.delete()
            else:
                await msg.delete()
                return

            setSGC = f"""
            UPDATE commanders
            SET name = '{newhti}'
            WHERE branch = 'HTI'
            """
            execute_query(connection,setSGC)

            commanders.getinfo()

        elif res.component.label == "Exit":
            await msg.delete()
            msg = await ctx.send("Process terminated.")
            await msg.delete(delay=5)


def setup(bot):
    bot.add_cog(Info(bot))