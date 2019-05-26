from NPC import NPC
class player:
    def __init__(self,dangqian):
        self.dangqian=dangqian
    def addNPC(self,id):
        for x in NPC.NPClist:
            if id==x:
                self.dangqian[x]=NPC.NPClist[x]
    def removeNPC(self,id):
        self.dangqian.pop(id)
    def showdangqian(self):
        print('当前NPC队伍共%d人，如下：'%(len(self.dangqian)))
        for x,y in self.dangqian.items():
            print(x,y)



