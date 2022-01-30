#!/usr/bin/python
# -*- coding: utf-8 -*-
#==================================
#
#	Media Circus version 3:
#	This program runs once a day at 0010 hrs.
#	It chooses ten headlines from tweets.txt and
#	compiles a list in dailytweets.txt that can be
#	accessed by any internet-enabled Media Circus
#
#   by Michael LeBlanc mleblanc@nscad.ca
#   August 2018
# 
#==================================


import sys, random, time


def main():

#	reset the current date
# 	f = open('date.txt', 'w')
# 	now = datetime.datetime.now()
# 	date = str(now.day)
# 	f.write(date)
# 	f.close()
	
#	get tweetindex, the line number where we start to retrieve our tweets from
#	the tweets.txt

	f = open('/home/pi/tweetindex.txt')
	tweetindex = int(f.read())
	f.close()
	
#		
	dailytweets = []
	limit = tweetindex + 10

#	get dailytweets from master list	
	f = open('/home/pi/tweets.txt')
	linenumber = 0
	
	for line in f:	
		linenumber = linenumber + 1	
		if (linenumber < tweetindex):
			pass
		elif (linenumber < limit):	
			line = line.replace('\n', '')
			line = line + ' . . . . . . ' 
			dailytweets = dailytweets + [line] 
			
	f.close()

#	print dailytweets
	
	
	
# 	convert dailytweets from a list to a single string with ellipses
	dailytweetsconverted = ' '.join(dailytweets)
	
	
	#print dailytweetsconverted		

#	save to file
	f = open('/var/www/html/mediacircus/dailytweets.txt', "w")
	f.write(str(dailytweets))
	f.close()
	
#	this file currently contains unwanted characters
	
#	prepare text for clean up	
	f = open('/var/www/html/mediacircus/dailytweets.txt')
	dailytweetsconverted = f.read()
	f.close()
	
	#	clean up text file:
	#	strip [' characters
	dailytweetsconverted = dailytweetsconverted.replace('[\'','')
	
	#	strip [" characters
	dailytweetsconverted = dailytweetsconverted.replace('[\"','')
	
	#	strip ', " characters
	dailytweetsconverted = dailytweetsconverted.replace('\', \"', '')
	
	#	strip ", ' characters
	dailytweetsconverted = dailytweetsconverted.replace('\", \'', '')
	
	#	strip ", " characters
	dailytweetsconverted = dailytweetsconverted.replace('\", \"', '')
	
	#	strip ', ' characters
	dailytweetsconverted = dailytweetsconverted.replace('\', \'', '')
	
	# 	strip '] characters
	dailytweetsconverted = dailytweetsconverted.replace('\']','')
	
	# 	strip "] characters
	dailytweetsconverted = dailytweetsconverted.replace('\"]','')
	

#	save the cleaned up text to file	
	f = open('/var/www/html/mediacircus/dailytweets.txt', "w")
	f.write(str(dailytweetsconverted))
	f.close()
	
#	increment the tweet index so that tomorrow a new tweet will display
#	the current limit is one more than the maximum lines in the file (minus ten)
	if (tweetindex == 1296):
		tweetindex = 1
	else:
		tweetindex = tweetindex + 1

# 	save to file
	f = open('/home/pi/tweetindex.txt', "w")
	newindex = str(tweetindex)
	f.write(newindex)
	f.close()
	

if __name__ == '__main__':
  main()
