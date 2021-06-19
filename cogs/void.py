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

gc = gspread.service_account(filename = "redacted")
ongoingvoids = gc.open_by_key("redacted")
ogv = ongoingvoids.sheet1

# Actual Commands

class Voids(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(kick_members = True)
    async def void(self,ctx, username, url, *, notes=None):
        commandmessage = ctx.message
        staffactions = discord.utils.get(ctx.guild.channels, id=580592288334348349)
        msg = await staffactions.send(f"**{username}'s Void Evidence** \n*{notes}* \n {url}")

        msgreactions = ["👍", "👎"]
        for reactions in msgreactions:
            await msg.add_reaction(reactions)

        timeinaday = datetime.now() + timedelta(days=1)
        comptime = timeinaday.strftime("%y"+"%m"+"%d"+"%H"+"%M")

        row = [username, str(comptime), str(msg.id)]
        index = 1 
        ogv.insert_row(row, index)

        
        await commandmessage.delete()

    @commands.command()
    @has_permissions(kick_members=True)
    async def checkvoids(self,ctx):
        cmdmsg = ctx.message
        staffannouncements = discord.utils.get(ctx.guild.channels, id=423640972103122945)
        staffactions = discord.utils.get(ctx.guild.channels, id=580592288334348349)
        mainserver = self.bot.get_guild(299660651910004736)
        today = datetime.now()
        cvcomptime = today.strftime("%y"+"%m"+"%d"+"%H"+"%M")
        try:
            voids = ogv.get_all_values()
        except gspread.APIError:
            await ctx.send(f"Oops! The bot has attempted to access Google's API too many times in the past 100 seconds! Calm down with using this command for the next 100 seconds.")
        checkrow = 0
        for v in voids:
            checkrow += 1
            print(checkrow)
            username = v[0]
            deadline = v[1]
            messageID = v[2]
            print(messageID)
            try:
                processingmessage = await staffactions.fetch_message(int(messageID))
                for r in processingmessage.reactions:
                    if r.emoji == "👍":
                        upvotes = r.count
                    elif r.emoji == "👎":
                        downvotes = r.count
                if upvotes >= 6 or downvotes >= 6:
                    if upvotes > downvotes:
                        await staffannouncements.send(f"{username} has been voided.")
                        result = await ctx.send(f"{username}'s results are ready.")
                        await result.delete(delay=3)
                        ogv.delete_row(checkrow)
                        checkrow -= 1
                    elif downvotes > upvotes:
                        await staffannouncements.send(f"{username} has not been voided.")
                        result = await ctx.send(f"{username}'s results are ready.")
                        await result.delete(delay=3)
                        ogv.delete_row(checkrow)
                        checkrow -= 1
                    else:
                        await staffactions.send(f"{mainserver.default_role} {username}'S VOTE IS AT A DRAW. START DISCUSSING RETARDS. AND IF THERE'S NO VOTES, START FUCKING VOTING ITS BEEN A WHOLE ASS DAY THE FUCK IS WRONG WITH Y'ALL???")
                else:
                    result = await ctx.send(f"{username}'s results are not ready.")
                    await result.delete(delay=3)
            except discord.errors.NotFound:
                fuckwuan = await ctx.send(f"{ctx.author.mention} SOME FUCKING MONKEY DELETED A MESSAGE BRUH (im deleting it doe dw.)")
                await fuckwuan.delete(delay=5)
                ogv.delete_row(checkrow)    

        await cmdmsg.delete()

    @commands.command()
    @has_permissions(kick_members = True)
    async def endvoid(self,ctx, mid):

        staffactions = discord.utils.get(ctx.guild.channels, id=580592288334348349)

        try:
            voids = ogv.get_all_values()
        except gspread.APIError:
            await ctx.send(f"Oops! The bot has attempted to access Google's API too many times in the past 100 seconds! Calm down with using this command for the next 100 seconds.")

        checkrow = 0
        for v in voids:
            checkrow += 1
            if v[2] == mid:
                ongoingvoidmessage = await staffactions.fetch_message(int(mid))
                await ongoingvoidmessage.delete()
                ogv.delete_row(checkrow)

                con = await ctx.send(f"{v[0]}'s void has been ended.")
                await con.delete(delay = 5)

        await ctx.message.delete()

    @commands.command()
    @has_permissions(kick_members=True)
    async def remind(self,ctx):
        moderator = discord.utils.get(ctx.guild.roles, id=316740881476485123)
        admin = discord.utils.get(ctx.guild.roles, id=299662755936600087)
        inductee = discord.utils.get(ctx.guild.roles, id=587839427867443208)
        author = ctx.message.author
        staffactions = discord.utils.get(ctx.guild.channels, id=580592288334348349)
        mainserver = self.bot.get_guild(299660651910004736)
        myballs = ""
        

        try:
            voids = ogv.get_all_values()
        except gspread.APIError:
            await ctx.send(f"Oops! The bot has attempted to access Google's API too many times in the past 100 seconds! Calm down with using this command for the next 100 seconds.")

        for v in voids:

            username = v[0]
            deadline = v[1]
            messageID = v[2]

            processingmessage = await staffactions.fetch_message(int(messageID))
            for r in processingmessage.reactions:
                if r.emoji == "👍":
                    upvotes = r.count
                elif r.emoji == "👎":
                    downvotes = r.count
            if upvotes >= 6 or downvotes >= 6:
                pass
            else:
                myballs += f"{username} - https://discord.com/channels/299660651910004736/580592288334348349/{messageID}\n"

        embed=discord.Embed(color=defaultcolor)
        embed.add_field(name="Unready Voids", value=myballs, inline=False)
        await staffactions.send(embed=embed)
        await staffactions.send(f"{moderator.mention} {admin.mention} {inductee.mention}")
    

def setup(bot):
    bot.add_cog(Voids(bot))