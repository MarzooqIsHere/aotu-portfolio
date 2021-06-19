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

class DevTeam:

    def __init__(self,id,bio="",colour=0x352852):
        self.bio = bio
        self.colour = colour
        self.id = id 

    def resetinfo(self,bio="",colour=0x352852):
        self.bio = ""
        self.colour = 0x352852

    def getinfo(self,id,bio="",colour=0x352852):
        self.bio = ""
        self.colour = 0x352852


        developers = execute_query(connection,"SELECT * from developers")

        devs = []

        for record in developers:
            devs.append(record)

        for r in devs:
            if int(r[0]) == self.id:

                self.bio = r[2]
                self.colour = int(r[3],16)

        

rad = DevTeam(redacted)        
rad.resetinfo()
rad.getinfo(redacted)
kenji = DevTeam(redacted)
kenji.resetinfo()
kenji.getinfo(redacted)
saw = DevTeam(redacted)     
saw.resetinfo()
saw.getinfo(redacted)
text = DevTeam(redacted)
text.resetinfo()
text.getinfo(redacted)
harp = DevTeam(redacted)
harp.resetinfo()  
harp.getinfo(redacted)
francis = DevTeam(redacted)
francis.resetinfo()
francis.getinfo(redacted)
marzooqd = DevTeam(redacted)
marzooqd.resetinfo()
marzooqd.getinfo(redacted)

whitelist = [channel ids]

defaultcolor = 0x352852


# Actual Command Stuff

class DevCommand(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def dev(self,ctx, arg=None):
        if arg != None:
            arg = arg.lower()

        author = ctx.message.author

        
        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        if arg ==  None:
            embed=discord.Embed(title="Dev Commands", description="Use these commands to find dev team members (ex. $dev rad)", color=defaultcolor)
            embed.set_author(name="AoT:U Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Rad - Head Developer", value="`.dev rad`", inline=False)
            embed.add_field(name="Harp - Animator", value="`.dev harp`", inline=False)
            embed.add_field(name="Saw - Mesher", value="`.dev saw`", inline=False)
            embed.add_field(name="Kenji - Scripter", value="`.dev kenji`", inline=False)
            embed.add_field(name="Francis - Scripter", value="`.dev francis`", inline=False)
            embed.add_field(name="Text - GFX Artist", value="`.dev text`", inline=False)
            await author.send(embed=embed)
            if isinstance(ctx.channel, discord.channel.DMChannel):
                pass
            else:
                messagesent=discord.Embed(color=defaultcolor)
                messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
                msg = await ctx.send(embed=messagesent)
                await msg.delete(delay=5.0)
        elif arg == "rad":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Rad | Head Developer", description=rad.bio, color=rad.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "marzooq":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Marzooq | Bot Developer", description=marzooqd.bio, color=marzooqd.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "francis":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Francis | Scripter", description=francis.bio, color=francis.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "kenji":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Kenji | Scripter", description=kenji.bio, color=kenji.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            embed.set_footer(text="He also helped with making some of this bot's features, shoutout kenji")
            await ctx.send(embed=embed)
        elif arg == "saw":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Saw | Mesher", description=saw.bio, color=saw.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "text":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Text | GFX Artist", description=text.bio, color=text.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "harp":
            sm = await self.bot.fetch_user(redacted)
            smpfp = sm.avatar_url
            embed=discord.Embed(title="Harp | Animator", description=harp.bio, color=harp.colour)
            embed.set_thumbnail(url=smpfp)
            embed.set_author(name="AoT:U Info")
            await ctx.send(embed=embed)
        elif arg == "devteamlowkeylazynegl":
            await ctx.message.delete()
            msg = await ctx.send("Ong, mfs really do be ignoring the player requests and doing nothing.")
            secondmsg = await ctx.send("Jk ly devs")
            await msg.delete(delay=1)
            await secondmsg.delete(delay=1)
            thirdmsg = await ctx.send("nah you lazy")
            await thirdmsg.delete(delay=1)
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: Option not recognised. Use `.dev` to see all options.", inline=False)
            await ctx.send(embed=embed)   


    @commands.command()
    async def devset(self,ctx,option=None):
        author = ctx.message.author
        authorid = author.id
        developers = execute_query(connection,"SELECT * from developers")

        devs = []
        for record in developers:
            devs.append(record)


        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        if authorid == redacted:
            user = rad
        elif authorid == redacted:
            user = kenji
        elif authorid == redacted:
            user = saw
        elif authorid == redacted:
            user = text
        elif authorid == redacted:
            user = harp
        elif authorid == redacted:
            user = francis
        elif authorid == redacted:
            user = marzooqd
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: You cannot use this command.", inline=False)
            await ctx.send(embed=embed)
            return   

        if option == None:
            embed=discord.Embed(title="AoT:U | Set Dev Profile ", description="List of customisable features in `.devset`", color=defaultcolor)
            embed.set_author(name="AoT:U | Info")
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="Bio", value="`.devset bio`", inline=False)
            embed.add_field(name="Colour", value="`.devset colour` or `.devset color`", inline=False)
            embed.set_footer(text="made by marzooq")
            await ctx.send(embed=embed)
        elif option == "bio":
            embed = discord.Embed(title="AoT:U | Set Dev Profile",color = defaultcolor)
            embed.add_field(name="New bio", value="Type your new bio below:")
            await ctx.send(embed=embed)

            newbio = await self.bot.wait_for("message", check=lambda message: message.author == author)


            newbioc = newbio.content
            newbioc = newbioc.replace("'","''")
            print(newbioc)
            for r in devs:
                if int(r[0]) == author.id:
                    
                    updatedBio = f"""
                    UPDATE developers
                    SET bio = '{newbioc}'
                    WHERE id = '{author.id}'
                    """
                    
                    execute_query(connection,updatedBio)

            
            await ctx.send("Updated.")

        elif option == "colour" or option == "color":
            embed = discord.Embed(title="AoT:U | Set Dev Profile",color=defaultcolor)
            embed.add_field(name="New Profile Colour", value="Type your colour's hex code below without the hashtag (ex. 352852):")
            await ctx.send(embed=embed)

            newcolour = await self.bot.wait_for("message", check=lambda message: message.author == author)
            newcolourc = newcolour.content
            for r in devs:
                if int(r[0]) == author.id:
                    updatedColour = f"""
                    UPDATE developers
                    SET colour = '0x{newcolourc}'
                    WHERE id = '{author.id}'
                    """
                    
                    execute_query(connection,updatedColour)

            await ctx.send("Updated")

        user.resetinfo()
        user.getinfo(author.id)

def setup(bot):
    bot.add_cog(DevCommand(bot))