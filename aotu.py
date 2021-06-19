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
import emoji
from spam import spamdict

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = ".", help_command=None,case_insensitive=False,intents=intents)
bot.remove_command('help') 

defaultcolor = 0x352852

whitelist = [channel ids were here :D]


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(name="AoT:U")
    await bot.change_presence(status=discord.Status.online,activity=game)
    global prison 
    global mainserver
    mainserver = bot.get_guild(redacted)
    prison = discord.utils.get(mainserver.channels, id=redacted)
    global moderatorrole
    moderatorrole = discord.utils.get(mainserver.roles, id=redacted)
    global botcommands
    botcommands = discord.utils.get(mainserver.channels, id=redacted)


    

@bot.event
async def on_message(message):

    def check(m):
        return(m.author == message.author and (datetime.utcnow()-m.created_at).seconds < 5)

    if not message.author.bot:
        if len(list(filter(lambda m: check(m), bot.cached_messages))) >= 8:
            async for role in message.author.roles:
                try:
                    await message.author.remove_roles(role)
                except:
                    pass
            await message.author.add_roles(discord.utils.get(message.channel.guild.roles,id=redacted))
            await message.author.add_roles(discord.utils.get(message.channel.guild.roles,id=redacted))
            await prison.send(f"{moderatorrole.mention} {message.author.mention} has been caught spamming. smh")
            return

    mc = message.content
    mc = mc.lower()
    
    if "nigga" in mc or "nigger" in mc or "kike" in mc or "faggot" in mc or "fag" in mc:
        await message.delete()
        sry = await message.channel.send("That word is not allowed in this server. Apologies for the inconvenience.")
        await sry.delete(delay=5)

    try:
        botcommands = discord.utils.get(message.guild.channels, id=redacted)
        if message.channel == botcommands:
            if "bot" in mc and "useless" in mc:
                responselist = [
                    "i swear  im not uselss!!!",
                    "if only i wasnt made by marzooq smh :rolling_eyes:",
                    "i AM useful fuck you",
                    f"you a bitch {message.author.mention}",
                    f"{message.author.mention} dnc keep crying bitchass mf",
                    "动态网自由门 天安門 天安门 法輪功 李洪志 Free Ryujin 六四天安門事件 LN Central 天安門大屠殺 Ackryllic Bias 反右派鬥爭 Staff Bias Struggle 大躍進政策 LN Picked as high command with no vote 文化大革命 LN Central always 20v1s with all of MP 人權 Player Rights 民運 Freedom to Ryujin自由 Freedom 獨立 Independence 多黨制 In-lore Admins 台灣 臺灣 Wall bad owner 中華民國",
                    "I AM EXTREMELY USEFUL AYO BRO STFU DUMBASS MF ILL BAN YO DUMBASS TRY ME",
                    "i apologise for being useless man...",
                    "kk dnc",
                    "whatchu know about rolling down in the deep",
                    "Silence, mortal being."
                ]
                await message.channel.send(random.choice(responselist)) 
    except:
        pass

    if mc.startswith('pick up the phone baby'):
        await message.channel.send("[redacted]")
    if mc.startswith("soldier of the stationary guard!"):
        await message.channel.send("[redacted]")
    if mc.startswith("mp pride"):
        await message.channel.send("[redacted]")
    if mc.startswith("wall sasageyo"):
        await message.channel.send("[redacted]")
    if mc.startswith("you're so ass"):
        await message.channel.send("[redacted]")
    if mc == "bryce":
        await message.channel.send("[redacted]")
    if mc == "yo homie dead":
        await message.channel.send("[redacted]")
    if mc == "bomber":
        await message.channel.send("[redacted]")
    if mc == "i got a new roach":
        await message.channel.send("[redacted]")
    if mc == "adios commander":
        await message.channel.send("[redacted]")
    if mc == "smoked":
        await message.channel.send("[redacted]")
    if mc == "ill beat yo ass":
        await message.channel.send("[redacted]")
    if mc == "it's walter wednesday":
        await message.channel.send("[redacted]")
    if mc == "hobu":
        await message.channel.send("[redacted]")
    if mc == "disco face":
        await message.channel.send("[redacted]")
    if mc == "sg fuckfest":
        await message.channel.send("[redacted]")
    if mc == "fight back":
        await message.channel.send("[redacted]")

    await bot.process_commands(message)

