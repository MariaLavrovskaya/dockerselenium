import csv
from subprocess import Popen



processes = []

with open('../file.csv', newline='') as f:
    reader = csv.reader(f)
    messages = list(reader)

for i in range(0, len(messages), 6):
    chrome_cmd = 'export BROWSER=chrome && python /Users/maria/Desktop/dockerselenium/main/test2.py'
    print(messages[i])
    processes.append(Popen(chrome_cmd, shell=True))

print(processes)









