import os 
import subprocess as process




#we can inherit the subprocess to use the classmethods
class create_lvm():
    def __init__(self):
       #here we can use env var to store and keep it permanently by assigning to os.environ["DEBUSSY"]
       self.phyvol=[]
       self.volgrp=[]
       self.logvol=[]

     #create physical vol"
    def createphyvol(self,pvcmd):
            
        self.pvcmd=pvcmd
        if len(self.pvcmd)>1 and self.pvcmd[0]=="pvcreate":
            
                #we can use process.run() or process.Popen() or os.system() to create physcialvolume
                self.temp=[]
                for i in self.pvcmd[1:]:
                        self.temp+=[i]
                
                process.run(["pvcreate"]+[self.temp],shell=True)
                self.phyvol.append(self.temp[0])
               
                
        else:
            return False
       
        return True



    #create volumegroup
    def createvolgrp(self,vgcmd):
        self.vgcmd=vgcmd
        if len(self.vgcmd)>2 and self.vgcmd[0]=="vgcreate":
            self.append=[]
            for i in self.vgcmd[2:]:
                self.append+=[i]
            
          
            process.run("vgcreate "+self.vgcmd+" ".join(self.append))
            
            self.volgrp.append(self.vgcmd[1])
            self.logvol+=["/dev"]+[self.vgcmd[1]]
          
        
            return True

        else:
            return False





    #create logicalvolume
    def createlogvol(self,lvcmd):
        self.lvcmd=lvcmd
        #--input=lvcreate,-n,lvname,-size,20G,vgname
        if len(self.lvcmd)>5 and self.lvcmd[0]=="lvcreate":
          #either run or Popen we can use but subprocess.run only work after 3.0
          try:
            process.run(["lvcreate",self.lvcmd[1],self.lvcmd[2],self.lvcmd[3],self.lvcmd[4],self.lvcmd[5]])
            self.logvol+=[self.lvcmd[2]]
            return True
          except:
              os.system(["lvcreate",self.lvcmd[1],self.lvcmd[2],self.lvcmd[3],self.lvcmd[4],self.lvcmd[5]])
              self.logvol+=[self.lvcmd[2]]
              return True
        else:
            return False

    #create filesystm
    def createfs(self,fsck):
        self.fsck=fsck
        if len(self.fsck)>1 and self.fsck[0]=="mkfs":
            process.run(["mkfs."+self.fsck[1],self.logvol])  
            return True
        else:
            return False



    #create dir
    def createmkdir(self,dir):
        self.dir=dir
        if len(self.dir)>=1:
            process.run(["mkdir",self.dir])
            
            return True
        else:
            return False

    #mount fs
    def mount(self,mnt):
        self.mnt=mnt
        if len(self.mnt)>=1:
            process.run(["mount",self.logvol,self.mnt])
            return True
        else:
            return False

    #unmount fs
    def unmount(self):
       
        process.run(["umount",self.mnt])
        return True


