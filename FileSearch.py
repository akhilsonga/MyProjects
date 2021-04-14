import os
import platform

def add_removal(s,cut):
    j=0
    print("s value : ",s)
    size = len(s)
    for i in range(size):
        j = j+1
        
    s3 = s
    i=0
    j=0
    #print(s3)
    for i in range(size):
        print("s3 value",s3)
        s3 = s3[ : -1]
        if s3[-1] == cut:
            s3 = s3[ : -1]
            break
   
    return s3


def search1(addr,filen1):
    os.chdir(addr)
    l = os.listdir()
    #filen1 = "TkinTest.py" #
    filen = filen1
    f = 0
    j = 0
    filen = add_removal(filen,".")
    filen = filen.lower()
    #s3 = s3[ : -1]
    str1 = ""
    for i in l:
        i = i.split(".")
        if len(i) >= 2:
            str1 = ''.join(map(str, i))
            str1 = str1.lower()
            str1 = add_removal(str1,".")
            
        if str1 == filen:
            f = f+1
            print("File found")
            print("File: ",)
        
    print("files",filen1,"found in ",addr," - directory") 
    return f
    
  
# Main function
def main():
    #start:
    a = platform.system()
    s = os.getcwd() 
    #s = "/users/akhilsonga/desktop/programs"
    f = 0
    temp = s
    f1 = 0
    f = 0
    a1 = 0
    if a == "Darwin":#checking whether it is mac or not?
        #
        ins = input("enter File name: ")
        #f = search1(s,i)
        a1 = s.split("/")
        a1 = len(a1) - 2
        print("a value (main) : ",a1)
        
        for i in range(a1):
            temp = add_removal(temp,"/")
            print("main Directory: ",temp)
            f = search1(temp,ins)
            f1 = f1 + f
            print("found : ",f1)


if __name__ == "__main__":
    main()   