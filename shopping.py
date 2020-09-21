import time
import sys

class Computer():
    def __init__(self):
        self.name=""
        self.schreen=""
        self.model=""
        self.feature=[]

    def ChooseComputername(self):
        name=["HP","Toshiba","Samsung","Monster"]
        counter=1
        for i in name:
            print("{}-{}".format(counter,i))
            counter +=1
        s=int(input("[**] Choose the name you want:  "))
        if(s==len(name)):
            self.name +=name[s-1]
        elif(s>len(name)):
            self.name="This telephon doesnt exist"
        else:
            self.name +=name[s]
    def ChooseComputermodel(self):
        model=["6570b","450a","a345","5890c","4536d"]
        counter=1
        for i in model:
            print("{}-{}".format(counter,i))
            counter +=1
        v=int(input("[**] Choose the index of the model: "))
        if(v==len(model)):
            self.model+=model[v-1]
        elif(v>len(model)):
            self.name +="Error"
        else:
            self.model+=model[v]
    def ChooseComputerschreen(self):
        schreenwith=["23x45","54x67","23x45","57x87","38x96"]
        counter=1
        for i in schreenwith:
            print("{}-{}".format(counter,i))
            counter +=1

        k=int(input("[**] Choose the screen larger and width:"))
        if(k==len(schreenwith)):
            self.schreen+=schreenwith[k-1]
        elif(k>len(schreenwith)):
            self.schreen +="Error"
        else:
            self.schreen +=schreenwith[k]
    def displayendinfo(self):
         print("You choose {} model {} and the Screen larger is {}".format(self.name,self.model,self.schreen))
         print("Thank you for you choose.\n Bye ")
         time.sleep(2)
         sys.exit()
print(
    '''
    1-Choose the Computer name by the index
    2-The model index
    3-The Schreen feature
    4-The Display information
    '''
)
new_objet=Computer()
while True:
    what=int(input("|==> Choose the number: "))
    if(what==1):
       new_objet.ChooseComputername()
    elif(what==2):
        new_objet.ChooseComputermodel()

    elif(what==3):
        new_objet.ChooseComputerschreen()
    elif(what==4):
        new_objet.displayendinfo()

        
    