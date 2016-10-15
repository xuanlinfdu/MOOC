# class Location(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         
#     def move(self, deltaX, deltaY):
#         return Location(self.x + deltaX, self.y + deltaY)
#     
#     def getX(self):
#         return self.x
#     
#     def getY(self):
#         return self.y
#     
#     def distFrom(self, other):
#         xDist = self.x - other.x
#         yDist = self.y - other.y
#         return (xDist**2 + yDist**2)**0.5
#     
#     def __str__(self):
#         return '<' + self.x + ', ' + 'self.y' + '>'
#     
# class Field(object):
#     def __init__(self):
#         self.drunk = {}
#         
#     def addDrunk(self, drunk, loc):
#         if drunk in self.drunk:
#             raise ValueError('Duplicate drunk')
#         else:
#             self.drunk[drunk] = loc
#     
#     def moveDrunk(self, drunk):
#         if not drunk in self.drunk:
#             raise ValueError('Drunk not in field')
#         xDist, yDist = drunk.takeStep()
#         currentLocation = self.drunk[drunk]
#         self.drunk[drunk] = currentLocation.move(xDist, yDist)
#         
#     def getLoc(self, drunk):
#         return self.drunk[drunk]
# import random
# 
# 
# class Drunk(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'This drunk is named ' + self.name
#     
# class UsualDrunk(Drunk):
#     def takeStep(self):
#         stepChoices =\
#             [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
#         return random.choice(stepChoices)
#     
# def walk(f, d, numSteps):
#     start = f.getLoc(d)
#     for s in range(numSteps):
#         f.moveDrunk(d)
#     return(start.distFrom(f.getLoc(d)))
# 
# 
# 
# def simWalks(numSteps, numTrials):
#     homer = UsualDrunk('Homer')
#     origin = Location(0, 0)
#     distances = []
#     for t in range(numTrials):
#         f = Field()
#         f.addDrunk(homer, origin)
#         distances.append(walk(f, homer, numSteps))
#     return distances
# 
# 
# 
# def drunkTest(numTrials = 20):
#     for numSteps in [10, 100, 1000, 10000]:
#         distances = simWalks(numSteps, numTrials)
#         print 'Random walk of ' + str(numSteps) + ' steps'
#         print ' Mean =', sum(distances)/len(distances)
#         print ' Max =', max(distances), 'Min =', min(distances)
# 
# 
# 
# 
# import pylab
# #   
# # #set line width
# # pylab.rcParams['lines.linewidth'] = 6
# # #set font size for titles
# # pylab.rcParams['axes.titlesize'] = 20
# # #set font size for labels on axes
# # pylab.rcParams['axes.labelsize'] = 20
# # #set size of numbers on x-axis
# # pylab.rcParams['xtick.major.size'] = 5
# # #set size of numbers on y-axis
# # pylab.rcParams['ytick.major.size'] = 5
# # #set size of markers
# # pylab.rcParams['lines.markersize'] = 10    
# # sum = 1
# # for i in range(200):
# #     sum = sum * (1 - (i * 0.001))
# #     
# # print (1 - sum)
# 
# import random
# 
# class intDict(object):
#     """A dictionary with integer keys"""
#     
#     def __init__(self, numBuckets):
#         """Create an empty dictionary"""
#         self.buckets = []
#         self.numBuckets = numBuckets
#         for i in range(numBuckets):
#             self.buckets.append([])
#             
#     def addEntry(self, dictKey, dictVal):
#         """Assumes dictKey an int.  Adds an entry."""
#         hashBucket = self.buckets[dictKey%self.numBuckets]
#         for i in range(len(hashBucket)):
#             if hashBucket[i][0] == dictKey:
#                 hashBucket[i] = (dictKey, dictVal)
#                 return
#         hashBucket.append((dictKey, dictVal))
#         
#     def getValue(self, dictKey):
#         """Assumes dictKey an int.  Returns entry associated
#            with the key dictKey"""
#         hashBucket = self.buckets[dictKey%self.numBuckets]
#         for e in hashBucket:
#             if e[0] == dictKey:
#                 return e[1]
#         return None
#     
#     def __str__(self):
#         res = '{'
#         for b in self.buckets:
#             for t in b:
#                 res = res + str(t[0]) + ':' + str(t[1]) + ','
#         return res[:-1] + '}' #res[:-1] removes the last comma
# 
# 
# def collision_prob(numBuckets, numInsertions):
#     '''
#     Given the number of buckets and the number of items to insert, 
#     calculates the probability of a collision.
#     '''
#     prob = 1.0
#     for i in range(1, numInsertions):
#         prob = prob * ((numBuckets - i) / float(numBuckets))
#     return 1 - prob
# 
# def sim_insertions(numBuckets, numInsertions):
#     '''
#     Run a simulation for numInsertions insertions into the hash table.
#     '''
#     choices = range(numBuckets)
#     used = []
#     for i in range(numInsertions):
#         hashVal = random.choice(choices)
#         if hashVal in used:
#             return False
#         else:
#             used.append(hashVal)
#     return True
# 
# def observe_prob(numBuckets, numInsertions, numTrials):
#     '''
#     Given the number of buckets and the number of items to insert, 
#     runs a simulation numTrials times to observe the probability of a collision.
#     '''
#     probs = []
#     for t in range(numTrials):
#         probs.append(sim_insertions(numBuckets, numInsertions))
#     return 1 - sum(probs)/float(numTrials)
# 
# 
# def main():
#     hash_table = intDict(25)
#     hash_table.addEntry(15, 'a')
# #    random.seed(1) # Uncomment for consistent results
#     for i in range(20):
#        hash_table.addEntry(int(random.random() * (10 ** 9)), i)
#     hash_table.addEntry(15, 'b')
#     print hash_table.buckets  #evil
#     print '\n', 'hash_table =', hash_table
#     print hash_table.getValue(15)
# 
# # print collision_prob(1000, 200)
# # print observe_prob(1000, 200, 1000)
# def prob_birthday(numberStudent):
#     prob = 1.0
#     for i in range(numberStudent):
#         prob = prob * (float(365 - i)/float(365))
#     return (1 - prob)
# 
# def under_prob(prob_set):
#     prob = 0.0
#     size = 0
#     while prob < prob_set:
#         size += 1
#         prob = prob_birthday(size)
#     return size - 1
# 
# print under_prob(0.99)
#         
# import numpy
# 
# def stdDevOfLengths(L):
#     if len(L) == 0:
#         return float('NaN')
#     else:
#         len_list = []
#         for item in L:
#             len_list.append(len(item))
#         
#         sum_ave = 0.0
#         for item in len_list:
#             sum_ave += item
#         valueAverage = sum_ave / len(len_list)
# 
#         sum_dev = 0
#         for item in len_list:
#             sum_dev += (item - valueAverage)**2
#         return (sum_dev / len(len_list))**0.5


