import random
"""Importing random values for taking random values into the list"""
class ConsoleGame:
    """Defining class for the game"""

    def generate(self):
        """In this function we generate the random 8X8 matrix in list by importing random values"""
        self.lst=[]
        for i in range(8):
            self.mat= random.sample(range(100),8)
            self.lst.append(self.mat)
        return self.lst

    def check(self,user_inp):
        """In this function we take user input"""
        self.z=0

        self.user_inp=user_inp
        for i in range(8):
            for j in range(8):
                if self.user_inp == self.lst[i][j]:
                    """If user input matches the element in the matrix then it breaks"""
                    self.z=1
                    break
        return self.z
             
                    
                    
def main():
    b=ConsoleGame()
    g=b.generate()
    print(g)
    while True:
        c=int(input("Enter 1 to play:"))
        if c==1:
            print('Lets begin the game')
            a=int(input('Enter a number below 100:'))
            y=b.check(a)
            if y==1:
                """If user input is the element in matrix it prints you loose else it prints win"""
                print('You loose! :(')
            else:
                print('You win! :)')
        else:
              break


main()
        

    
    
                    

        
        
         
