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

# Actual Commands

class staffmembers:

    def __init__(self,id,hostables=[],reco=[],deps=[],haformat="",rformat="",dformat="",bio="",colour=0x352852):
        self.id = id
        self.hostables = hostables
        self.reco = reco
        self.deps = deps
        self.haformat = haformat
        self.rformat = rformat
        self.dformat = dformat
        self.bio = bio
        self.colour = colour

    def resetinfo(self,hostables=[],reco=[],deps=[],haformat="",rformat="",dformat="",bio="",colour=0x352852):
        self.hostables = []
        self.reco = []
        self.deps = []
        self.haformat = ""
        self.rformat = ""
        self.dformat = ""
        self.bio = ""
        self.colour = 0x352852

    def getinfo(self,id,hostables=[],reco=[],deps=[],haformat="",rformat="",dformat="",colour=0x352852):
        self.hostables.clear
        self.reco.clear
        self.deps.clear
        haformat = ""
        rformat = ""
        dformat = ""
        colour = 0x352852

        sms = execute_query(connection,"SELECT * from staffmembers")

        whole = []

        for record in sms:
            whole.append(record)

        for r in whole:
            if int(r[22]) == self.id:

                self.colour = int(r[21],16)

                if int(r[0]) == 1:
                    self.hostables.append("Titan Trainings")
                
                if int(r[1]) == 1:
                    self.hostables.append("Med PDs")

                if int(r[2]) == 1:
                    self.hostables.append("Rep PDs")
                
                if int(r[3]) == 1:
                    self.hostables.append("Mining PDs")
                
                if int(r[4]) == 1:
                    self.hostables.append("Building PDs")
                
                if int(r[5]) == 1:
                    self.hostables.append("Woodchopping PDs")
                
                if int(r[6]) == 1:
                    self.hostables.append("Lore PDs")

                if int(r[7]) == 1:
                    self.deps.append("Faction Team")
                
                if int(r[8]) == 1:
                    self.deps.append("Economy Team")
                
                if int(r[9]) == 1:
                    self.deps.append("Lore Team")

                if int(r[10]) == 1:
                    self.deps.append("Outreach Team")

                if int(r[11]) == 1:
                    self.deps.append("Eboard")
                
                if int(r[12]) == 1:
                    self.reco.append("Titan Trainings")
                
                if int(r[13]) == 1:
                    self.reco.append("Med PDs")

                if int(r[14]) == 1:
                    self.reco.append("Rep PDs")
                
                if int(r[15]) == 1:
                    self.reco.append("Mining PDs")
                
                if int(r[16]) == 1:
                    self.reco.append("Building PDs")

                if int(r[17]) == 1:
                    self.reco.append("Woodchopping PDs")

                if int(r[18]) == 1:
                    self.reco.append("Lore PDs")


                if str(r[20]) == "":
                    self.bio = "N/A"
                else:
                    self.bio = str(r[20])
                

                for h in self.hostables:
                    self.haformat += (f"• {h}\n")

                for r in self.reco:
                    self.rformat += (f"• {r}\n")

                for d in self.deps:
                    self.dformat += (f"• {d}\n")

                if self.dformat == "":
                    self.dformat = "N/A"

                if self.haformat == "":
                    self.haformat = "N/A"

                if self.rformat == "":
                    self.rformat = "N/A"

                

marzooq = staffmembers(316288809216245762)
marzooq.resetinfo()
marzooq.getinfo(316288809216245762)
loogi = staffmembers(155747479764074497)
loogi.resetinfo()
loogi.getinfo(155747479764074497)
wind = staffmembers(169569985230798848)
wind.resetinfo()
wind.getinfo(169569985230798848)
alive = staffmembers(100697818817126400)
alive.resetinfo()
alive.getinfo(100697818817126400)
leo = staffmembers(414568632320786433)
leo.resetinfo()
leo.getinfo(414568632320786433)
aisu = staffmembers(325403729522065418)
aisu.resetinfo()
aisu.getinfo(325403729522065418)
izu = staffmembers(213729329413095424)
izu.resetinfo()
izu.getinfo(213729329413095424)
knight = staffmembers(255488170379051008)
knight.resetinfo()
knight.getinfo(255488170379051008)
adler = staffmembers(249877126273040386)
adler.resetinfo()
adler.getinfo(249877126273040386)
junko = staffmembers(218569136551231499)
junko.resetinfo()
junko.getinfo(218569136551231499)
astern = staffmembers(311245590510174210)
astern.resetinfo()
astern.getinfo(311245590510174210)


# Actual Commands

class StaffCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def staff(self, ctx):

        author = ctx.message.author

        embed=discord.Embed(title="AoT:U | Staff", description="Select staff category:",color=defaultcolor)
        embed.add_field(name="Admins", value="View administrators",inline=False)
        embed.add_field(name="Mods", value="View moderators",inline=False)
        embed.add_field(name="Inductees", value="View inductees",inline=False)
        embed.add_field(name="Lore Team", value="alr i think you get the point, view lore team",inline=False)
        embed.set_footer(text="Bot made by Marzooq :D (with a little help from ErichLegacy)")
        msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="Admins"), Button(style=ButtonStyle.green,label="Mods"), Button(style=ButtonStyle.green,label="Inductees"), Button(style=ButtonStyle.green,label="Lore Team"),Button(style=ButtonStyle.red,label="Exit")]])

        res = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

        if res.component.label == "Admins":
            await msg.delete()

            embed=discord.Embed(title="AoT:U | Staff", description="Select staff member:",color=defaultcolor)
            embed.add_field(name="Admins", value="• Luigi\n• Alive\n• Leo \n• Aisu\n• Adler\n• Wind",inline=False)
            embed.set_footer(text="Bot made by Marzooq :D (with a little help from ErichLegacy)")
            msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="Aisu"), Button(style=ButtonStyle.green,label="Adler"),Button(style=ButtonStyle.green,label="Luigi"),Button(style=ButtonStyle.green,label="Alive")],[Button(style=ButtonStyle.green,label="Leo"),Button(style=ButtonStyle.green,label="Wind"),Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

            if yes.component.label == "Aisu":
                await msg.delete()
                sm = await self.bot.fetch_user(325403729522065418)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Aisu | Head Admin", description=f"*{aisu.bio}*", color=aisu.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=aisu.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=aisu.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=aisu.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Adler":
                await msg.delete()
                sm = await self.bot.fetch_user(249877126273040386)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Adler | Head Mod", description=f"*{adler.bio}* ", color=adler.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=adler.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=adler.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=adler.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Luigi":
                await msg.delete()
                sm = await self.bot.fetch_user(155747479764074497)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Luigi | Admin", description=f"*{loogi.bio}* ", color=loogi.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=loogi.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=loogi.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=loogi.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Alive":
                await msg.delete()
                sm = await self.bot.fetch_user(100697818817126400)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Alive | Admin", description=f"*{alive.bio}* ", color=alive.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=alive.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=alive.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=alive.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Leo":
                await msg.delete()
                sm = await self.bot.fetch_user(414568632320786433)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Leonard | Admin", description=f"*{leo.bio}* ", color=leo.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value="• Head of Economy", inline=False)
                embed.add_field(name="Recommended PDs", value=leo.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=leo.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Wind":
                await msg.delete()
                sm = await self.bot.fetch_user(169569985230798848)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Wind | Head Admin", description=f"*{wind.bio}* ", color=wind.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value="• Head Admin", inline=False)
                embed.add_field(name="Recommended PDs", value="• Cases", inline=False)
                embed.add_field(name="Hostable PDs", value=wind.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Exit":
                await msg.delete()
                return
        
        elif res.component.label == "Mods":
            await msg.delete()

            embed=discord.Embed(title="AoT:U | Staff", description="Select staff member:",color=defaultcolor)
            embed.add_field(name="Mods", value="• Junko\n• Izu\n• Knight\n• Marzooq\n• Astern", inline=False)
            embed.set_footer(text="Bot made by Marzooq :D (with a little help from ErichLegacy)")
            msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="Marzooq"),Button(style=ButtonStyle.green,label="Junko"),Button(style=ButtonStyle.green,label="Izu")],[Button(style=ButtonStyle.green,label="Knight"),Button(style=ButtonStyle.green,label="Astern"),Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

            
            if yes.component.label == "Junko":
                await msg.delete()
                sm = await self.bot.fetch_user(218569136551231499)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Junko | Mod", description=f"*{junko.bio}* ", color=junko.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=junko.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=junko.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=junko.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Astern":
                await msg.delete()
                sm = await self.bot.fetch_user(311245590510174210)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Astern | Mod", description=f"*{astern.bio}* ", color=junko.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=astern.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=astern.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=astern.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Izu":
                await msg.delete()
                sm = await self.bot.fetch_user(213729329413095424)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Izu | Mod", description=f"*{izu.bio}* ", color=izu.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=izu.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=izu.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=izu.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Knight":
                await msg.delete()
                sm = await self.bot.fetch_user(255488170379051008)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Knight | Mod", description=f"*{knight.bio}* ", color=knight.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=knight.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=knight.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=knight.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Marzooq":
                await msg.delete()
                sm = await self.bot.fetch_user(316288809216245762)
                smpfp = sm.avatar_url
                embed=discord.Embed(title="Marzooq | Mod", description=f"*{marzooq.bio}* ", color=marzooq.colour)
                embed.set_author(name="AoT:U Info")
                embed.set_thumbnail(url=smpfp)
                embed.add_field(name="Department(s)", value=marzooq.dformat, inline=False)
                embed.add_field(name="Recommended PDs", value=marzooq.rformat, inline=False)
                embed.add_field(name="Hostable PDs", value=marzooq.haformat, inline=False)
                embed.set_footer(text="This bot was made by Marzooq :3 (with a little help from ErichLegacy)")
                await ctx.send(embed=embed)
            elif yes.component.label == "Exit":
                await msg.delete()
                return
        
        elif res.component.label == "Inductees":

            await msg.delete()

            embed=discord.Embed(title="AoT:U | Staff", description="Select staff member:",color=defaultcolor)
            embed.add_field(name="Inductees", value="Coming soon...", inline=False)
            embed.set_footer(text="Bot made by Marzooq :D (with a little help from ErichLegacy)")
            eyes = discord.PartialEmoji(name="👀")
            msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.gray,disabled=True,emoji=eyes), Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

            if yes.component.label == "Exit":
                await msg.delete()
                return

        elif res.component.label == "Lore Team":

            await msg.delete()

            embed=discord.Embed(title="AoT:U | Staff", description="Select staff member:",color=defaultcolor)
            embed.add_field(name="Lore Team", value="Coming soon...", inline=False)
            embed.set_footer(text="Bot made by Marzooq :D (with a little help from ErichLegacy)")
            eyes = discord.PartialEmoji(name="👀")
            msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.gray,disabled=True,emoji=eyes), Button(style=ButtonStyle.red,label="Exit")]])

            yes = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

            if yes.component.label == "Exit":
                await msg.delete()
                return

        elif res.component.label == "Exit":
            await msg.delete()
            return

    @commands.command()
    async def set(self, ctx,option=None):
        author = ctx.message.author
        authorid = author.id

        sms = execute_query(connection, "SELECT * from staffmembers")

        whole = []

        for record in sms:
            whole.append(record)

        

        ha = discord.utils.get(ctx.guild.roles, id=361068539768995843)
        hl = discord.utils.get(ctx.guild.roles, id=745008718076444773)
        hd = discord.utils.get(ctx.guild.roles, id=397538047618580481)

        isEboard = False

        if ha in author.roles or hl in author.roles or hd in author.roles:
            isEboard = True

        
        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        
        if authorid == 155747479764074497:
            user = loogi
        elif authorid == 169569985230798848:
            user = wind
        elif authorid == 100697818817126400:
            user = alive
        elif authorid == 414568632320786433:
            user = leo
        elif authorid == 325403729522065418:
            user = aisu
        elif authorid == 213729329413095424:
            user = izu
        elif authorid == 255488170379051008:
            user = knight
        elif authorid == 249877126273040386:
            user = adler
        elif authorid == 218569136551231499:
            user = junko
        elif authorid == 316288809216245762:
            user = marzooq 
        elif authorid == 311245590510174210:
            user = astern
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: You cannot use this command.", inline=False)
            await ctx.send(embed=embed)
            return   


        if option == None:
            embed=discord.Embed(title="AoT:U | Set Profile ", description="List of customisable features in `.set`", color=defaultcolor)
            embed.set_author(name ="AoT:U | Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Bio", value="`.set bio`", inline=False)
            embed.add_field(name="Hostable PDs", value="`.set hostables`", inline=False)
            embed.add_field(name="Recommended PDs", value="`.set recommended`", inline=False)
            embed.add_field(name="Departments", value="`.set departments`", inline=False)
            embed.add_field(name="Colour", value="`.set colour` or `.set color`", inline=False)
            embed.set_footer(text="made by marzooq")
            await ctx.send(embed=embed)
        
        if option == "bio":
            embed = discord.Embed(title="AoT:U | Set Profile",color = defaultcolor)
            embed.add_field(name="New bio", value="Type your new bio below:")
            await ctx.send(embed=embed)

            newbio = await self.bot.wait_for("message", check=lambda message: message.author == author)
            newbioc = newbio.content
            newbioc = newbioc.replace("'", "''")
            for r in whole:
                if int(r[22]) == author.id:

                    updatedBio = f"""
                    UPDATE staffmembers
                    SET bio = '{newbioc}'
                    WHERE id = '{author.id}'
                    """

                    execute_query(connection,updatedBio)
            
            await ctx.send("Updated.")

        elif option == "colour" or option == "color":
            embed = discord.Embed(title="AoT:U | Set Profile",color=defaultcolor)
            embed.add_field(name="New Profile Colour", value="Type your colour's hex code below without the hashtag (ex. 352852):")
            await ctx.send(embed=embed)

            newcolour = await self.bot.wait_for("message", check=lambda message: message.author == author)
            newcolourc = newcolour.content
            
            for r in whole:
                if int(r[22]) == author.id:
                    updatedColour = f"""
                    UPDATE staffmembers
                    SET colour = '0x{newcolourc}'
                    WHERE id = '{author.id}'
                    """

                    execute_query(connection,updatedColour)

            await ctx.send("Updated")

        elif option == "hostables":
            embed = discord.Embed(title="AoT:U | Set Profile",description ="*Add a thumbs up reaction when done.*",color = defaultcolor)
            embed.add_field(name="Set Hostable PDs", value="""React as appropriate:
            :one: Titan Trainings
            :two: Med PDs
            :three: Rep PDs
            :four: Mining PDs
            :five: Building PDs
            :six: Woodchopping PDs
            :seven: Lore PDs
            :thumbsup: Done
            """)
            msg = await ctx.send(embed=embed)
            msgreactions = ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","👍"]

            for r in msgreactions:
                await msg.add_reaction(r)
            
            await self.bot.wait_for("reaction_add",check=lambda reaction,user: str(reaction.emoji)=="👍" and user == ctx.message.author)

            await ctx.send("Uploading info.")

            msg = await msg.channel.fetch_message(msg.id)

            for r in msg.reactions:
                if r.emoji == "1️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET tthostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "1️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET tthostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "2️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET medhostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                elif r.emoji == "2️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET medhostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "3️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET rephostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "3️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET rephostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "4️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET mininghostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "4️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET mininghostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "5️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET buildinghostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "5️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET buildinghostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "6️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET woodchoppinghostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "6️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET woodchoppinghostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "7️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET lorehostable = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "7️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET lorehostable = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)


        elif option == "recommended":
            embed = discord.Embed(title="AoT:U | Set Profile",description ="*Add a thumbs up reaction when done.*",color = defaultcolor)
            embed.add_field(name="Set Recommended PDs", value="""React as appropriate:
            :one: Titan Trainings
            :two: Med PDs
            :three: Rep PDs
            :four: Mining PDs
            :five: Building PDs
            :six: Woodchopping PDs
            :seven: Lore PDs
            :thumbsup: Done
            """)
            msg = await ctx.send(embed=embed)
            msgreactions = ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","👍"]

            for r in msgreactions:
                await msg.add_reaction(r)
            
            print(msg.reactions)
            
            await self.bot.wait_for("reaction_add",check=lambda reaction,user: str(reaction.emoji)=="👍" and user == ctx.message.author)

            await ctx.send("Uploading info.")


            msg = await msg.channel.fetch_message(msg.id)
            print(msg.reactions)

            for r in msg.reactions:
                if r.emoji == "1️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET ttreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "1️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET ttreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "2️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET medreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "2️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET medreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "3️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET repreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "3️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET repreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "4️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET miningreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "4️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET miningreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "5️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET buildingreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "5️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET buildingreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "6️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET woodchoppingreco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "6️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET woodchoppingreco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "7️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET lorereco = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "7️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET lorereco = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

        elif option == "departments" or option == "department" or option == "dep":
            embed = discord.Embed(title="AoT:U | Set Profile",description ="*Add a thumbs up reaction when done.*",color = defaultcolor)
            embed.add_field(name="Set Departments", value="""React as appropriate:
            :one: Faction Team
            :two: Economy Team
            :three: Lore Team
            :four: Outreach Team
            :five: Eboard
            :thumbsup: Done
            """)
            msg = await ctx.send(embed=embed)
            msgreactions = ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣","👍"]

            for r in msgreactions:
                await msg.add_reaction(r)
            
            print(msg.reactions)
            
            await self.bot.wait_for("reaction_add",check=lambda reaction,user: str(reaction.emoji)=="👍" and user == ctx.message.author)

            await ctx.send("Uploading info.")


            msg = await msg.channel.fetch_message(msg.id)
            print(msg.reactions)

            for r in msg.reactions:
                if r.emoji == "1️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET factionteam = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "1️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET factionteam = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "2️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET econteam = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "2️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET econteam = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "3️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET loreteam = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "3️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET loreteam = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "4️⃣" and r.count == 2:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET outreachteam = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "4️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET outreachteam = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)

                if r.emoji == "5️⃣" and r.count == 2 and isEboard == True:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET eboard = '1'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)
                elif r.emoji == "5️⃣" and r.count == 1:
                    for i in whole:
                        if int(i[22]) == author.id:
                            updated = f"""
                            UPDATE staffmembers
                            SET eboard = '0'
                            WHERE id = '{author.id}'
                            """
                            execute_query(connection,updated)


        user.resetinfo()
        user.getinfo(author.id)

def setup(bot):
    bot.add_cog(StaffCommand(bot))