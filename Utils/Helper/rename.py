#�޸��ļ���
#coding=gbk
import os
import sys


path = os.getcwd()
#filename = 'ImageSet'
filename = 'Annotations'
filepath = os.path.join(path,filename)
filelist = os.listdir(filepath)
for i in range(len(filelist)):
    name = filelist[i]
    Olddir=os.path.join(filepath,name)
    name = name.replace('Jan','1')  #�ı��ַ�����ָ�����ַ�
    name = name[:16]+name[19:]  #�ַ�����Ƭ
    Newdir=os.path.join(filepath,name)
    os.rename(Olddir,Newdir)   #�޸��ļ���