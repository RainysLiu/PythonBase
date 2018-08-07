class NPC(object):
    NPClist = {}
    def __init__(self,name,info,id):
        self.name=name
        self.info=info
        self.id=id
        NPC.NPClist[self.id]=self.name+self.info
    @classmethod
    def show(self):
        print('可选NPC：')
        for x, y in NPC.NPClist.items():
            print(x, y)
