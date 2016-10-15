# import random
# 
# def noReplacementSimulation(numTrials):
#     yes = 0
#     for i in range(numTrials):
#         ballPool = [1, 2, 3, 4, 5, 6]
#         ballSelected = []
#         #select 3 balls
#         for j in range(3):
#             ball = random.choice(ballPool)
#             ballSelected.append(ball)
#             ballPool.remove(ball)
#         #check if balls have the same color
#         if sorted(ballSelected) == [1, 2, 3] or sorted(ballSelected) == [4, 5, 6]:
#             yes += 1
#     
#     return float(yes) / numTrials
# 
# print noReplacementSimulation(1000000)

# import random
# import pylab
# 
# def SumOfRoll(numberTrials):
#     result = []
#     for i in range(numberTrials):
#         a = random.randrange(1, 7)
#         b = random.randrange(1, 7)
#         result.append(a + b)
#     return result
# 
# pylab.figure() 
# pylab.hist(SumOfRoll(1000000))
# pylab.show()
class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''
import random
    
def test():
    if random.random() < 0.5:
        return 1
    else:
        raise NoChildException

L = [1, 2, 3, 4]
try:
    L.append(test())
except NoChildException:
    pass
print L
