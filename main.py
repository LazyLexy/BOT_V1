import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction, Activity, ActivityType, Status
import psutil
import time
import asyncio
from myserver import server_on
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

Welcome_emoji = "<a:2_:1200789975332040744> "
Fire_emoji = "<a:FirePurple:1285964011191402591> "
Number_emoji = "<a:bell:1285963604432261160> "
Vrf_emoji = "<a:checkmark:1285963484697202729> "
Vrfrec_emoji = "<a:vrf_rec:1285602992988491806> "

GUILD_ID = 1103309084104589395
start_time = time.time()

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"""{TerminalColors.HEADER}▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .
██· █▌▐█▀▄.▀·██•  ▐█ ▌▪ ▄█▀▄ ·██ ▐███▪▀▄.▀·
██▪▐█▐▐▌▐▀▀▪▄██ ▪ ██ ▄▄▐█▌.▐▌▐█ ▌▐▌▐█·▐▀▀▪▄
▐█▌██▐█▌▐█▄▄▌▐█▌ ▄▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌
 ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ 
""")
    print(f'{TerminalColors.BOLD}Logged in as {bot.user.name}')
    print(f"{TerminalColors.OKBLUE}Connected to {len(bot.guilds)} servers:{TerminalColors.ENDC}")
    for guild in bot.guilds:
        print(f"{TerminalColors.OKGREEN}- {guild.name} {TerminalColors.WARNING}(ID: {guild.id}){TerminalColors.ENDC}")
    total_users = sum(len(guild.members) for guild in bot.guilds)
    print(f"{TerminalColors.BOLD}{TerminalColors.WARNING}Serving {total_users} users{TerminalColors.ENDC}")
    print(f'{TerminalColors.BOLD}{TerminalColors.OKGREEN}{len(synced)} command(s)')
    while True:
        activities = [
            discord.Game(name="คำสั่ง /help"),
            discord.Streaming(name="Streaming", url="เกิดปัญหาอะไรติดต่อ bezonex"),
            discord.Activity(type=discord.ActivityType.watching, name="Bot by: BE4ON3X")
        ]
        for activity in activities:
            await bot.change_presence(activity=activity)
            await asyncio.sleep(10)

    #verify
    verification_channel = bot.get_channel(1200779471574269983)
    if verification_channel:
        embed = discord.Embed(
            title="𝐕𝐄𝐑𝐈𝐅𝐘 𝐓✦ 𝐄𝐍𝐓𝐄𝐑 𝐓𝐇𝐄 𝐒𝐄𝐑𝐕𝐄𝐑\n✦・︶︶꒷꒦︶꒦︶꒷꒦꒷︶︶꒦︶꒦꒷︶・✦",
            description=f"₊˚ :   𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐬𝐞𝐫𝐯𝐞𝐫!\n ₊˚ :   𝐏𝐥𝐞𝐚𝐬𝐞 𝐫𝐞𝐚𝐜𝐭 𝐰𝐢𝐭𝐡 {Vrfrec_emoji} 𝐭𝐨 𝐯𝐞𝐫𝐢𝐟𝐲 𝐲𝐨𝐮𝐫𝐬𝐞𝐥𝐟 𝐚𝐧𝐝 𝐠𝐚𝐢𝐧 𝐚𝐜𝐜𝐞𝐬𝐬.",
            color=0xff0064
        )

        embed.set_image(
            url='https://media.discordapp.net/attachments/1284250029208502326/1285595580298432573/standard.gif?ex=66ead7af&is=66e9862f&hm=cf77f7cebf890ef488b8cf72f9525ed1fbeddaba5be83d4dc095753c4b0f508a&=')
        try:
            message = await verification_channel.send(embed=embed)
            await message.add_reaction(Vrfrec_emoji)
            print("Embed message sent successfully.")
        except discord.Forbidden:
            print("Bot does not have permission to send messages in this channel.")
        except discord.HTTPException as e:
            print(f"Failed to send embed message: {e}")


#ping
@bot.tree.command(name='ping', description='ตรวจค่าปิงของบอท | Check bot response time')
async def ping(interaction):
    bot_latency = (bot.latency*1000)
    emmbed = discord.Embed(title="Pong! 🏓",
                           description=f"> **{bot_latency:.2f}** ms(avg!)",
                           color=0xff0064)
    emmbed.set_image(url='https://cdn.discordapp.com/attachments/1284250029208502326/1285325072831221902/ping.gif?ex=66e9dbc1&is=66e88a41&hm=9ee87f9bdd43493812817c71a782d1d41a4d880a8348383e3ea7711fb89eb798&')
    await interaction.response.send_message(embed = emmbed)

