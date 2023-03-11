#!/bin/python

import os
import subprocess as process

import time as t


#we can inherit the subprocess to use the classmethods
class create_lvm():
    def __init__(self):
       #here we can use env var to store and keep it permanently by assigning to os.environ["DEBUSSY"]=20
       #we can used to run the code with subprocess.run() it will run all the subprocess, so we get crash inbetween the testcases 
       self.phyvol=" "
       self.volgrp=" "
       self.logvol=" "

     #create physical vol"
    def createphyvol(self,pvcmd):

        self.pvcmd=pvcmd
        if len(self.pvcmd)>1 and self.pvcmd[0]=="pvcreate":

                #we can use process.run() or process.Popen() or
os.system() to create physcialvolume
                self.temp=[]
                for i in self.pvcmd[1:]:
                        self.temp.append(i)
                print("created physicalvol")
                os.system("pvcreate "+" ".join(self.temp))
                self.phyvol=" ".join(self.temp)

        else:

            return False

        return True



    #create volumegroup
    def createvolgrp(self,vgcmd):
        self.vgcmd=vgcmd
        if len(self.vgcmd)>=2 and self.vgcmd[0]=="vgcreate":
            #volgrp name and vgcreate
            print("created volgrp")
            os.system("vgcreate "+" "+self.vgcmd[1]+" "+self.phyvol)


            self.logvol="/dev"+"/"+self.vgcmd[1]


            return True

        else:

            return False





    #create logicalvolume
    def createlogvol(self,lvcmd):
        self.lvcmd=lvcmd
        #--input=lvcreate,-n,lvname,-size,20G,vgname
        if len(self.lvcmd)>=5 and self.lvcmd[0]=="lvcreate":
          #either run or Popen we can use but subprocess.run only work after 3.0

              os.system("lvcreate "+" "+self.lvcmd[1].lower()+"
"+self.lvcmd[2]+" "+self.lvcmd[3].upper()+" "+self.lvcmd[4].upper()+"
"+self.lvcmd[5])
              self.logvol+="/"+self.lvcmd[2]
              print("createdlogvol")
              return True
        else:

            return False

    #create filesystm
    def createfs(self,fsck):
        self.fsck=fsck
        if len(self.fsck)>=1 and self.fsck[0]=="mkfs":
            print("createdfs")
            os.system("mkfs.xfs "+" "+self.logvol)
            return True
        else:

            return False



    #create dir
    def createmkdir(self,dir):
        self.dir=dir
        if len(self.dir)>=1:
            print(f"created dir {self.dir[0]}")
            os.system("mkdir "+" "+self.dir[0])

            return True
        else:
            return False

    #mount fs
    def mount(self,mnt):
        self.mnt=mnt
        if len(self.mnt)>=1 and self.mnt[0]=="mnt":
            print("mounted")
            os.system("mount "+" "+self.logvol+" "+self.dir[0])
            return True
        else:
            return False

    #unmount fs
    def unmount(self):

        t.sleep(20)
        print("unmounted")
        os.system("umount "+self.dir[0])
        return True
