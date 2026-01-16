with open ("scanreport.txt","r") as file:
	lines = f.readlines()

words =["Nothing","not here","decoy","Empty","Wrong","Try","Still","Continue","inside"]
with open("cleanReport.txt","w") as f:
	for line in lines:
		if word in words not in line :
			f.write(line)