#info
@bot.tree.command(name='info', description='ข้อมูลบอท | Bot info')
async def ping(interaction):
    # bot_start_time
    current_time = time.time()
    uptime_seconds = current_time - start_time
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    uptime_seconds = uptime_seconds % 60
    #bot_latency
    bot_latency = (bot.latency*1000)
    emmbed = discord.Embed(title="📖  AiWaen Information ↷",
                           description=f"> ไอดี : ``{str(bot.user.id)}``\n> ชื่อ : ``{bot.user.name}``\n> เซิฟเวอร์ที่ใช้งาน : ``{len(bot.guilds)}``\n> จำนวนผู้ใช้ : ``{len(list(bot.get_all_members()))}``\n> discord.py Version : ``2.0+``\n> เวลาทำงาน : ``{int(uptime_hours)}h {int(uptime_minutes)}m {int(uptime_seconds)}s``",
                           color=0xff0064,
                           timestamp=discord.utils.utcnow())
    emmbed.set_image(url='https://media.discordapp.net/attachments/1284250029208502326/1285596266037903370/bot_info2.gif?ex=66ead853&is=66e986d3&hm=f3bfbde9fc4a547a762093b175e6a99850ea5d34168c9c9ada827280199d1d77&=')
    emmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1284250029208502326/1285328906215362612/742_20231104132634.jpg?ex=66e9df53&is=66e88dd3&hm=e270cc201808cf332612cd5352ac490d20b18a2dde3f5297589ee5dc1f8e468c&')
    await interaction.response.send_message(embed = emmbed)

#gateway คนเข้า
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1284250029208502326) #ไอดีห้อง
    guild = member.guild  # The current server
    member_count = guild.member_count  # Total number of members in the server
    emmbed = discord.Embed(title='𝗪𝗘𝗟𝗖𝗢𝗠𝗘  𝗧✦  𝗗𝗬𝗡𝗘𝗦𝗧𝗬\n✦・︶꒷꒦︶︶꒷꒦꒷︶︶꒦꒷︶・✦',
                           description= f"{Welcome_emoji}・𝗨𝗦𝗘𝗥︲{member.mention}\n{Number_emoji}・𝗡𝗨𝗠𝗕𝗘𝗥︲{member_count}\n{Fire_emoji}・𝗥𝗨𝗟𝗘𝗦︲<#1284250029208502326>\n{Vrf_emoji}・𝗩𝗘𝗥𝗜𝗙𝗬︲<#1284250029208502326>\n",
                           colour=0xff0064,
                           timestamp=discord.utils.utcnow())
    emmbed.set_image(url='https://media.discordapp.net/attachments/1284250029208502326/1285595580298432573/standard.gif?ex=66ead7af&is=66e9862f&hm=cf77f7cebf890ef488b8cf72f9525ed1fbeddaba5be83d4dc095753c4b0f508a&=')
    emmbed.set_thumbnail(url=member.avatar.url)
    await channel.send(embed = emmbed) #ส่งข้อความไปที่ห้องนั้นๆ

#vrf
VERIFIED_ROLE_ID = 1103309084104589397
VERIFICATION_CHANNEL_ID = 1200779471574269983



@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    # Checking if the emoji is the custom emoji by ID
    if reaction.message.channel.id == VERIFICATION_CHANNEL_ID and reaction.emoji.id == 1285602992988491806:  # Use the custom emoji ID here
        role = discord.utils.get(user.guild.roles, id=VERIFIED_ROLE_ID)
        if role:
            try:
                await user.add_roles(role)

                # Send confirmation message
                confirmation_message = await reaction.message.channel.send(f"{user.mention} has been verified and given the role!")

                # Delete confirmation message after a short delay
                await confirmation_message.delete(delay=5)

            except discord.Forbidden:
                await reaction.message.channel.send(f"Failed to add role to {user.mention}. The bot may not have the necessary permissions.")
            except discord.HTTPException as e:
                await reaction.message.channel.send(f"Failed to add role due to an HTTP error: {e}")
        else:
            await reaction.message.channel.send(f"Role with ID {VERIFIED_ROLE_ID} not found.")
    else:
        await reaction.message.channel.send(f"Invalid reaction or channel.")


