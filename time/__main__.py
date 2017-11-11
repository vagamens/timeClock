import os
import sys
import datetime
from copy import deepcopy
from pprint import pprint

def calculate(filename):
	lines = []
	with open(filename, 'r') as f:
		read_data = f.read()
		lines = read_data.split('\n')
	lines.pop(-1)
	for i in range(len(lines)):
		lines[i] = lines[i].split(',')
	total = datetime.timedelta(0,0,0)
	while len(lines) > 1:
		if lines[0][-1] == 'in' and lines[1][-1] == 'out':
			line1 = deepcopy(lines[0])
			line2 = deepcopy(lines[1])
			line1[0] = line1[0].split('-')
			line1[1] = line1[1].split(':')
			line2[0] = line2[0].split('-')
			line2[1] = line2[1].split(':')
			d1 = datetime.datetime(int(line1[0][0]), int(line1[0][1]),
								   int(line1[0][2]), int(line1[1][0]),
								   int(line1[1][1]), int(line1[1][2]))
			d2 = datetime.datetime(int(line2[0][0]), int(line2[0][1]),
								   int(line2[0][2]), int(line2[1][0]),
								   int(line2[1][1]), int(line2[1][2]))
			total = total+(d2-d1)
		lines.pop(1)
		lines.pop(0)
	os.remove(filename)
	return total

def main(args):
	filename = 'time/workfile'

	if args[-1] == 'calc':
		print(calculate(filename))
	else:
		with open(filename, 'a') as f:
			curTime = str(datetime.datetime.now()).split('.')[0].split(' ')
			curTime.append(args[-1])
			print(curTime)
			f.write(','.join(curTime)+'\n')

if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		pass