import urllib
import re
import lib2to3


symbolfile = open("symbols.txt")

symbolslist = symbolfile.read()

num_lines = sum(1 for line in open('symbols.txt'))



array = []
j=0
while j<num_lines:
    b = symbolslist.split('\n')[j]
    array.append(b)
    j+=1

i=0

while i<num_lines:
    htmlfile = urllib.urlopen("http://www.marketwatch.com/investing/stock/" + array[i])
    htmltext = htmlfile.read()
    regex = '<p class="data bgLast">(.+?)</p>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "The stock" ,array[i], "has a price of: ", price[0]
    i+=1
