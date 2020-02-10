import re, requests, sys
from collections import Counter
from tqdm.auto import tqdm

def getYtbers(num):
	youtubeList = []
	pattern = re.compile(r'/user/\w+')
	for loop in tqdm(range(num)):
		website = requests.get("https://www.youtube.com/").text
		matches = pattern.findall(website)
		for i in matches:
			youtubeList.append(i.replace("/user/",''))
	return Counter(youtubeList)

def logData(dictYtb):
	data = ""
	logFile = open('log.txt','w')
	num = 1
	for key, value in dictYtb.items():
		print(num)
		print(key + " " + str(value) + "\n")
		logFile.write(key + ":" + str(value) + "\n")
		num+=1
	logFile.close()

def main(num):
	dictYtb = getYtbers(num)
	logData(dictYtb)

	


num = int(sys.argv[1])

main(num)


