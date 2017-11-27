from HTMLParser import HTMLParser
import urllib2
import time
from collections import Counter
import re


#get url
Url = raw_input("What is the URL of the website you want to check? :" + '\n')

#get time
while True:
#make sure 'time' is a number
    try:
        Time = int(raw_input("What amount of seconds would you like to let pass between checking the website against itself: " + '\n'))
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
    if result.lower() == 'yes' or result.lower() =='y':
        findoutmore()
    else:
        print "End of code"
         
        
def nochange():
    print "The website didn't change, but that's okay. Some things aren't as ready for change as others." + '\n' + "Who are we to tell them otherwise?"
    print "End of code"

    
    
def findoutmore():
    answer = raw_input("Which would you like to know about: \'start tags\', \'data\', or \'different words\'?")
#start tags
    if answer.lower() == 'start tags':
        print "Start tags changed %s times" %abs(stl2 - stl)
        findoutmore()
#data
    elif answer.lower() == 'data':
        print "Data changed %d times" %abs(dl2-dl)
        findoutmore()
#different words
    elif answer.lower() == 'different words':
        print "Here is a list of words and hex code that changed and the different number of instances it appeared:"
        print returnNotMatches(Test1, Test2)
        findoutmore()
#other
    else:
        leave = raw_input("Would you like to exit?")
        if leave.lower() == 'yes' or leave.lower() == 'y':
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


#feed the parser
parser = MyHTMLParser()
parser.feed(data)

#count up words
words1 = re.findall(r'\w+', data.lower())
Test1 = Counter(words1)

#number of words in array
stl = len(starttag_list)
dl = len(data_list)

#pause
time.sleep(Time)

#reread data after pause
webUrl2 = urllib2.urlopen(Url)
data2 = webUrl2.read()

#feed the parser a second time
parser2 = MyHTMLParser2()
parser2.feed(data2)

#count up words
words2 = re.findall(r'\w+', data2.lower())
Test2 = Counter(words2)

#number of words in array
stl2 = len(starttag_list2)
dl2 = len(data_list2)

#test change
if Test1 == Test2:
    nochange()
else:
    change()

