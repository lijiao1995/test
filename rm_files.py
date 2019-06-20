#coding=utf-8
import os
import shutil

fast_list = []
#指定路径
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
	#将路径中的文件或文件夹添加到列表中
	fast_list = os.listdir(a)
	for f in fast_list:
		#将文件指定为绝对路径
		filePath = os.path.join( a, f)
		#if filePath in keepfiles:
			#os.remove(filePath)
		if os.path.isfile(filePath):
			#判断是否为文件
			os.remove(filePath)
			print filePath + " is removed!"
		elif os.path.isdir(filePath):
			#判断是否为文件夹
			shutil.rmtree(filePath,True)
			print "dir: " + filePath +" is removed!"


