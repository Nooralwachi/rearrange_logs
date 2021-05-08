from collections import defaultdict
def rearrange_logs(filename,logs):
	with open(filename, 'r') as file,open('get_log.txt', 'w') as fget,open('set_log.txt', 'w') as fset, open('add_log.txt', 'w') as fadd  :
		for line in file:
			items = line.split()
			func,date = items[2],items[1]
			if func == 'Get':
				fget.write(line)
				logs['Get'][date] +=1
			elif func =='Set':
				fset.write(line)
				logs['Set'][date] +=1
			elif func == 'Add':
				fadd.write(line)
				logs['Add'][date] +=1
def logs(files):
	get_d,set_d,add_d=defaultdict(int),defaultdict(int),defaultdict(int)	
	logs= {'Get': get_d , 'Set': set_d, 'Add': add_d}
	for item in files:
		rearrange_logs(item, logs)
	with open('stats_log.txt', 'w') as fstatus:
		for stats,dic in logs.items():
			fstatus.write(stats + '\n')
			for date,count in dic.items():
				fstatus.write(str(date) + ' ' +str(count) + '\n')
logs(['log1.txt', 'log2.txt', 'log3.txt'])