@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    if reaction.message.channel.id == VERIFICATION_CHANNEL_ID and reaction.emoji == Vrfrec_emoji:
        role = discord.utils.get(user.guild.roles, id=VERIFIED_ROLE_ID)
        if role:
            try:

                # ลบปฏิกิริยา ✅ ที่ผู้ใช้ลบ
                await reaction.remove(user)

            except discord.Forbidden:
                await reaction.message.channel.send(
                    f"Failed to remove role from {user.mention}. The bot may not have the necessary permissions.")
            except discord.HTTPException as e:
                await reaction.message.channel.send(f"Failed to remove role due to an HTTP error: {e}")
        else:
            await reaction.message.channel.send(f"Role with ID {VERIFIED_ROLE_ID} not found.")
    else:
        await reaction.message.channel.send(f"Invalid reaction or channel.")


# คำสั่งแสดงข้อมูลเซิร์ฟเวอร์ใน embed
@bot.tree.command(name='guild', description='ข้อมูลเซิฟเวอร์ | Guild info')
async def ping(interaction):
    guild = interaction.guild
    # ข้อมูลพื้นฐานของเซิร์ฟเวอร์
    server_name = guild.name
    owner = guild.owner
    member_count = guild.member_count
    text_channel_count = len(guild.text_channels)
    voice_channel_count = len(guild.voice_channels)
    verification_level = guild.verification_level
    boost_count = guild.premium_subscription_count
    boost_tier = guild.premium_tier
    shard_id = guild.shard_id
    created_at = guild.created_at.strftime("%d/%m/%Y %H:%M")
    # สร้าง embed
    embed = discord.Embed(title=f"{server_name} Information", colour=0xff0064)
    # ส่วนข้อมูลเจ้าของ
    embed.add_field(name="``📖`` ข้อมูลต่างๆ ↷", value=f"┊เจ้าของ ``:`` {owner.mention}\n┊ภาษา ``:`` ``th``\n╰ ชื่อ ``:`` ``{server_name}``", inline=False)
    embed.add_field(name='``📚`` ข้อมูลต่างๆ ↷',
                    value=f'```เลเวลบูส : {boost_tier}\nจำนวนบทบาท : {len(guild.roles)}\nห้องเสียงทั้งหมด : {voice_channel_count}\nสมาชิกทั้งหมด : {member_count}/{guild.max_members}\nความปลอดภัย : {verification_level}\nอีโมจิ : {len(guild.emojis)}\nเลเวลบูส : {boost_count}\n```',
                    inline=False)
    embed.set_image(url='https://media.discordapp.net/attachments/1284250029208502326/1285589711968014336/guild_info.gif?ex=66ead238&is=66e980b8&hm=a0f0bb31699deb6ba7953174a80e742de1a8238686ef9047caa8eff9791daf36&=')
    embed.set_thumbnail(url=guild.icon.url)
    embed.set_footer(text=f"ID ・ {guild.id} | 🕗เซิฟเวอร์ถูกสร้างเมื่อ ・ {created_at}")
    await interaction.response.send_message(embed = embed)

#help
@bot.tree.command(name='help', description='คำสั่งใช้งานบอทเบื้องต้น | Help Commands')
async def ping(interaction):
    emmbed = discord.Embed(title="🎸  Help Commands ↷", color=0xff0064)
    emmbed.add_field(name='> /help', value='> คำสั่งใช้งานบอทเบื้องต้น', inline=True)
    emmbed.add_field(name='> /info', value='> ข้อมูลบอท', inline=True)
    emmbed.add_field(name='> /guild', value='> ข้อมูลเซิฟเวอร์', inline=True)
    emmbed.add_field(name='> /ping', value='> เช็คปิงบอท', inline=True)
    emmbed.set_image(url='https://media.discordapp.net/attachments/1284250029208502326/1285636747379605586/help.gif?ex=66eafe06&is=66e9ac86&hm=e7b24720c83b21aaaa79139619156e4d75e9109d9cc320f30ff3ed2f54058167&=')
    await interaction.response.send_message(embed = emmbed)

server_on()

bot.run(os.getenv('TOKEN'))
