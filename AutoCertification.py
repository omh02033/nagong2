import discord
import asyncio
import openpyxl
import os

client = discord.Client()
channelid = '662180169221668894'
servername = "METEOR"
@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("===================")

    @client.event
    async def on_message(message):
        if message.content.startswith('!인증'):
            channel = message.channel.id
            if channel == int(channelid):
                if message.author.bot:
                    return None
                nick = message.author.nick
                id = message.author.id
                print(id)
                author = message.author
                if nick == None:
                    file = openpyxl.load_workbook("경고.xlsx")
                    sheet = file.active
                    i = 1
                    while True:
                        if sheet["A" + str(i)].value == str(id):
                            sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                            file.save("경고.xlsx")
                            if sheet["B" + str(i)].value >= 10:
                                await message.channel.send(
                                    "<@{}>\n경고를 총 10회 받으셨으므로, 서버에서 추방됩니다.".format(id))
                                await message.guild.ban(author)
                            else:
                                await message.channel.send(
                                    "<@{}>\n+ 경고 1회\n권한을 받으실 조건이 갖춰져 있지 않습니다.\n```yaml\n고유번호 | 닉네임 | 직업\n```\n```fix\n경고 10회 이상 추방 입니다.\n```".format(
                                        id))
                            break
                        elif sheet["A" + str(i)].value == None:
                            sheet["A" + str(i)].value = str(id)
                            sheet["B" + str(i)].value = 1
                            file.save("경고.xlsx")
                            await message.channel.send(
                                "<@{}>\n+ 경고 1회\n권한을 받으실 조건이 갖춰져 있지 않습니다.\n```yaml\n고유번호 | 닉네임 | 직업\n```\n```fix\n경고 10회 이상 추방 입니다.\n```".format(
                                    id))
                            break
                elif nick[1:2] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[2:3] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[3:4] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[4:5] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[5:6] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[6:7] == '|':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[1:2] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[2:3] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[3:4] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[4:5] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[5:6] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)
                elif nick[6:7] == 'ㅣ':
                    await message.channel.send(
                        "인증 성공 !\n<@{}>님 ! {} 서버에 오신걸 환영합니다 !!".format(id, servername))
                    author = message.author
                    role = discord.utils.get(message.guild.roles, name="💎국민💎")
                    await author.add_roles(role)

                else:
                    file = openpyxl.load_workbook("경고.xlsx")
                    sheet = file.active
                    i = 1
                    while True:
                        if sheet["A" + str(i)].value == str(id):
                            sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                            file.save("경고.xlsx")
                            if sheet["B" + str(i)].value >= 10:
                                await message.channel.send(
                                    "<@{}>\n경고를 총 10회 받으셨으므로, 서버에서 추방됩니다.".format(id))
                                await message.guild.ban(author)
                            else:
                                await message.channel.send(
                                    "<@{}>\n+ 경고 1회\n권한을 받으실 조건이 갖춰져 있지 않습니다.\n```yaml\n고유번호 | 닉네임 | 직업\n```\n```fix\n경고 10회 이상 추방 입니다.\n```".format(
                                        id))
                            break
                        elif sheet["A" + str(i)].value == None:
                            sheet["A" + str(i)].value = str(id)
                            sheet["B" + str(i)].value = 1
                            file.save("경고.xlsx")
                            await message.channel.send(
                                "<@{}>\n+ 경고 1회\n권한을 받으실 조건이 갖춰져 있지 않습니다.\n```yaml\n고유번호 | 닉네임 | 직업\n```\n```fix\n경고 10회 이상 추방 입니다.\n```".format(
                                    id))
                            break
            else:
                return None
        else:
            return None
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