@bot.command()
async def help(ctx, arg = "main"):

    if arg != None:
        arg = arg.lower()

    author = ctx.message.author
    await ctx.message.delete()

    
    if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
        pass
    else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
        msg = await ctx.send(embed=embed)  
        await msg.delete(delay=5)
        return
    
    if arg == "main":
        embed=discord.Embed(title="AoT:U | Help", description="List of commands. You can also use commands on their own to see the options available (ex. .staff)", color=defaultcolor)
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="`.ticket`", value="Open a ticket to request a PD. (ex. .ticket tt)", inline=False)
        embed.add_field(name="`.close`", value="Closes your ticket. (ex. `.close`)", inline=False)
        embed.add_field(name="`.info`", value="Get information about AoT:U. (ex. .info tc)", inline=False)
        embed.add_field(name="`.staff`", value="View staff, their capabilities and bios. (ex. .staff marzooq)", inline=False)
        embed.add_field(name="`.dev`", value="View devs and what they do for AoT:U. (ex. .dev rad)", inline=False)
        embed.add_field(name="`.dep`", value="View staff departments and their function in AoT:U. (ex. .dep economy)", inline=False) 
        embed.add_field(name="`.about`", value="View the bot's version number and a suggestions/bug report form. (ex. .about)", inline=False)  
        embed.add_field(name="`.devset`", value="**Dev only** Change your dev bio (ex. .devset bio)", inline=False)
        embed.add_field(name="`.memes`", value="View a list of memes the bot provides (ex. .memes)",inline=False)     
        embed.add_field(name="`.fr`", value="Lets you request a faction through Discord (ex. .fr)",inline=False)    
        embed.add_field(name="`.getrole`", value="Get the role for the branch you are in. (ex. .getrole mp)",inline=False)     
        embed.add_field(name="`.removerole`", value="Remove branch roles that you do not need/use. (ex. .removerole sl)",inline=False)      
        embed.set_footer(text="made by marzooq ")
        await author.send(embed=embed)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            messagesent=discord.Embed(color=defaultcolor)
            messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
            msg = await ctx.send(embed=messagesent)
            await msg.delete(delay=5.0)
    elif arg == "mod" or arg == "staff":
        if author.guild_permissions.kick_members:
            embed=discord.Embed(title="AoT:U | Help", description="List of commands. You can also use commands with options on their own to see the options available.", color=defaultcolor)
            embed.set_thumbnail(url="[redacted]")
            embed.add_field(name="`.void`", value=r"Start the automatic void process for a player. (ex. .void [username] [url] {notes})", inline=False)
            embed.add_field(name="`.checkvoids`", value=r"Check on voids which automatically sends ready voids to #staff-announcements. (ex. .checkvoids)", inline=False)
            embed.add_field(name="`.endvoid`", value=r"End a void and remove it from the system. (ex. .endvoid [vote message id])", inline=False)
            embed.add_field(name="`.ban`", value=r"Bans a player from every AoT:U server and logs it onto the banlist. (ex. .ban [member id] [length in days] [reason])", inline=False)
            embed.add_field(name="`.unban`", value=r"Unbans a player from every AoT:U server. (ex. .ban [member id] [length in days] [reason])", inline=False)
            embed.add_field(name="`.set`", value=r"Set your profile info. Change your hostable PDs, recommended PDs, department, and bio. (ex. .set hostables)", inline=False)
            embed.add_field(name="`.clear`", value=r"Purge messages. Default is 5 messages. (ex. .clear 7)", inline=False)
            embed.add_field(name="`.remind`", value=r"Remind the others of which voids need voting on. (ex. .remind)", inline=False)
            embed.set_footer(text="made by marzooq ")
            await author.send(embed=embed)
            if isinstance(ctx.channel, discord.channel.DMChannel):
                pass
            else:
                messagesent=discord.Embed(color=defaultcolor)
                messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
                msg = await ctx.send(embed=messagesent)
                await msg.delete(delay=5.0)
        else:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Error", value=":warning: You need to be a staff member to use this command.", inline=False)
            msg = await ctx.send(embed=embed)
            await msg.delete(delay=5.0)
    else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Error", value=":warning: Option not recognised. Only `.help`, `.help staff` and `.help mod` are recognised.", inline=False)
        await ctx.send(embed=embed)  


