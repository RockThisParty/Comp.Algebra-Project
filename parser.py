import re

text = []
dictionary = {}

def parse(filename):
    global text
    global dictionary
    with open(filename, "r") as f:
        for line in f:          
            text += re.split(r'\W+', line)
    words = list(set(text))
    words.remove("")
    return words

def html(filename):
    with open(filename+".html", "w") as f:
         f.write("Hello it's work")


#html("test") 
print(parse("test"))
