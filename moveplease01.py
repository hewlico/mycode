#!/usr/in/env python3
import shutil
import os 

#Program renames and move raynor.obj to /ceph_storage
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj','ceph_storage/')

xname = input('What is the new name for Kerrigan.obj?')
shutil.move('ceph_storage/kerrigan.obj','ceph_storage/' + xname) 
