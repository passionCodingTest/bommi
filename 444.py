data=["1 Brown 0", "2 Cony 0","4 Doll 2","8 Brown-cony 4"]

id=[]
name=[]
parent=[]



def solution(word):

    for i in data:
        id.append(i.split()[0])
        name.append(i.split()[1])
        parent.append(i.split()[2])
    
    for idx,n in enumerate(name):
        if word in n:

            for p in parent:
                if int(p) > 0:
                    print(p)


solution("Brown")
