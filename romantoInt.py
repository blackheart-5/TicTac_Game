# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:45:01 2023

@author: Adobea
"""

class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        rdict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,
        'M':1000}
        
        num = 0
        x = 0 
        
        for i in range(0,len(s)-1):
            
            if s[i] == 'I' and (s[x+1] == 'V' or s[x+1] == 'X'):
                sub = 2
            elif s[i] == 'X' and (s[x+1] == 'L' or s[x+1] == 'C'):
                sub = 20
            elif s[i] == 'C' and (s[x+1] == 'D' or s[x+1] == 'M'):
                sub = 200 
            else:
                sub = 0
            
            num = rdict[s[i]] + num - sub 
            x += 1
            
        num += rdict[s[-1]] 
            
        return num
romn = 'MCMXCIV'
romn = Solution()
romn.romanToInt('MCMXCIV')



            


        