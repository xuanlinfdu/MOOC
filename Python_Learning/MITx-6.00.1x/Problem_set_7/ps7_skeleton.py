import random as rand
import string
import math

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        temp_location = []
        for item in location:
            temp_location.append(float(item))
        self.location = tuple(temp_location)
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
      

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name 
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return float(1 * adoption_center.get_number_of_species(self.desired_species))
    



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        sum_con = 0
        for item in self.considered_species:
            sum_con += adoption_center.get_number_of_species(item)
        return Adopter.get_score(self, adoption_center) + (0.3 * sum_con)

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center) - (0.3 * adoption_center.get_number_of_species(self.feared_species)) 
        if score >= 0.0:
            return score
        else:
            return 0.0

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        for item in self.allergic_species:
            for animal in adoption_center.get_species_count().keys():
                if item == animal:
                    return 0.0
        return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        mini_effect = 1.0
        for item in self.medicine_effectiveness.keys():
            for animal in adoption_center.get_species_count().keys():
                if item == animal:
                    if self.medicine_effectiveness[item] < mini_effect:
                        mini_effect = self.medicine_effectiveness[item]
                        
        return Adopter.get_score(self, adoption_center) * mini_effect
                
            

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        temp_location = []
        for item in location:
            temp_location.append(float(item))
        self.location = tuple(temp_location)
        
    def get_linear_distance(self, to_location):
        d_x = self.location[0]-to_location.get_location()[0]
        d_y = self.location[1]-to_location.get_location()[1]
        d = math.sqrt(d_x**2 + d_y**2)
        return d
        
    def get_score(self, adoption_center):
        if self.get_linear_distance(adoption_center) < 1:
            return Adopter.get_score(self, adoption_center)
        elif self.get_linear_distance(adoption_center) < 3 and self.get_linear_distance(adoption_center) >= 1:
            return Adopter.get_score(self, adoption_center) * rand.uniform(0.7, 0.9)
        elif self.get_linear_distance(adoption_center) < 5 and self.get_linear_distance(adoption_center) >= 3:
            return Adopter.get_score(self, adoption_center) * rand.uniform(0.5, 0.7)
        elif self.get_linear_distance(adoption_center) < 5 and self.get_linear_distance(adoption_center) >= 3:
            return Adopter.get_score(self, adoption_center) * rand.uniform(0.5, 0.7)
        elif self.get_linear_distance(adoption_center) >= 5:
            return Adopter.get_score(self, adoption_center) * rand.uniform(0.1, 0.5)

class CmpAdopterCenter(object):
    def __init__(self, adopter, adoptioncenter):
        self.adopter = adopter
        self.adoptioncenter = adoptioncenter
    
    def get_adopter(self):
        return self.adopter
    
    def get_adoptioncenter(self):
        return self.adoptioncenter
    
    def display_score(self):
        return self.adopter.get_score(self.adoptioncenter)
    
    def __cmp__(self, other):
        return cmp(self.adopter.get_score(self.adoptioncenter), other.adopter.get_score(other.adoptioncenter))
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    list_for_sort = []
    list_for_print = []
    for item in list_of_adoption_centers:
        list_for_sort.append(CmpAdopterCenter(adopter, item))
    list_for_sort.sort(reverse = True)
    for item in list_for_sort:
        list_for_print.append(item.get_adoptioncenter())
    return list_for_print
    
    

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    list_for_sort = []
    list_for_print = []
    for item in list_of_adopters:
        list_for_sort.append(CmpAdopterCenter(item, adoption_center))
    list_for_sort.sort(reverse = True)
    length = min(n, len(list_for_sort))
    for i in range(length):
        list_for_print.append(list_for_sort[i].get_adopter())
    return list_for_print

    

# adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
# adopter2 = Adopter("Two", "Cat")
# adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
# adopter4 = FearfulAdopter("Four","Cat","Dog")
# adopter5 = SluggishAdopter("Five","Cat", (1,2))
# adopter6 = AllergicAdopter("Six", "Cat", "Dog") 
# 
# ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
# ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
# ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))
# 
# # how to test get_adopters_for_advertisement
# get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# # you can print the name and score of each item in the list returned
#  
# adopter4 = FearfulAdopter("Four","Cat","Dog")
# adopter5 = SluggishAdopter("Five","Cat", (1,2))
# adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 
#  
# ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
# ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
# ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
# ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
# ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
# ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
#  
# # how to test get_ordered_adoption_center_list
# get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])                            
# # you can print the name and score of each item in the list returned
