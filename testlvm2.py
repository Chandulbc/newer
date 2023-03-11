#!/bin/python3

import unittest as unit
import argparse
import sys
import create_lvm as lv



'''
  logical volume management -
                              1. attach device to virtualbox
                              2. give file level permissions because
every thing linux is file and folder
                              3. create partition to it by giving the
commands of n new partition, p print partition list, t change type of
Id then
                              hexcode 8e to Id then w write all changes
                              then use the code to automate and create
the lvm, shrirk and increase the size
                              by giving the following format
                                python testfilename.py
--input1=pvcreate,/dev/sdb --input2=vgcreate,vgname,/dev/sdb .....

'''
class TestLvm(unit.TestCase):

    #partition to physcial
    def test_A(self):

         #provide input in the format of --input1=pvcreate,/dev/sda
         self.assertTrue(call.createphyvol(takeinputs.input1.split(",")))



    #physcial to volgrop
    def test_B(self):

         self.assertTrue(call.createvolgrp(takeinputs.input2.split(",")))



    #volgroup to logvol
    def test_C(self):


        self.assertTrue(call.createlogvol(takeinputs.input3.split(",")))


    #make mkfs.xfs
    def test_D(self):


        self.assertTrue(call.createfs(takeinputs.input4.split(",")))
    #mkdir dir
    def test_E(self):


        self.assertTrue(call.createmkdir(takeinputs.input5.split(",")))

    #mount point
    def test_F(self):

        self.assertTrue(call.mount(takeinputs.input6.split(",")))

    #unmount from point
    def test_G(self):
       self.assertTrue(call.unmount())





if __name__=="__main__":
    temp=argparse.ArgumentParser()
    #partition to physcial
    temp.add_argument("--input1",default="My Input")
    #physcial to volgrop
    temp.add_argument("--input2",default="My Input")
    #volgroup to logvol
    temp.add_argument("--input3",default="My Input")
    #make mkfs.xfs
    temp.add_argument("--input4",default="My Input")
    #mkdir dir
    temp.add_argument("--input5",default="My Input")
    #mount point
    temp.add_argument("--input6",default="My Input")

    temp.add_argument("unittest_args",nargs="*")
    takeinputs=temp.parse_args()
    call=lv.create_lvm()
    print(takeinputs.input1.split(","),takeinputs.input2.split(","),takeinputs.input3.split(","),takeinputs.input4.split(","),takeinputs.input5.split(","),takeinputs.input6.split(","))
    unit.main(argv=sys.argv[:1])

