def lsystem(number):
    language=[]
    termset=[]
    nonterm=''
    trans=''
    input=''
    d={}
    N=number
    with open("L.txt","r") as f:
        i=0
        for line in f:
            if line.lstrip().startswith('#'): 
                continue
            if(i<1): 
                line2 = line.strip('\n').split(",")
                language=line2 
                print("Language:")
                print(language)
            elif(i==1):
                line2=line.strip('\n').split(",")
                termset=line2
            elif(i==2):
                input = line.strip('\n')
                print("Input:")
                print(input)
            else: 
                line2 = line.strip('\n').split(",")
                nonterm,trans = line2
                d[nonterm] = trans
                print("Non Terminal Symbol\n"+nonterm+"\nProduction Result\n"+trans)
            i+=1
    print("Dictionary of value pairs:")
    print(d)
    print("Terminal symbols:")
    print(termset)
    print("Input: "+input)
    string=''
    for j in range(0,N):
       for k in input:
           if k in termset:
               string+=k
           else:
               print(k)
               string+=d[k]
       input=string
       string=''
    print("For N =",N)
    print(input)

    with open("output.txt","w") as f:
        f.write(input)
    return input

if __name__ == "__main__":
    lsystem(2)
