with open("scanreport.txt", "r") as file:
    lines = file.readlines()

words = ["Nothing", "Not here", "Keep","","decoy", "Empty", "Wrong", "Try", "Still", "Continue", "inside"]

with open("cleanReport.txt", "w") as f:
    for line in lines:
        if not any(word in line for word in words):
            f.write(line)