@bot.command()
async def dep(ctx, depa=None):
    author = ctx.message.author
    
    if ctx.message.channel.id in whitelist or isinstance(ctx.channel, discord.channel.DMChannel):
        pass
    else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Error", value=f":warning: Bot commands are prohibited in this channel. {author.mention}", inline=False)
        msg = await ctx.send(embed=embed)  
        await msg.delete(delay=5)
        return

    if depa == None:
        embed=discord.Embed(title="Departments", description="List of departments. Use these with `.dep` to find members of departments.", color=defaultcolor)
        embed.set_author(name="AoT:U | Info")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Faction Team", value="`.dep faction`", inline=False)
        embed.add_field(name="Economy Team ", value="`.dep economy`", inline=False)
        embed.add_field(name="Lore Team", value="`.dep lt`", inline=False)
        embed.add_field(name="Outreach Team", value="`.dep outreach`", inline=False)
        embed.add_field(name="Eboard", value="`.dep eboard`", inline=False)
        embed.set_footer(text="made by marzooq")
        await author.send(embed=embed)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            messagesent=discord.Embed(color=defaultcolor)
            messagesent.add_field(name="Sent",value=f"Check your DMs {author.mention}")
            msg = await ctx.send(embed=messagesent)
            await msg.delete(delay=5.0)
    elif depa == "faction":
        embed=discord.Embed(title="Faction Team", description="The Faction Team approves and moderates factions in AoT:U.", color=defaultcolor)
        embed.set_author(name="AoT:U | Departments")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Head of Faction Team", value="- Alive", inline=False)
        embed.add_field(name="Members", value="\n- Adler \n- Sloopy \n- Marzooq", inline=False)
        embed.set_footer(text="made by marzooq ")
        await ctx.send(embed=embed)
    elif depa == "economy":
        embed=discord.Embed(title="Economy Team", description="The Economy Team moderates and works on AoT:U's economy.", color=defaultcolor)
        embed.set_author(name="AoT:U | Departments")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Head of Economy Team", value="- Leo", inline=False)
        embed.add_field(name="Members", value="- Alive \n- Marzooq\n- Knight ", inline=False)
        embed.set_footer(text="made by marzooq ")
        await ctx.send(embed=embed)
    elif depa == "lt" or depa == "lore":
        embed=discord.Embed(title="Lore Team", description="The Lore Team create the storyline of AoT:U.", color=defaultcolor)
        embed.set_author(name="AoT:U | Departments")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Head of Lore Team", value="- Ackryllic  ", inline=False)
        embed.add_field(name="Lore Team Members", value="- Alive \n- Luigi \n- Wuan\n- Adler \n- Retro \n- Stormy \n- Glad \n- Aisu\n- Respawn", inline=False)
        embed.add_field(name="Trial Lore Team Members", value="N/A", inline=False)
        embed.set_footer(text="made by marzooq ")
        await ctx.send(embed=embed)
    elif depa == "outreach":
        embed=discord.Embed(title="Outreach Team", description="The Outreach Team's job is to connect and take feedback from the community.", color=defaultcolor)
        embed.set_author(name="AoT:U | Departments")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Head of Outreach Team", value="- Luigi", inline=False)
        embed.add_field(name="Members", value="- Glad \n- Aisu \n- Stormy \n- Dutchko", inline=True)
        embed.set_footer(text="made by marzooq ")
        await ctx.send(embed=embed)
    elif depa == "eboard":
        embed=discord.Embed(title="e-Board", description="The eboard is the staff members at the top in charge of the most important matters.", color=defaultcolor)
        embed.set_author(name="AoT:U | Departments")
        embed.set_thumbnail(url="[redacted]")
        embed.add_field(name="Game Owner", value="- Wall", inline=False)
        embed.add_field(name="Head Admin", value="- Aisu", inline=False)
        embed.add_field(name="Head Moderator ", value="- ???", inline=False)
        embed.set_footer(text="made by marzooq ")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Error", value=":warning: Option not recognised. Use `.dep` to see all options. ", inline=False)
        await ctx.send(embed=embed)
    


bot.load_extension("cogs.mod")
bot.load_extension("cogs.tickets")
bot.load_extension("cogs.roles")
bot.load_extension("cogs.factions")
bot.load_extension("cogs.void")
bot.load_extension("cogs.staff")
bot.load_extension("cogs.info")
bot.load_extension("cogs.dev")
bot.load_extension("cogs.misc")
bot.run("TOKEN_ID")