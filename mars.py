"""Here we are defining a class to calculate the remaining distance to be travelled to reach the Mars planent"""
class MarsMissionDetector:

    def __init__(self,distance):
        """This function defines the input distance that we have already covered travelling"""
        self.distance=distance

    def calculate(self):
        """Here based on the distance travelled remaining distance needed to travel to mars is calculated"""
        self.remaining= 54.6- self.distance
        print('The remaining distance to be travelled is %f million kilometers:'%self.remaining)
        self.d={self.distance:self.remaining}
        """It is represented in the form of dictionary where key is represented by distance already travelled and value is remaining distance"""
        print(self.d)

def main():
    """This is the function which calls the class by its object and gives the value for distance travelled which is taken by the user as input"""
    x=int(input("Enter the distance travelled already:"))
    y=MarsMissionDetector(x)
    y.calculate()

main()

        
    
