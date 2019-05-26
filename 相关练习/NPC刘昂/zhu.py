from NPC import NPC
from player import player
player1=player({})
NPC1=NPC('阿尔萨斯','   使用霜之哀伤的怒火攻击敌人','1')
NPC2=NPC('吉安娜','   使用奥数法术攻击敌人','2')
NPC3=NPC('乌塞尔','   使用圣光的力量治愈盟友','3')
while True:
    NPC.show()
    player1.showdangqian()
    c=input('请选择你要继续的操作：'
          '1. 邀请组队 '
          '2. 踢出队伍 '
          '0. 完成 \n'
          '')
    if c=='1':
        b=input('请选择可选NPC中要组队的NPC的ID\n')
        if b=='1':
            player1.addNPC(b)
        if b=='2':
            player1.addNPC(b)
        if b=='3':
            player1.addNPC(b)
    if c=='2':
        b = input('请选择可选NPC中要踢出的NPC的ID\n')
        if b == '1':
            player1.removeNPC(b)
        if b == '2':
            player1.removeNPC(b)
        if b == '3':
            player1.removeNPC(b)
    if c=='0':
        break



