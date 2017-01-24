import difflib
from datetime import datetime
import time
while True:
	f=open('host0','r')  #open a file
	f1=open('host1','r') #open another file to compare
	str1=f.read()
	str2=f1.read()
	str1=str1.split()  #split the words in file by default through the spce
	str2=str2.split()
	d=difflib.Differ()     # compare and just print
	diff=list(d.compare(str2,str1))
	#print '\n'.join(diff)
	f2=open('diff','a')
	f2.write('\n')
	t= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	f2.write(time.ctime())
	print("Difference at ", time.ctime())
	f2.write('\n')
	f2.write('\n'.join(diff))
	f2.write('\n')
	time.sleep(1800)
