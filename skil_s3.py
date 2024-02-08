import re
import numpy as np

class Skil(object):
    """Skilaverkefni 3 f. REI

    """

    def arr_to_dict(self,ls1):
        d={}

        for i in range(len(ls1)):

            for j in range(len(ls1[i])):
                # print(j)
                d[(i,j)] = ls1[i][j]
        return d




    def dict_to_arr(self,d):
        ls1 = []
        temp = []
        max = int(np.sqrt(len(d)))-1 # to get one side length without going through the list twice
        # print(max)
        for k, v in d.items():
            i,j = k
            temp.append(v)
            
            if (j == max):
            
                # print(j)
                ls1.append(temp)
                temp = []

        return ls1
        # print(ls1)



    def snuavid(self,d1):
        d2 = {}
        for k, v in d1.items():
            if v in d2:
                # temp = []
                if type(d2[v]) is list:
                    d2[v].append(k)
                else:
                    d2[v] = [d2[v], k]
            else:    
                d2[v]= k
        return d2

if __name__ == '__main__':
    skil = Skil()
    # val = skil.arr_to_dict([[0,1,2],[3,4,5], [6,7,8]])
    # print(val)
    # print(skil.dict_to_arr(val))
    # # print(np.arange(9).reshape((3,3)).tolist())
    # print(skil.arr_to_dict(np.arange(9).reshape((3,3)).tolist()))
    # print(skil.dict_to_arr(skil.arr_to_dict(np.arange(9).reshape((3,3)).tolist())))
    # print(skil.snuavid({"hello":2, "hell":2, "hi":1, "hel":2}))

