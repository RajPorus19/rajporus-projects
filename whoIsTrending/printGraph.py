import matplotlib.pyplot as plt 

youtubers = []
vidNum = []

with open("log.txt") as logFile:
	lines = logFile.readlines()
	others = 0
	for line in lines:
		if int(line.replace("\n","").split(":")[1]) <= 2:
			others += 1
		else :
			youtubers.append(line.replace("\n","").split(":")[0])
			vidNum.append(int(line.replace("\n","").split(":")[1]))

	youtubers.append("Other irrelevant youtubers")
	vidNum.append(others)



plt.pie(vidNum, labels = youtubers)


plt.show()