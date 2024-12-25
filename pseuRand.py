import time
from lfsr import main, next_lfsr
import numpy as np
import math
class pseuRand:
    def __init__(self):
        self.bi = (1 << 127) | 1
        for i in range(int(round(time.time()))**2 % 10000):
            self.bi = next_lfsr(self.bi)
        self.num = 0
    def printNums(self):
        main()
    def coinFlip(self): #randomly ouputs a 0 or a 1
        seconds = time.time()
        
        for i in range(int(round(seconds))**2 % 1000):
            self.bi = next_lfsr(self.bi)
        self.num = self.bi & 1
        return self.num
    def nSideDie(self, sides):
        """
        Models an n-sided die
        """
        seconds = time.time()
        bin_length = math.floor(math.log(sides)/math.log(2))+1
        print(bin_length, ((1 << bin_length)-1))
        for i in range(int(round(seconds))**2 % 1000):
            self.bi = next_lfsr(self.bi)
        while (self.bi & ((1 << bin_length)-1)) > sides-1:
            # print((self.bi & ((1 >> bin_length)-1)))
            self.bi = next_lfsr(self.bi)
        return (self.bi & ((1 << bin_length)-1)) + 1
if __name__ == "__main__":
    rando = pseuRand()
    print(rando.coinFlip())
    a = []
    n = 5000
    # Coin Flipping 
    # for i in range(n):
    #     a.append(rando.coinFlip())
    # unique_elements, counts = np.unique(a, return_counts=True)
    # print(unique_elements)
    # print(counts,np.array(counts)/n)
    ###################

    # Die Rolling
    for i in range(n):
        a.append(rando.nSideDie(3))
    unique_elements, counts = np.unique(a, return_counts=True)
    print(unique_elements)
    print(counts,np.array(counts)/n)
    # print(a)
