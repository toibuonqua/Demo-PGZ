# type: ignore
import pgzero
import random

class person:
    
    def __init__(self, list_person_images = []):
        self.list_person_images = list_person_images
        self.list_persons = []
        
    def __random_person_picture(self):
        return self.list_person_images[random.choice(range(len(self.list_person_images)))]
    
    def create_persons(self, number):
        for index in range(number):
            self.list_persons.append(Actor(self.__random_person_picture()))
        return 1

    def check_persons_death(self):
        
    
    
        
    
    