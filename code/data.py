# coding: utf-8
import bs4
get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup
get_ipython().run_line_magic('cd', 'Documents/proust/')
soup = BeautifulSoup('A\ LA\ RECHERCHE\ DU\ TEMPS\ PERDU\ -\ Marcel\ Proust\ -\ Texte\ intégral\ en\ une\ seule\ page\ Web.html')
text = soup.get_text()
len(text)
text
soup
head data.html
get_ipython().system('head data.html')
print(soup.prettify())
soup = BeautifulSoup('data.html', 'html.parser')
print(soup.prettify())
get_ipython().run_line_magic('ls', '')
with open('data.html', 'rt') as file:
    soup = BeautifulSoup(file)
    
text = soup.get_text()
len(text)
with open('data.txt','wt') as file:
    file.write(text)
    
get_ipython().system('head data.txt')
get_ipython().system('head -n 100 data.txt')
len(text.split('\n'))
len(text.split('\n\n'))
paragraphs = text.split('\n')
paragraphs[3:6]
paragraphs[10:15]
get_ipython().system('ls -lh data.txt')
len(text)
paragraphs = text.split('\n\n')
paragraphs[0][:100]
paragraphs[1][:100]
for p in paragraphs:
    print(p[:100])
    
for p in paragraphs:
    print(p[:100], '\n\n+++++++++++++++\n\n')
    
    
soup.find_all('div')
sections = soup.find_all('div')
len(sections)
sections[0]
section_text = sections[0].get_text()
section_text[:100]
section_text[-100:]
len(section_text)
sections = soup.find_all(class="views-row")
import re
re.find('\d\d\d', text)
re.search('\d\d\d', text)
match = re.search('\d\d\d', text)
text[match]
text[match.start: match.end+100]
text[match.start(): match.end()+100]
matches = re.findall(r'\b\d\d\d\b', text)
len(matches)
matches[0]
sections = re.split(r'\b\d\d\d\b', text)
len(sections)
sections[0]
sections[1]
len(sections)
len(sections[1])
import numpy as np
import pandas as pd
pd.DataFrame([len(s) for s in sections]).describe()
[len(s) for s in sections]
get_ipython().system('mkdir sections')
for i, section in enumerate(sections):
    break
    with open(f'sections/{i:03d}.txt', 'wt') as file:
        file.write(section)
        
print(f'sections/{i:03d}.txt')
for i, section in enumerate(sections):
#    break
    with open(f'sections/{i:03d}.txt', 'wt') as file:
        file.write(section)
        
get_ipython().run_line_magic('ls', 'sections')
get_ipython().run_line_magic('save', 'data.py')
get_ipython().run_line_magic('save', 'data.py ~0/')
