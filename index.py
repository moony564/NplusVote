from cgitb import text
from optparse import Option
from nextcord import Interaction, ButtonStyle, Member, Embed, Colour
from nextcord.ext import commands
from nextcord.ui import Button, View
import nextcord
import os

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('봇 시작')
    await client.change_presence(activity=nextcord.Game(name= "`/명령어` 입력하기"))



@client.slash_command(description="명령어 종류 확인하기", )
async def 명령어(inter:Interaction):
    helpEmbed = Embed(title="명령어 종류", description="명령어 모음.")
    helpEmbed.add_field(name="익명투표용버튼", value="2개의 선택지로 투표를 할수있습니다.(중복불가)")
    helpEmbed.add_field(name="버튼", value="2개의 버튼(내용은 자유)을 만들고 그에대한 답을 설정가능합니다.", inline=True)
    helpEmbed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/990566114587201607/1051808651221934120/-001.png')
    await inter.send(embed=helpEmbed, ephemeral=True)


# @client.slash_command(description="메시지 입력을 받음", )
# async def 테스트(inter:Interaction, 메시지:str):
#     await inter.response.send_message(f"입력받은 메시지 : \" {메시지} \"")

# @client.slash_command(description="메시지 입력을 받음",)
# async def 상메변경(inter:Interaction, 메시지:str):
#     if inter.user.id == 491511126379593738:
#         await client.change_presence(activity=nextcord.Game(name= f"{메시지}"))
#         await inter.response.send_message(f"변경됨\n변경된 메시지 : \" {메시지} \"")

# @client.slash_command(description="유저 호출", )
# async def 유저호출(inter:Interaction, 메시지, 유저아이디:Member):
#     await inter.response.send_message(f"<@{유저아이디.id}> 님\n\" {메시지} \" 이라고 전해달라네요!")


@client.slash_command(description="버튼", )
async def 버튼(inter:Interaction, 입력문구1, 입력문구2, 입력문구3, 답장1, 답장2, 사진링크_없으면0이라고):
    yes = Button(label=f"{입력문구2}", style=ButtonStyle.green)
    yesno = Button(label=f"{입력문구3}", style=ButtonStyle.danger)

    async def yes1_Click(interaction):
        await interaction.response.send_message(f"{답장1}")

    async def yes2_Click(interaction):
        await interaction.response.send_message(f"{답장2}")

    yes.callback = yes1_Click
    yesno.callback = yes2_Click

    myview = View(timeout=10000000000000000000*1230123123021434923592340324)
    myview.add_item(yes)
    myview.add_item(yesno)

    embed1 = Embed(title=f"{입력문구1}", colour=Colour.green())
    if 사진링크_없으면0이라고 != "0":
        embed1.set_thumbnail(url= f'{사진링크_없으면0이라고}')

    await inter.response.send_message(embed=embed1, view=myview)

# @client.command()
# async def 안녕(inter):
#     await inter.send('응! 안녕!')

@client.slash_command(description="버튼", )
async def 익명투표용버튼(inter:Interaction, 제목, 버튼1, 버튼2, 사진링크_없으면0이라고):
    yes = Button(label=f"{버튼1}", style=ButtonStyle.green)
    yesno = Button(label=f"{버튼2}", style=ButtonStyle.danger)
    

    기회 = [1,2,3]
    async def yes1_Click(interaction):
        if interaction.user.id not in 기회:
            기회.append(interaction.user.id)
            await interaction.response.send_message(f"{버튼1}한명 추가")
        elif interaction.user.id in 기회:
            await interaction.response.send_message(f"당신은 이미 투표를 했습니다.", ephemeral=True)
    async def yes2_Click(interaction):
        if interaction.user.id not in 기회:
            기회.append(interaction.user.id)
            await interaction.response.send_message(f"{버튼2}한명 추가")
        elif interaction.user.id in 기회:
            await interaction.response.send_message(f"당신은 이미 투표를 했습니다.", ephemeral=True)
    

    yes.callback = yes1_Click
    yesno.callback = yes2_Click

    myview = View(timeout=10000000000000000000*1230123123021434923592340324)
    myview.add_item(yes)
    myview.add_item(yesno)

    embed1 = Embed(title=f"{제목}", colour=Colour.green())
    if 사진링크_없으면0이라고 != "0":
        embed1.set_thumbnail(url= f'{사진링크_없으면0이라고}')

    await inter.response.send_message(embed=embed1, view=myview)


ac_tk = os.environ["B_TK"]
client.run(ac_tk)