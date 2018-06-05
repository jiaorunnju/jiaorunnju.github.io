import os
import sys

index_template = '''
## Here is all my articles

### Algorithms
{0}

### Programming
{1}

### Somethingelse
{2}
'''
path = os.getcwd() + "\\docs"
dirs = ["Algorithms", "Programming", "Somethingelse"]

toc = []

for d in dirs:
    curpath = path + "\\" + d
    files = os.listdir(curpath)
    index = ""
    for i in files:
        if os.path.isfile(curpath+"\\"+i):
            filename = os.path.splitext(i)[0]
            index += '[{0}](docs/{1}/{2})\n'.format(filename, d, filename)
    
    toc.append(index)

print(index_template.format(toc[0], toc[1], toc[2]))