# # # # # def iterPower(base, exp):
# # # # #     result = 1
# # # # #     while exp > 0:
# # # # #         result = result * base
# # # # #         exp -= 1
# # # # #     return result
# # # # # # 
# # # # # # print iterPower(7, 2)
# # # # # from itertools import count
# # # # # from matplotlib.mathtext import Char
# # # # # 
# # # # # # def recurPowerNew(base, exp):
# # # # #     if exp <= 0:
# # # # #         return 1
# # # # #     if exp % 2 == 0:
# # # # #         return recurPowerNew(base * base, exp/2)
# # # # #     else:
# # # # #         return base * recurPowerNew(base, exp - 1)
# # # # #     
# # # # # print recurPowerNew(3, 0)
# # # # from Finder.Finder_items import item
# # # # 
# # # # # def gcdIter(a, b):
# # # # #     if a < b:
# # # # #         test = a
# # # # #     else:
# # # # #         test = b
# # # # #     while True:
# # # # #         if (a % test == 0) and (b % test == 0):
# # # # #             return test
# # # # #         test -= 1
# # # # 
# # # # # def gcdRecur(a, b):
# # # # #     if a == 0:
# # # # #         return b
# # # # #     elif b == 0:
# # # # #         return a
# # # # #     if a > b:
# # # # #         return gcdRecur(a - b, b)
# # # # #     else:
# # # # #         return gcdRecur(a, b - a)
# # # # #     
# # # # # print gcdRecur(2, 12), gcdRecur(6, 12), gcdRecur(9, 12), gcdRecur(17, 12)
# # # # 
# # # # # def printMove(fr, to):
# # # # #     print 'move from' + ' ' + str(fr) + ' ' + 'to' + ' ' + str(to)
# # # # #     
# # # # # def Towers(n, fr, to, spare):
# # # # #     if n == 1:
# # # # #         printMove(fr, to)
# # # # #     else:
# # # # #         Towers(n - 1, fr, spare, to)
# # # # #         Towers(1, fr, to, spare)
# # # # #         Towers(n - 1, spare, to, fr)
# # # # #         
# # # # # Towers(7, 'fr', 'to', 'spare')
# # # # 
# # # # # def lenIter(aStr):
# # # # #     count =0
# # # # #     for ch in aStr:
# # # # #         count = count + 1
# # # # #     return count
# # # # # 
# # # # # print lenIter('asd')
# # # # # 
# # # # # def lenIter(aStr):
# # # # #     if aStr == "":
# # # # # #         return 0
# # # # # #     else:
# # # # # #         return 1 + lenIter(aStr[1:])
# # # # # # 
# # # # # # print lenIter('a')
# # # # # 
# # # # # def isIn(char, aStr):
# # # # # #     if len(aStr) == 1:
# # # # # #         if char == aStr[0]:
# # # # # #             return True
# # # # # #         else:
# # # # # #             return False
# # # # #     if len(aStr) % 2 == 0:
# # # # #         if aStr[len(aStr)/2] == char:
# # # # #             return True
# # # # #         elif char < aStr[len(aStr)/2]:
# # # # #             return isIn(char, aStr[0:len(aStr)]/2)
# # # # #         else:
# # # # #             return isIn(char, aStr[len(aStr)/2:])
# # # # #     else:
# # # # #         if aStr[(len(aStr)-1)/2] == char:
# # # # #             return True
# # # # #         elif char < aStr[(len(aStr)-1)/2]:
# # # # # #             return isIn(char, aStr[0:(len(aStr)-1)/2])
# # # # # #         else:
# # # # # #             return isIn(char, aStr[(len(aStr)-1)/2:])
# # # # # print isIn('p', 'abcdefghijkl')
# # # # # 
# # # # #         
# # # # # 
# # # # # def semordnilap(str1, str2):
# # # # #     if len(str1) == 1 or len(str2) == 1 or str1 == str2:
# # # # #         return False
# # # # #     if len(str1) != len(str2):
# # # # #         return False
# # # # #     
# # # # #     def realcheck(str1, str2):
# # # # #         if str1 == "" and str2 == "":
# # # # #             return True
# # # # #         if str1[0] == str2[-1]:
# # # # #             return realcheck(str1[1:], str2[:-1])
# # # # #         else:
# # # # #             return False
# # # # #     return realcheck(str1, str2)
# # # # #         
# # # # # 
# # # # # 
# # # # # print semordnilap('i', 'p')
# # # # # 
# # # # # x = (1, 2, (3, 'John', 4), 'Hi')
# # # # # 
# # # # # print x[-1][2]
# # # # # 
# # # # # def oddTuples(aTup):
# # # # #     bTup = ()
# # # # #     for i in aTup:
# # # # #         bTup = bTup + (i,)
# # # # #     return bTup
# # # # # 
# # # # # print oddTuples((1, 2, 3, 4, [4,5,6]))
# # # # 
# # # # # 
# # # # # def applyToEach(L, f):
# # # # #     for i in range(len(L)):
# # # # #         L[i] = f(L[i])
# # # # # 
# # # # # def carre(a):
# # # # #     return a*a
# # # # # 
# # # # # testList = [1, -4, 8, -9]
# # # # # applyToEach(testList, carre)
# # # # # print testList
# # # # 
# # # # # animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# # # # # 
# # # # # animals['d'] = ['donkey']
# # # # # animals['d'].append('dog')
# # # # # # animals['d'].append('dingo')
# # # # # # 
# # # # # # print animals
# # # # # 
# # # # # def howMany(dict_given):
# # # # #     amount = 0
# # # # #     for i in dict_given.values():
# # # # #         for e in i:
# # # # #             amount += 1
# # # # #     return amount
# # # # # 
# # # # # animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# # # # # 
# # # # # animals['d'] = ['donkey']
# # # # # animals['d'].append('dog')
# # # # # animals['d'].append('dingo')
# # # # # 
# # # # # print howMany(animals) 
# # # # # 
# # # # # def howMany1(dict_given):
# # # # #     result = 0
# # # # #     for i in dict_given.keys():
# # # # #         result = result + len(dict_given[i])
# # # # #     return result
# # # # # 
# # # # # print howMany1(animals)       
# # # # # 
# # # # # def biggest(dict_given):
# # # # #     result = ''
# # # # #     biggest_value = 0
# # # # #     for i in dict_given.keys():
# # # # #         if len(dict_given[i]) >= biggest_value:
# # # # #             result = i
# # # # #     return result
# # # # # 
# # # # # print biggest(animals)
# # # # 
# # # # #         
# # # # #         
# # # # # def ndigits(x):
# # # # #     x = abs(x)
# # # # #     if x < 10:
# # # # #         return 1
# # # # #     else:
# # # # #         return 1 + ndigits(x/10)
# # # # #     
# # # # # print ndigits(-392840923814)
# # # # # 
# # # # # def isWordGuessed(secretWord, lettersGuessed):
# # # # #     count = 0
# # # # #     for i in secretWord:
# # # # #         if i in lettersGuessed:
# # # # #             count += 1
# # # # #     if count == len(secretWord):
# # # # #         return True
# # # # #     else:
# # # # #         return False
# # # # #             
# # # # # # print isWordGuessed('love', 'lo')
# # # # # def getGuessedWord(secretWord, lettersGuessed):
# # # # #     word_printed = []
# # # # #     for i in secretWord:
# # # # #         if i in lettersGuessed:
# # # # #             word_printed.append(i)
# # # # #         else:
# # # # #             word_printed.append('_ ')
# # # # #     return ''.join(word_printed)
# # # # # 
# # # # # # print getGuessedWord('apple', 'p')
# # # # # import string
# # # # # def getAvailableLetters(lettersGuessed):
# # # # #     letteroriginal = list(string.ascii_lowercase)
# # # # #     for i in lettersGuessed:
# # # # #         if i in letteroriginal:
# # # # #             letteroriginal.remove(i)
# # # # #     return ''.join(letteroriginal)
# # # # # 
# # # # # print getAvailableLetters('hijklm')
# # # # # 
# # # # # 
# # # # def nfruits(initial_quantities, string_pattern):
# # # #     #check every element in the string_pattern based on its order
# # # #     for i in range(len(string_pattern)):
# # # #         #He ate one kind of fruit
# # # #         initial_quantities[string_pattern[i]] -= 1
# # # #         #except the last one which he eats just on reaching the campus
# # # #         if not i == (len(string_pattern) - 1):
# # # #             #he buyed 1 fruit of each type other than the one he just had
# # # #             for item in initial_quantities.keys():
# # # #                 if not item == string_pattern[i]:
# # # #                     initial_quantities[item] += 1
# # # #     #to obtain the maximum
# # # #     max_value = 0
# # # #     for item in initial_quantities.values():
# # # #         if item >= max_value:
# # # #             max_value = item
# # # #      
# # # #     return max_value
# # # #  
# # # #  
# # # # # print nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')
# # # # # print range(2)
# # # testa = {'a': 1, 'b': 2}
# # # # testb = testa.copy()
# # # # testa['a'] = 0
# # # # print testb
# # # 
# # # x = 'pi'
# # # y = 'pie'
# # # x, y = y, x
# # # print x, y
# # 
# # class Clock(object):
# #     def __init__(self, time):
# #         self.time = time
# #         
# #     def print_time(self):
# #         print self.time
# # 
# # boston_clock = Clock('5:30')
# # paris_clock = boston_clock
# # paris_clock.time = '10:30'
# # boston_clock.print_time()
# 
# # class Quene(object):
# #
# 
# class Queue(object):
#     def __init__(self):
#         self.vals = []
# #     
# #     def insert(self, e):
# #         self.vals.append(e)
# #     
# #     def remove(self):
# #         try:
# #             return self.vals.pop(0)
# #         except:
# #             raise ValueError
# #         
# # queue = Queue()
# # queue.insert(5)
# # queue.insert(6)
# # print queue.vals 
# # print queue.remove()        
# # print queue.remove()
# # print queue.remove()   
#      
#      
# def genPrimes():
#     listPrime = []
#     prime = 1
#     while True:
#         check_status = False
#         while not check_status:
#             check_status = True
#             prime += 1
#             for i in listPrime:
#                 if (prime % i) == 0:
#                     check_status = False
#         listPrime.append(prime)
#         yield prime
# 
# prime = genPrimes()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# print prime.next()
# 
#              
        

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.location = location
        self.species_count = species_types
    def get_number_of_species(self, animal):
        try:
            return self.species_count[animal]
        except:
            return 0
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_count.copy()  
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if self.species_count[species] > 0:
            self.species_count[species] -= 1
        cache_animal = []
        for item in self.species_count.keys():
            if self.species_count[item] == 0:
                cache_animal.append(item)
        for item in cache_animal:
            del self.species_count[item]
            
test = AdoptionCenter('a', {'Cat': 1}, (1.0, 1.0))
print test.get_location()
print test.get_name()