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

whitelist = [channel id]

defaultcolor = 0x352852

gc = gspread.service_account(filename = "aotu-bot-b0020fac483b.json")
punishmentlist = gc.open_by_key("1RN6b9TKfD7xCGCY02t0Dw6kcNyTzuxsXzITUo5rkYzk")
banlist = punishmentlist.sheet1

# Actual Commands

class Mod(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def unban (self, ctx, uid):
        mainserver = self.bot.get_guild(redacted)
        author = ctx.message.author
        if author.guild_permissions.administrator or author.guild_permissions.ban_members:
            pass
        else:
            return
        servers = [redacted]

        tobebanned = await self.bot.fetch_user(uid)
        
        for serverid in servers:
            server = self.bot.get_guild(serverid)
            bannedusers = await server.bans()
            for banentry in bannedusers:
                user = banentry.user
                if f"{user.name}#{user.discriminator}" == f"{tobebanned.name}#{tobebanned.discriminator}":
                    try:
                        await server.unban(user)
                    except:
                        print(f"failed to unban from {server.name}")
        
            

        await ctx.send(f"Unbanned {tobebanned.mention}")

    @commands.command()
    async def ban(self,ctx, uid: discord.Member, length, *, reason):
        print("Beginnging")
        author = ctx.message.author
        if author.guild_permissions.administrator or author.guild_permissions.ban_members:
            pass
        else:
            return

        print("Passed perm check")
        mainserver = self.bot.get_guild(redacted)

        print("After mainser = self.bot")

        try:
            uid = int(uid)
        except:
            pass


        if isinstance(uid, int) == True:
            member = await self.bot.fetch_user(uid)
        elif isinstance(uid, discord.Member) == True:
            member = uid

        print("After member parse")

        bl = banlist.get_all_values()
        mipo = len(bl) + 1

        print("After Sheet grab")

        await ctx.message.delete()

        if length == "perm":
            today = datetime.now()
            today = today.strftime("%m" + "/" + "%d" + "/" + "%y")
            sheetbanlength = f"{today} - Permanent"
            playername = member.display_name
            prestaff = ctx.message.author
            staff = prestaff.display_name
            staff, uselessassbit = staff.split("|", 1)

        elif length[:-1].isnumeric():
            today = datetime.now()
            playername = member.display_name
            if length.endswith("d"):
                length = length[:-1]
                banover = today + timedelta(days=int(length))
                length = f"{length} days"
            elif length.endswith("w"):
                length = length[:-1]
                banover = today + timedelta(weeks=int(length))
                length = f"{length} weeks"
            elif length.endswith("m"):
                length = length[:-1]
                banover = today + timedelta(days=31 *int(length))
                length = f"{length} months"
            elif length.endswith("y"):
                length = length[:-1]
                length = f"{length} years"
                banover = today + timedelta(days=365 * int(length))
            prestaff = ctx.message.author
            staff = prestaff.display_name
            staff, uselessassbit = staff.split("|", 1)
            today = today.strftime("%m" + "/" + "%d" + "/" + "%y")
            banover = banover.strftime("%m" + "/" + "%d" + "/" + "%y")
            sheetbanlength = f"{today} - {banover}"
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Length should either be 'perm' or an integer followed by a time increment (ie. 12d or 1y) {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        print("After length parsing")

        embed=discord.Embed(title=f"Notes | {playername}", description="Use 'none' if you don't want to add any notes.",color=defaultcolor)
        nm = await ctx.send(embed=embed)

        def check(user):
            return user == ctx.message.author

        try: 
            msg = await self.bot.wait_for("message", timeout=30.0, check=lambda message: message.author == ctx.message.author)
            if msg.content == "none":
                notes = ""
            else:
                notes = msg.content 
            await nm.delete()
            await msg.delete()
        except asyncio.TimeoutError:
            await ctx.send("You ran out of time.")


        row = ["Both", playername, f"{sheetbanlength}", reason, staff, notes]
        banlist.insert_row(row, mipo)

        print("added to sheet")


        if length == "perm":
            await member.send(f"Greetings, {member.display_name}. You have been permanently banned from AoT:U by {author.name}#{author.discriminator}. The reason stated is:\n**{reason}\nFor more information regarding the AoT:U Binding Ruleset, visit https://aotuniverse.net/guidelines/binding-ruleset/")
        elif type(length) == int:
            await member.send(f"Greetings, {member.display_name}. You have been banned for {length} by {author.name}#{author.discriminator}. The reason stated is:\n**{reason}**\nFor more information regarding the AoT:U Binding Ruleset, visit https://aotuniverse.net/guidelines/binding-ruleset/")

        print("message sent")

        servers = [299660651910004736,262963971361865728,419629573286789120,419627594648911873,419627664471752704,601456669196812308]
        
        
        for server in servers:
            try:
                otherguild = self.bot.get_guild(server)
                print(otherguild.name)
                await otherguild.ban(member, reason=reason)
            except:
                print("failed to ban")
                pass

        
        await ctx.send (f"Banned {member.mention}")

    @ban.error
    async def banerror(self,ctx,error):
        if isinstance(error, MissingPermissions):
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You do not have permissions to use this command.", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)

    @commands.command()
    @has_permissions(kick_members=True)
    async def mute(self,ctx,uid : discord.Member):
        mainserver = self.bot.get_guild(299660651910004736)

        author = ctx.message.author

        try:
            uid = int(uid)
        except:
            pass


        if isinstance(uid, int) == True:
            member = await self.bot.fetch_user(uid)
        elif isinstance(uid, discord.Member) == True:
            member = uid

        for role in member.roles:
            try:
                await member.remove_roles(role)
            except:
                pass
        await member.add_roles(discord.utils.get(mainserver.roles,id=329299494027919360))
        await member.add_roles(discord.utils.get(mainserver.roles,id=303259572200800256))

        await ctx.send(f"Muted {member.mention}")

    @commands.command()
    @has_permissions(kick_members=True)
    async def unmute(self,ctx,uid: discord.Member):
        mainserver = self.bot.get_guild(299660651910004736)

        try:
            uid = int(uid)
        except:
            pass


        if isinstance(uid, int) == True:
            member = await self.bot.fetch_user(uid)
        elif isinstance(uid, discord.Member) == True:
            member = uid

        await member.remove_roles(discord.utils.get(mainserver.roles,id=329299494027919360))
        await member.remove_roles(discord.utils.get(mainserver.roles,id=303259572200800256))
        await member.add_roles(discord.utils.get(mainserver.roles,id=337431076177707008))
        await member.add_roles(discord.utils.get(mainserver.roles,id=733175468185878558))

        await ctx.send(f"Unmuted {member.mention}")

    @commands.command()
    @has_permissions(manage_messages = True)
    async def clear (self,ctx, amount = 5):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)

    
def setup(bot):
    bot.add_cog(Mod(bot))