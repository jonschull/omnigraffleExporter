#onchange.py
def between(s,first,second):
	if s.find(first) > -1:
		return (s.split(first)[1].split(second)[0])

def do(cmd='ls'):
	print 'DOING ', cmd
	from os import popen3
	pIn,pOut,pErr=0,1,2
	popenResults=popen3(cmd)  #showTheImage: I was running this twice
	pOut=popenResults[pOut].read()
	pErr=popenResults[pErr].read()
	print pErr,pOut
	return pOut


def giveClue():
	print "You haven't asked me to do anything.  Here's an example:"
	print """python onchange.py "ls -l" FileToWatch.txt FileToWatch2.txt"""
	print """So, when FileToWatch.txt changes, it will be passed to the command "ls-l". """


mTimes={} 			    #global dict of modification times.  (a purist would make havechanged a class with a persistent variable)
oldmTimes={}			 
from os.path import getmtime #modification time

def haveChanged(filenames):

	changed=[]
	for fn in filenames:
		if not mTimes.has_key(fn):  
			mTimes[fn] = oldmTimes[fn] = 1 #initialize  

		oldmTimes[fn], mTimes[fn]= mTimes[fn], getmtime(fn)
		if mTimes[fn]<>oldmTimes[fn]:
			changed.append(fn)
	return changed


if __name__=='__main__':
	"""from user import * # overkill
	try:   overkill
		callme('/Users/jis/python/onchange.py') 
	except:
		pass
	"""	
	from sys import argv
	from string import join
	params=argv[1:]  #omit python...
	allparams=join(params)
	filenames=Executor=None

	if not params: giveClue()
	else:
		Executor=between(allparams, '"','"')
		if not Executor: Executor=params[0]
		try: filenames=allparams.split(Executor,1)[1].split()
		except: pass
		print 'EXECUTOR =', Executor
		print 'FILENAMES=', filenames
	
	if not filenames: print "\nBUT YOU HAVEN'T TOLD ME WHAT FILES TO WATCH" #and exit
	else:
		from time import sleep
		while 1:
			for fn in haveChanged(filenames):
				do(Executor + ' ' + fn)
			sleep(1)
	

		
	
