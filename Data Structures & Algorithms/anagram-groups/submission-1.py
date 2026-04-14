class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}

        #for each word in list
        #initialize 26 long array corresponding to letters
        for word in strs:
            temp = [0] * 26
            

            #for each char in word
            #update index of array corresponding to word by +1
            for char in word:
                temp[ord(char) - 97] += 1
            
            #if key in ht already
            #ht[key].append new word
            #update array as key to ht
                # key - abc array
                # val - word in an array
            
            #convert to tuple so it is mutable and can be hashed
            temp = tuple(temp)

            if temp in ht:
                ht[temp].append(word)
            else:
                ht.update({temp : [word]})

        #for each key in ht
        #build new 2d array 
        res = []
        print(ht)


        for x in ht.values():
            print(x)
            res.append(x)

        # for key in ht:
        #     temp = []
        #     for val in ht[key]:
        #         temp.append(val)
        #     res.append(temp)
        return res
        
