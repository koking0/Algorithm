from datetime import datetime

time_list = []

with open("records.txt", 'r') as fp:
    for line in fp.readlines():
        line = line.strip()
        print(line)
        tiem_item = datetime.strptime(line, "%Y-%m-%d %H:%M:%S")
        print(tiem_item)
        time_list.append(tiem_item)
