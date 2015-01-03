import itertools
import re
import requests


poorrichardsurl = 'https://archive.org/stream/poorrichardsalma00franrich/poorrichardsalma00franrich_djvu.txt'

def getpoorrichardstext():
    '''return a generator over all proverbs'''
    return requests.get(poorrichardsurl).text

def cleanpoorrichardstext(text):
    '''given poor richards text, clean it'''
    text = itertools.dropwhile(lambda x: not x.startswith('1.'), text.splitlines())
    text = itertools.takewhile(lambda x: not x.startswith('A star preced'), text)
    text = itertools.ifilter(lambda x: 'POOR RICHARD\'S ALMANACK' not in x, text)
    text = itertools.imap(lambda x: x.lstrip('\'"'), text)
    text = itertools.imap(lambda x: x.replace('1 /.', '177.'), text)
    text = itertools.imap(lambda x: x.replace('7*', '7.*'), text)
    return '\n'.join(text) 

def findpoorrichardsproverbs(text):
    '''given poor richard's text, find all proverbs'''
    found = re.findall(r'\n(\d+\.)(.*?)(?=(\n\d|\Z))', text, re.DOTALL)
    foundlist = [list(i) for i in found]
    for i, prov in enumerate(found):
        i_0 = float(prov[0])  
        if i < len(found) - 1 and i_0 + 1 != float(found[i + 1][0]):
            if float(found[i-1][0]) + 2 == float(found[i+1][0]):
                foundlist[i][0] = str(int(float(found[i-1][0])+1)) + '.'
    return foundlist

def cleanproverbs(textlist):
    '''given textlist, delete newlines, remove dashes'''
    

def getproverbs():
    text = getpoorrichardstext()
    text = cleanpoorrichardstext(text)
    return findpoorrichardsproverbs(text)


def main():
    proverbs = getproverbs()
    #for proverb in proverbs:
        #print proverb
    return proverbs

if __name__ == '__main__':
    l = main()
    last = None
    #print cleanpoorrichardstext(getpoorrichardstext())[:100]
    for i in l:
        if last is not None:
            if float(last) + 1 != float(i[0]):
                print last, i[0]
        last = i[0]
