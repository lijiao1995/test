#coding=utf-8
import os
import shutil

fast_list = []
#ָ��·��
delpath = ["/home/riqqv3.2.4/IMPORTFILE/DT/DONE",
           "/home/riqqv3.2.4/IMPORTFILE/DT/DONEOLD",
		   "/home/riqqv3.2.4/IMPORTFILE/DT/DT",
		   "/home/riqqv3.2.4/IMPORTFILE/DT/DT_SLIP",
		   "/home/riqqv3.2.4/IMPORTFILE/DT/ERROR",
		   "/home/riqqv3.2.4/IMPORTFILE/OTT/DONE",
		   "/home/riqqv3.2.4/IMPORTFILE/OTT/DONEOLD",
		   "/home/riqqv3.2.4/IMPORTFILE/OTT/OTT",
		   "/home/riqqv3.2.4/IMPORTFILE/OTT/OTT_SLIP",
		   "/home/riqqv3.2.4/IMPORTFILE/SITEINFO",
		   "/home/riqqv3.2.4/INFO",
		   "/home/riqqv3.2.4/LOG"]
""""
keepfiles =["/home/riqqv3.2.4/IMPORTFILE/SITEINFO/cfg_grid50_10.csv",
			"/home/riqqv3.2.4/IMPORTFILE/SITEINFO/cfg_grid50.csv",
			"/home/riqqv3.2.4/IMPORTFILE/SITEINFO/tdlte_cell_import.csv",]
"""
for a in delpath:
	#��·���е��ļ����ļ�����ӵ��б���
	fast_list = os.listdir(a)
	for f in fast_list:
		#���ļ�ָ��Ϊ����·��
		filePath = os.path.join( a, f)
		#if filePath in keepfiles:
			#os.remove(filePath)
		if os.path.isfile(filePath):
			#�ж��Ƿ�Ϊ�ļ�
			os.remove(filePath)
			print filePath + " is removed!"
		elif os.path.isdir(filePath):
			#�ж��Ƿ�Ϊ�ļ���
			shutil.rmtree(filePath,True)
			print "dir: " + filePath +" is removed!"


