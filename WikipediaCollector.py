from numpy import result_type
import wikipedia
import re
import numpy
import os

def WikiSearch(search):
    return wikipedia.search(search)
def ContentSearch(WikiSearch):
    if len(WikiSearch) > 1:
        print(WikiSearch,'\n')
        tmp = input("Which one are you looking for?\n")
        return wikipedia.page(WikiSearch[int(tmp)]).content
    else: 
        return wikipedia.page(WikiSearch).content

def PageTitle(search):
    if len(search) > 1:
        print(search,'\n')
        tmp = input("Which one are you looking for?\n")
        return wikipedia.page(search[int(tmp)]).title
    else: 
        return wikipedia.page(search).title
    
def SaveContent(content,title):
    SavePath = 'C:/Users/ThaDemonReaper/Desktop/Complete Code/Logic/Wikipedia Data' 
    with open(str(title)+'.txt','w', encoding='utf-8') as f:
            f.write(content)
            os.path.join(SavePath,str(f))
    print('done')


SaveContent(ContentSearch(WikiSearch('Nikola Tesla')),PageTitle(WikiSearch('Nikola Tesla')))