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

# Actual Commands

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["getroles"])
    async def getrole(self,ctx):

        author = ctx.message.author
        message = ctx.message


        mpinmain = discord.utils.get(ctx.guild.roles, id=726851781513969675),
        slinmain = discord.utils.get(ctx.guild.roles, id=726851786484219984),
        sginmain = discord.utils.get(ctx.guild.roles, id=726851784147992646),
        tiinmain = discord.utils.get(ctx.guild.roles, id=299663716465639425)

        roles = [mpinmain,slinmain,sginmain,tiinmain]

        

        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        embed=discord.Embed(title="AoT:U | Get Role", description="Select branch:",color=defaultcolor)
        msg = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green,label="MP"), Button(style=ButtonStyle.green,label="SG"), Button(style=ButtonStyle.green,label="SL"),Button(style=ButtonStyle.green,label="TI"), Button(style=ButtonStyle.gray,label="Exit")]])

        res = await self.bot.wait_for("button_click", check= lambda res: res.user == author and res.channel == ctx.channel)

        for role in roles:
            try:
                await author.remove_roles(role)
            except:
                pass

        if res.component.label == "MP":
            print(author.id)
            mp = self.bot.get_guild(419627594648911873)
            print(f"MP server gotten. {mp.name}")
            mppp = discord.utils.get(mp.roles, id=643292504623677450)
            print(f"Got the MP Personnel Role. {mppp.name}")
            mpinmain = discord.utils.get(ctx.guild.roles, id=726851781513969675)
            print(f"MP role in main server obtained. {mpinmain.name}")
            checkinmp = await mp.fetch_member(author.id)
            print(f"Got the member in MP server. {checkinmp.name}")
            print(checkinmp.roles)
            if mppp in checkinmp.roles:
                print("adding role")
                await author.add_roles(mpinmain)
            else:
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Error", value=":warning: You are not in MP. ", inline=False)
                msg = await ctx.send(embed=embed)
                await msg.delete(delay=5)
            await message.delete()
        elif res.component.label == "SL":

            print(author.id)
            sl = self.bot.get_guild(419627664471752704)
            print(f"SL server obtained. {sl.name}")
            sllp = discord.utils.get(sl.roles, id=419662373771542529)
            print(f"Got the SL Personnel Role. {sllp.name}")
            slinmain = discord.utils.get(ctx.guild.roles, id=726851786484219984)
            print(f"SL role in the main server obtained. {slinmain.name}")
            checkinsl = await sl.fetch_member(author.id)
            print(f"Got the member in SL server. {checkinsl.name}")
            print(checkinsl.roles)
            if sllp in checkinsl.roles:
                print("adding role")
                await author.add_roles(slinmain)
            else:
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Error", value=":warning: You are not in SL. ", inline=False)
                msg = await ctx.send(embed=embed)
                await msg.delete(delay=5)
            await message.delete()
        elif res.component.label == "SG":
            print(author.id)
            sg = self.bot.get_guild(419629573286789120)
            print(f"SG server obtained. {sg.name}")
            sggp = discord.utils.get(sg.roles, id=419662484299841549)
            print(f"Got the SG Personnel Role. {sggp.name}")
            sginmain = discord.utils.get(ctx.guild.roles, id=726851784147992646)
            print(f"SG role in the main server obtained. {sginmain.name}")
            checkinsg = await sg.fetch_member(author.id)
            print(f"Got in the member SG server. {checkinsg.name}")
            print(checkinsg.roles)
            if sggp in checkinsg.roles:
                print("adding role")
                await author.add_roles(sginmain)
            else:
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Error", value=":warning: You are not in SG. ", inline=False)
                msg = await ctx.send(embed=embed)
                await msg.delete(delay=5)
            await message.delete()
        elif res.component.label == "TI":
            print(author.id)
            ti = self.bot.get_guild(262963971361865728)
            print(f"TC server obtained. {ti.name}")
            tii = discord.utils.get(ti.roles, id=621897408850427904)
            print(f"Got the Instructor Role. {tii.name}")
            tiinmain = discord.utils.get(ctx.guild.roles, id=299663716465639425)
            print(f"TI role in the main server obtained. {tiinmain.name}")
            checkinti = await ti.fetch_member(author.id)
            print(f"Got in the member SG server. {checkinti.name}")
            print(checkinti.roles)
            if tii in checkinti.roles:
                print("adding role")
                await author.add_roles(tiinmain)
            else:
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Error", value=":warning: You are not in TI. ", inline=False)
                msg = await ctx.send(embed=embed)
                await msg.delete(delay=5)
            await message.delete()
            

    @commands.command(aliases=["removeroles"])
    async def removerole(self,ctx):
        author = ctx.message.author
        message = ctx.message
        mpinmain = discord.utils.get(ctx.guild.roles, id=726851781513969675)
        sginmain = discord.utils.get(ctx.guild.roles, id=726851784147992646)
        slinmain = discord.utils.get(ctx.guild.roles, id=726851786484219984)
        tiinmain = discord.utils.get(ctx.guild.roles, id=299663716465639425)


        if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
            msg = await ctx.send(embed=embed)  
            await msg.delete(delay=5)
            return

        try:
            await author.remove_roles(mpinmain)
        except:
            pass
        
        try:
            await author.remove_roles(slinmain)
        except:
            pass
        try:
            await author.remove_roles(sginmain)
        except:
            pass

        try:
            await author.remove_roles(tiinmain)
        except:
            pass
        
        await message.delete()


def setup(bot):
    bot.add_cog(Roles(bot))