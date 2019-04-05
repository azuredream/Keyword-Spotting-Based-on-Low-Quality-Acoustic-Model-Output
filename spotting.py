import os
from xpinyin import Pinyin
from fuzzywuzzy import fuzz

class keywordSpoter(object):
	"""docstring for keywordSpoter"""
	def __init__(self, keywordlist,simithreshold = 78):
		super(keywordSpoter, self).__init__()
		self.keywordlist = keywordlist
		self.simithreshold = simithreshold
		self.Targetlist = []
		self.Targetdict = {}
		pin = Pinyin()
		for i in keywordlist:
			ipinyin = pin.get_pinyin(i,"")
			self.Targetlist.append(ipinyin)
			self.Targetdict[ipinyin] = i+";"

	def simi(self,a,b):
		return fuzz.ratio(a,b)

	def getWord(self,input):
		pin = Pinyin()
		a = pin.get_pinyin(input,"")
		result = ""
		for i in self.Targetlist:#对每个关键词
			windowwidth = len(i)#以目标词长度为窗口，遍历输入串
			j = 0
			preratio = 0#当相似度从阈值以上变化到阈值以下，记为一次命中
			ratio = 0
			while(j+windowwidth<=len(a)):
				preratio = ratio
				ratio = self.simi(a[j:j+windowwidth],i)
				#print(i+":"+a[j:j+windowwidth]+":"+str(ratio))
				if preratio>self.simithreshold and ratio<self.simithreshold:	
					#print(a[j-1:j+windowwidth-1],"simi",preratio)
					result+=self.Targetdict[i]#当相似度从阈值以上变化到阈值以下，记为一次命中，将它计入结果
				j+=1
			if ratio>self.simithreshold:#如果目标词在末尾，相似度不会回落，直接计入
				result+=self.Targetdict[i]
		return result


if __name__ == '__main__':
	while(True):
		ss = keywordSpoter(["你好","再见","没错"])
		inputstr = input("Intput your str:")
		print(ss.getWord(inputstr))
