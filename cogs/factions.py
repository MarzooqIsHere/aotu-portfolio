import discord 
import logging
from discord import colour
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

whitelist = [channel ids and stuff]

defaultcolor = 0x352852

botpfp = "[redacted]"

# Actual Commands

class Factions(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    @commands.command(aliases=["factionrequest","frequest","faction"])
    async def fr(self,ctx):
        
        author = ctx.message.author

        fteam = discord.utils.get(ctx.guild.roles, id=redacted)

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        await ctx.message.delete()
        frchannel = discord.utils.get(ctx.guild.channels, id=redacted)
        requester = author.display_name
        requesterdiscord = f"{author.name}#{author.discriminator}"

        embed = discord.Embed(title="AoT:U | Faction Request",description="Wait 60 seconds if you want to cancel this request.",color = defaultcolor)
        embed.add_field(name="Faction Name", value="Type your faction name below:")
        await ctx.send(embed=embed)

        try:
            fname = await self.bot.wait_for("message",timeout=60 ,check=lambda message: message.author == author)
        except asyncio.TimeoutError:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You ran out of time {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        embed = discord.Embed(title="AoT:U | Faction Request",description="Wait 60 seconds if you want to cancel this request.",color = defaultcolor)
        embed.add_field(name="Faction Server Link", value="Send your faction's discord server below:")
        await ctx.send(embed=embed)

        try:
            flink = await self.bot.wait_for("message",timeout=60 ,check=lambda message: message.author == author)
        except asyncio.TimeoutError:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You ran out of time {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        embed = discord.Embed(title="AoT:U | Faction Request",description="Wait 60 seconds if you want to cancel this request.",color = defaultcolor)
        embed.add_field(name="Faction Purpose", value="Type your faction's purpose below:")
        await ctx.send(embed=embed)

        try:
            fpurpose = await self.bot.wait_for("message",timeout=60 ,check=lambda message: message.author == author)
        except asyncio.TimeoutError:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You ran out of time {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        await ctx.send("Request sent.")

        await frchannel.send(f"""{fteam.mention}
Faction Request from **{requester}**
**Requester:** {requester} / {requesterdiscord}

**Faction Name:** {fname.content}
**Discord Link:** {flink.content}

**Faction Purpose:** {fpurpose.content}

""")


    @commands.command(aliases=["nf","createfaction"])
    @has_permissions(manage_channels=True)
    async def newfaction(self,ctx):
        author = ctx.message.author

        if ctx.message.guild.id == redacted:
            pass
        else:
            return

        guild = ctx.guild

        embed = discord.Embed(title="New Faction", description="Send the faction's name below",color=defaultcolor)
        embed.set_author(name="AoT:U",icon_url=botpfp)
        embed.set_footer(text="Times out in 60 seconds")
        msg = await ctx.send(embed=embed)

        try:
            res = await self.bot.wait_for("message", check=lambda message: message.author == ctx.message.author and message.channel == ctx.message.channel,timeout=60.0)
        except TimeoutError:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You ran out of time {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return
        
        factionName = res.content

        await msg.delete()

        embed = discord.Embed(title="New Faction", description="Send the faction's head's ID below (they **must** be in this server)",color=defaultcolor)
        embed.set_author(name="AoT:U",icon_url=botpfp)
        embed.set_footer(text="Times out in 60 seconds")
        msg = await ctx.send(embed=embed)

        
        try:
            res = await self.bot.wait_for("message", check=lambda message: message.author == ctx.message.author and message.channel == ctx.message.channel, timeout=60.0)
        except TimeoutError:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: You ran out of time {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        factionHeadID = res.content
        factionHead = await self.bot.fetch_user(factionHeadID)
        await msg.delete()

        category = await guild.create_category(f"{factionName}")
        await category.set_permissions(factionHead,read_messages=True,send_messages=True)
        await category.set_permissions(guild.default_role,read_messages=False,send_messages=False)
        announcements = await guild.create_text_channel("announcements", category=category)
        general = await guild.create_text_channel("General", category=category)
        offTopic = await guild.create_text_channel("off-topic", category=category)
        bestOf = await guild.create_text_channel("best-of", category=category)


def setup(bot):
    bot.add_cog(Factions(bot))