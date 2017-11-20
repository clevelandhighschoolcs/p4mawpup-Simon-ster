from HTMLParser import HTMLParser
import urllib2
import time
from collections import Counter
import re

Url = raw_input("What is the URL of the website you want to check? :" + '\n')
while True:
    try:
        Time = int(raw_input("What amount of time would you like to let pass between checking the website against itself:  " + '\n'))
        break
    except ValueError:
        print("Not a valid number")

webUrl = urllib2.urlopen(Url)
data = webUrl.read()
starttag_list = []
data_list = []
starttag_list2 = []
data_list2 = []

def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

def change():
    print "There was a change"
    result = raw_input("Would you like to know more about the change?")
    if result.lower == 'yes' or 'y':
        findoutmore()
        
def nochange():
    print "There was no change, but that's okay Simon, you'll get it to work"
    print "End of code"

def findoutmore():
    answer = raw_input("Would you like to know about \'start tags\', \'data\', or \'different words\'?")
    if answer == 'start tags':
        print "Start tags changed %s times" %abs(stl2 - stl)
        findoutmore()
    elif answer == 'data':
        print "Data changed %d times" %abs(dl2-dl)
        findoutmore()
    elif answer == 'different words':
        print "Here is a list of the words and code that was different and the different number of times it appeared:"
        print returnNotMatches(Test1, Test2)
        findoutmore()
    else:
        leave = raw_input("Would you like to exit?")
        if leave.lower == 'yes' or 'y':
            print "End of code"
        else:
            findoutmore()
class MyHTMLParser(HTMLParser):

    def handle_starttag(self,tag,attrs):
#       print "Encountered a start tag:", tag
        starttag_list.append(tag)

    def handle_data(self,data):
#       print "Encountered some data :", data
        data_list.append(data)
    
class MyHTMLParser2(HTMLParser):

    def handle_starttag2(self,tag,attrs):
#       print "Encountered a start tag:", tag
        starttag_list2.append(tag)
    
    def handle_data2(self,data):
#       print "Encountered some data :", data
        data_list2.append(data)
    

parser = MyHTMLParser()
parser.feed(data)
words1 = re.findall(r'\w+', data.lower())
Test1 = Counter(words1)
stl = len(starttag_list)
dl = len(data_list)

time.sleep(Time)

webUrl2 = urllib2.urlopen(Url)
data2 = webUrl2.read()

parser2 = MyHTMLParser2()
parser2.feed(data2)
words2 = re.findall(r'\w+', data2.lower())
Test2 = Counter(words2)
stl2 = len(starttag_list2)
dl2 = len(data_list2)


if Test1 == Test2:
    nochange()
else:
    change()

               
