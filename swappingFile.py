from os import name


#f = open('test.txt')
#print(f.read())

def switchyDitchy():
    words=0
    characters=0
    name1=input('enter the file name ')
    name2=input('enter the file name ')
    with open(name1,'r') as a:
        data_a = a.read()
    with open(name2,'r') as b:
        data_b = b.read()
    with open(name1,'w') as a:
        a.write(data_b)
    with open(name2,'w') as b:
        b.write(data_a)

switchyDitchy()
