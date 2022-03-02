# coding: utf-8
import spacy
from spacy import displacy
from tqdm import tqdm
from pathlib import Path

model = spacy.load('fr_core_news_lg')
with open('data/sections/003.txt','rt') as file:
    text = file.read()
    
len(text)
doc = model(text)
len(doc)
len(doc.ents)

html = displacy.render(doc, style="ent", page=True)
len(html)
with open('data/sections/003.html', 'wt') as file:
    file.write(html)
    
get_ipython().system('realpath data/sections/003.html')
doc.ents
from collections import Counter
Counter(doc.ents.most_common(30))
Counter(doc.ents).most_common(30)
Counter(list(doc.ents)).most_common(30)
doc.ents[0]
Counter(['Combray','Combray'])
list(doc.ents)
type(doc.ents[0])
type(doc.ents[0].text)
type(doc.ents[0].lower)
doc.ents[0].text
lower(doc.ents[0].text)
doc.ents[0].text.lower()
Counter([e.text.lower() for e in doc.ents]).most_common(30)
Counter([e.text.lower().strip() for e in doc.ents]).most_common(30)
doc.ents[0].type
doc.ents[0]._type
doc.ents[0]._ent_type
doc.ents[0].label
doc.ents[0].label_
doc.to_disk('data/sections/003.spacy')
from_disk=spacy.Doc.from_disk('data/sections/003.spacy')
from_disk=spacy.tokens.Doc.from_disk('data/sections/003.spacy')
from spacy.tokens import Doc
from spacy.vocab import Vocab
from_disk = Doc(Vocab()).from_disk("data/sections/003.spacy")
get_ipython().run_line_magic('ls', '-lh data/sections/003.spacy')
get_ipython().system('wc -l data/sections/003.spacy')
get_ipython().system('head data/sections/003.spacy')
from_disk==doc
from_disk.ents==doc.ents
from_disk.ents
Counter([e.text.lower().strip() for e in doc.ents]).most_common(30)
Counter([e.text.lower().strip() for e in from_disk.ents]).most_common(30)

get_ipython().run_line_magic('pinfo', 'spacy.pipe')
get_ipython().run_line_magic('pinfo', 'model.pipe')
spacy.prefer_gpu()
get_ipython().run_line_magic('pinfo', 'spacy.prefer_gpu')

root = Path('data/sections')
list(root.glob('*.txt'))
sorted(root.glob('*.txt'))
get_ipython().run_line_magic('save', 'code/ner.py ~0/')
import spacy
from spacy import displacy
from tqdm import tqdm
from pathlib import Path
model = spacy.load('fr_core_news_lg')
root = Path('data/sections')
def load_text(paths):
    for path in tqdm(paths):
        with open(path, 'rt') as file:
            text = file.read()
        yield text
        
loader = load_text(sorted(root.glob('*.txt')))
def load_text(paths):
    for path in tqdm(paths):
        with open(path, 'rt') as file:
            text = file.read()
        yield path, text
        
        
for path, text in load_text(sorted(root.glob('*.txt'))):
    doc = model(text)
    with open(path.with_suffix('.html'), 'wt') as file:
        file.write(html)
    doc.to_disk(path.with_suffix('.spacy'))
    
for path, text in load_text(sorted(root.glob('*.txt'))):
    doc = model(text)
    html = displacy.render(doc, style="ent", page=True)
    with open(path.with_suffix('.html'), 'wt') as file:
        file.write(html)
    doc.to_disk(path.with_suffix('.spacy'))
    
    
