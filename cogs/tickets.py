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

whitelist = [814533871562784798,
580592288334348349,
299664952388747264,
821862043010727968,
801244090506543144,
718296924855206028,
796218668946030642,
796371548347826177,
805779268931158016,
838406201300877363]

defaultcolor = 0x352852

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

econstaff = []

def checkstaff(column,list):


    sms = execute_query(connection, "SELECT * from staffmembers")

    whole = []

    for record in sms:
        whole.append(record)

    for r in whole:
        if r[column] == 1:
            list.append(r[22])

checkstaff(8, list=econstaff)

# Actual Commands

class Tickets(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ticket(self,ctx):

        category = discord.utils.get(ctx.guild.categories, id=838172698928349258)
        coderperms = await self.bot.fetch_user(316288809216245762)
        author = ctx.message.author

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        guild = ctx.guild
        nickname = author.display_name
        moderator = discord.utils.get(ctx.guild.roles, id=316740881476485123)
        admin = discord.utils.get(ctx.guild.roles, id=299662755936600087)
        inductee = discord.utils.get(ctx.guild.roles, id=587839427867443208)
        loreteamrole = discord.utils.get(ctx.guild.roles, id=538784453078548490)
        logchannel = discord.utils.get(ctx.guild.channels, id=838174340230414356)
        
        embed=discord.Embed(title="AoT:U | Open Ticket", description="Select ticket category:",color=defaultcolor)
        embed.add_field(name="PD", value="For PD options",inline=False)
        embed.add_field(name="Help", value="For help categories (regular and admin)",inline=False)
        embed.add_field(name="Other", value="For anything else like economy",inline=False)
        msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="PD",disabled=True), Button(style=ButtonStyle.green,label="Help"), Button(style=ButtonStyle.green,label="Other"), Button(style=ButtonStyle.red,label="Exit")]])

        res = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel and res.message == msg)

        if res.component.label == "PD":
            embed=discord.Embed(title="AoT:U | Open Ticket", description="Select PD type:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed,components=[[Button(style=ButtonStyle.green,label="Med"), Button(style=ButtonStyle.green,label="Titan Training"), Button(style=ButtonStyle.green,label="Building"), Button(style=ButtonStyle.green, label="Woodchopping"), Button(style=ButtonStyle.green,label="Mining")],[Button(style=ButtonStyle.green,label="Lore"), Button(style=ButtonStyle.green,label="Rep"), Button(style=ButtonStyle.green,label="Other"), Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check=lambda yes: yes.user == author and yes.channel == ctx.channel and yes.message == msg)

            if yes.component.label == "Med":
                await logchannel.send(f"{author.mention} has opened a med PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Med PD", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Med PD Ticket.")
                await msg.delete()

            elif yes.component.label == "Titan Training":
                await logchannel.send(f"{author.mention} has opened a titan training ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Titan Training", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Titan Training Ticket.")
                await msg.delete()
                

            elif yes.component.label == "Building":
                await logchannel.send(f"{author.mention} has opened a building PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Building", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Building PD Ticket.")
                await msg.delete()

            elif yes.component.label == "Woodchopping":
                await logchannel.send(f"{author.mention} has opened a wood-chopping PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Wood chopping", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole, read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Wood-chopping PD Ticket.")
                await msg.delete()
        
            elif yes.component.label == "Mining":
                await logchannel.send(f"{author.mention} has opened a mining PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Mining", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Mining PD Ticket.")
                await msg.delete()
            
            elif yes.component.label == "Lore":
                await logchannel.send(f"{author.mention} has opened a lore PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Lore", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Lore PD Ticket.")
                await msg.delete()
            
            elif yes.component.label == "Rep":
                await logchannel.send(f"{author.mention} has opened a rep PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Rep", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True,send_messages=True)
                await channel.set_permissions(admin, read_messages=True,send_messages=True)
                await channel.set_permissions(inductee, read_messages=True,send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Rep PD Ticket.")
                await msg.delete()
            elif yes.component.label == "Other":
                await logchannel.send(f"{author.mention} has opened an other type PD ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="PD Request ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="PD Type ", value=f"Other PD Type", inline=False)
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True, send_messages=True)
                await channel.set_permissions(admin, read_messages=True, send_messages=True)
                await channel.set_permissions(inductee, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.set_permissions(loreteamrole,read_messages=True,send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s PD (Other) Ticket.")
                await msg.delete()
            elif yes.component.label == "Exit":
                await msg.delete()
                msg = await ctx.send("Command exited.")
                await msg.delete(delay=5)
        elif res.component.label == "Help":
            embed=discord.Embed(title="AoT:U | Open Ticket", description="Select Help type:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="Help (All staff)"), Button(style=ButtonStyle.green, label = "Admin Help"), Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda yes: yes.user == author and yes.channel == ctx.channel and yes.message == msg)

            if yes.component.label == "Help (All staff)":
                await logchannel.send(f"{author.mention} has opened a help ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="Help ", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="Instructions", value=f"Please describe the issue below and a staff member will reply ASAP.\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(admin, read_messages=True, send_messages=True)
                await channel.set_permissions(moderator, read_messages=True, send_messages=True)
                await channel.set_permissions(inductee, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Help Ticket.")
                await msg.delete()
            elif yes.component.label == "Admin Help":
                await logchannel.send(f"{author.mention} has opened an admin ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="Admin Help", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="Instructions", value=f"Please describe the issue below and a staff member will reply ASAP.\nPing admins every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{admin.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(admin, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Admin Ticket.")
                await msg.delete()
            elif yes.component.label == "Exit":
                await msg.delete()
                await ctx.send("Command exited.")
                await msg.delete(delay=5)

        elif res.component.label == "Other":

            embed=discord.Embed(title="AoT:U | Open Ticket", description="Select Other type:",color=defaultcolor)
            await msg.delete()
            msg = await ctx.send(embed=embed, components = [[Button(style=ButtonStyle.green,label="Economy"), Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda yes: yes.user == author and yes.channel == ctx.channel and yes.message == msg)

            if yes.component.label == "Economy":
                await logchannel.send(f"{author.mention} has opened an econ ticket.")
                channel = await ctx.guild.create_text_channel(f"ticket-for-{author.display_name}", category=category)
                check = await ctx.send(f"{author.mention}. Check the main server for your ticket channel. {channel.mention}")
                await check.delete(delay=5)
                embed=discord.Embed(title="Econ Request", color=defaultcolor)
                embed.set_author(name="AoT:U | Ticket System")
                embed.add_field(name="Instructions ", value=f"Fill in the following form in the following format: \n ```**Time:**\n**Location:**\n**Notes/Info:**```\nPing moderators, admins, and inductees every few hours if they do not respond.\nUse `.close` in this channel to close this ticket.", inline=False)
                embed.set_footer(text="made by marzooq ")
                await channel.send(embed=embed)
                await channel.send(f"{author.mention}\n{moderator.mention} {admin.mention} {inductee.mention} {loreteamrole.mention}")
                await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(author, read_messages=True, send_messages=True)
                await channel.set_permissions(coderperms, read_messages=True, send_messages=True)
                await channel.edit(topic = f"{author.display_name}'s Economy Ticket.")
                await msg.delete()
                for s in econstaff:
                    smember = await self.bot.fetch_user(s)
                    try:
                        await channel.set_permissions(smember, read_messages=True, send_messages=True)
                        name = smember.name
                        print(name + " succeeded")
                    except:
                        name = smember.name
                        print(name + " failed")
                
            elif yes.component.label == "Exit":
                await msg.delete()
                msg = await ctx.send("Command exited.")
                await msg.delete(delay=5)
        
        elif res.component.label == "Exit":
            await msg.delete()
            msg = await ctx.send("Command exited")
            await msg.delete(delay=5)


    @commands.command()
    async def close(self,ctx):
        author = ctx.message.author
        category = ctx.message.channel.category
        channel = ctx.message.channel
        logchannel = discord.utils.get(ctx.guild.channels, id=838174340230414356)
        publiclogs = discord.utils.get(ctx.guild.channels, id=840610004117225472)

        selectTimeInfo = """
            SELECT * from averagetimes
            """

        info = execute_query(connection, selectTimeInfo)

        infodissect = []

        for i in info:
            infodissect.append(i)

        for i in infodissect:
            totaltime = i[0]
            totalno = i[1]
        
        timenow = datetime.utcnow()
        difference = timenow - channel.created_at
        dseconds = difference.seconds
        ddays = difference.days
        hours = dseconds // 3600
        minutes = (dseconds//60)%60
        hoursforsheet = hours + (ddays*24) + (minutes/60)

        if hoursforsheet < 0.16666666667:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: Cannot close this channel as it is not 10 minutes old yet.", inline=False)
            await ctx.send(embed=embed)
            return
        else:
            pass


        topic = channel.topic
        name, ttype = topic.split("'s ", 1)
        ttype = ttype.replace(".","")

        tickettime = (f"{ddays} days, {hours} hours and {minutes} minutes")

        addInfo = f"""
            UPDATE averagetimes
            SET totaltime = {float(totaltime) + float(hoursforsheet)}, totalno = {int(totalno) + 1}
            """

        execute_query(connection,addInfo)

        average = float(totaltime + float(hoursforsheet)) / (int(totalno) + 1)
        average = timedelta(hours=float(average))
        averageseconds = average.seconds
        averagedays = average.days
        averagehours = averageseconds // 3600
        averageminutes = (averageseconds//60)%60
        averagetime = (f"{averagedays} days, {averagehours} hours and {averageminutes} minutes")


        if category.id == 838172698928349258:
            await logchannel.send(f"{author.mention} has closed a {ttype}. #{channel.name}")
            embed=discord.Embed(title="Ticket Closed", description=f"{ttype} was closed in {tickettime}",color=defaultcolor)
            embed.set_footer(text=f"Average time: {averagetime}")
            await publiclogs.send(embed=embed) 
            await channel.delete()
        else: 
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: Cannot close this channel. I see what you're trying to do, retard gtfo here :eyes:", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def add(self,ctx, member : discord.Member):

        await ctx.message.delete()
        author = ctx.message.author
        channel = ctx.message.channel
        category = discord.utils.get(ctx.guild.categories, id=838172698928349258)


        if category.id == 838172698928349258:
            await channel.set_permissions(member, read_messages=True, send_messages=True)
            await ctx.send(f"{member.mention} added to the ticket.")


    @commands.command()
    @has_permissions(kick_members=True)
    async def remove(self,ctx, member : discord.Member):
        await ctx.message.delete()
        author = ctx.message.author
        channel = ctx.message.channel
        logs = discord.utils.get(ctx.guild.channels, id=840610004117225472)
        testchannel = discord.utils.get(ctx.guild.channels, id=838406201300877363)
        category = discord.utils.get(ctx.guild.categories, id=838172698928349258)



        if category.id == 838172698928349258:
            await channel.set_permissions(member, read_messages=False, send_messages=False)
            await ctx.send(f"{member.mention} removed to the ticket.")


def setup(bot):
    bot.add_cog(Tickets(bot))

   