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

whitelist = [channel ids]

defaultcolor = 0x352852

# Actual Commands

class Misc(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ditto(self, ctx,*,arg):

        await ctx.send(arg)

    @commands.command()
    async def memes(self,ctx):
        author = ctx.message.author

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        memelist = ["pick up the phone baby", 
            "soldier of the stationary guard!",
            "mp pride",
            "wall sasageyo",
            "you're so ass",
            "bryce",
            "yo homie dead",
            "bomber",
            "i got a new roach",
            "adios commander",
            "smoked",
            "ill beat yo ass",
            "it's walter wednesday",
            "hobu",
            "disco face",
            "sg fuckfest",
            "fight back"]

        memes = ""

        for m in memelist:
            memes += f"• `{m}`\n"

        author = ctx.author
        embed = discord.Embed(title="AoT:U | Meme List", color=defaultcolor)
        embed.add_field(name="List", value=memes)
        await author.send(embed=embed)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            messagesent=discord.Embed(color=defaultcolor)
            messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
            msg = await ctx.send(embed=messagesent)
            await msg.delete(delay=5.0)


    @commands.command()
    async def about(self,ctx):
        author = ctx.message.author

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        embed=discord.Embed(title="AoT:U Bot | About", description="AoT:U Bot was made by Marzooq and it provides many features to make AoT:U easier to play and enjoy.",color=defaultcolor)
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Version", value="1.8", inline=False)
        embed.add_field(name="Bug Reports", value="redacted", inline=True)
        embed.set_footer(text="Lead: Marzooq Helpers: ErichLegacy, Luigi122342, MissingAdler")
        await author.send(embed=embed)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            messagesent=discord.Embed(color=defaultcolor)
            messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
            msg = await ctx.send(embed=messagesent)
            await msg.delete(delay=3)

    @commands.command()
    async def reactiontest(self,ctx):

        author = ctx.message.author

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return


        msg = await ctx.send("React to this message.")
        await msg.add_reaction("🤡")

        await self.bot.wait_for("reaction_add",check=lambda reaction,user: str(reaction.emoji)=="🤡" and user == ctx.message.author)

        await ctx.send("You are a clown.")

    @commands.command()
    async def latency(self,ctx):
        await ctx.send(f"{float(self.bot.latency)*1000}ms")




def setup(bot):
    bot.add_cog(Misc(bot))