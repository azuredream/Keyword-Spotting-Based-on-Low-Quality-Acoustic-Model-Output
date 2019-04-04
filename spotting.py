import os
from xpinyin import Pinyin
from fuzzywuzzy import fuzz

simithreshold = 78 #%
#您好请稍等；再见；请交费
Targetlist = ["ninhaoqingshaodeng","zaijian","qingjiaofei"]
Targetdict = {"ninhaoqingshaodeng":"您好请稍等;","zaijian":"再见;""qingjiaofei":"请交费;"}




def simi(a,b):
	return fuzz.ratio(a,b)

def getWord(input):
	pin = Pinyin()
	a = pin.get_pinyin(input,"")

	result = ""
	#cursimi = 0
	for i in Targetlist:#对每个关键词
		windowwidth = len(i)#以目标词长度为窗口，遍历输入串
		j = 0
		preratio = 0#当相似度从阈值以上变化到阈值以下，记为一次命中
		ratio = 0
		while(j+windowwidth<=len(a)):
			preratio = ratio
			ratio = simi(a[j:j+windowwidth],i)
			#print(i+":"+a[j:j+windowwidth]+":"+str(ratio))
			if preratio>simithreshold and ratio<simithreshold:	
				#print(a[j-1:j+windowwidth-1],"simi",preratio)
				result+=Targetdict[i]#当相似度从阈值以上变化到阈值以下，记为一次命中，将它计入结果
			j+=1
		if ratio>simithreshold:#如果目标词在末尾，相似度不会回落，直接计入
			result+=Targetdict[i]
		#ratio = simi(a,i)
		#if ratio>simithreshold and ratio>cursimi:
		#	cursimi = simi(a,i)
		#	result = i
	#print("simi:",cursimi)
	return result
