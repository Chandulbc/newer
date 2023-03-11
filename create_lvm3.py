#!/bin/python3

import os
import subprocess as process

import time as t


#we can inherit the subprocess to use the classmethods
class create_lvm():
    def __init__(self):
       #here we can use env var to store and keep it permanently by
assigning to os.environ["DEBUSSY"]
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
                p=["pvcreate"]+self.temp
                process.run(p)


                self.phyvol=" ".join(self.temp)

        else:

            return False

        t.sleep(10)
        return True



    #create volumegroup
    def createvolgrp(self,vgcmd):
        self.vgcmd=vgcmd
        if len(self.vgcmd)>=2 and self.vgcmd[0]=="vgcreate":
            #volgrp name and vgcreate
            print("created volgrp")
            p2=["vgcreate"]+[self.vgcmd[1]]+self.phyvol.split()
            process.run(p2)


            self.logvol="/dev"+"/"+self.vgcmd[1]

            t.sleep(10)
            return True

        else:

            return False





    #create logicalvolume
    def createlogvol(self,lvcmd):
        self.lvcmd=lvcmd
        #--input=lvcreate,-n,lvname,-size,20G,vgname
        if len(self.lvcmd)>=5 and self.lvcmd[0]=="lvcreate":
          #either run or Popen we can use but subprocess.run only work after 3.0

              process.run(["lvcreate"]+[self.lvcmd[1].lower()]+[self.lvcmd[2]]+[self.lvcmd[3].upper()]+[self.lvcmd[4].upper()]+[self.lvcmd[5]])
              self.logvol+="/"+self.lvcmd[2]
              print("createdlogvol")

              t.sleep(10)
              return True
        else:

            return False

    #create filesystm
    def createfs(self,fsck):
        self.fsck=fsck
        if len(self.fsck)>=1 and self.fsck[0]=="mkfs":
            print("createdfs")
            process.run(["mkfs.xfs"]+[self.logvol])
            t.sleep(10)
            return True
        else:

            return False



    #create dir
    def createmkdir(self,dir):
        self.dir=dir
        if len(self.dir)>=1 :
           #print(f"created dir {self.dir[0]}")
            process.run(["mkdir"]+[self.dir[0]])
            t.sleep(10)
            return True
        else:
            return False

    #mount fs
    def mount(self,mnt):
        self.mnt=mnt
        if len(self.mnt)>=1 and self.mnt[0]=="mnt":
            print("mounted")
            process.run(["mount"]+[self.logvol]+[self.dir[0]])
            t.sleep(10)
            return True
        else:
            return False

    #unmount fs
    def unmount(self):

        #t.sleep(20)
        print("unmounted")
        t.sleep(20)
        process.run(["umount"]+[self.dir[0]])
        return True
