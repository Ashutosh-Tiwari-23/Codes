# Implementation of polymorphism using Abstract classes,run time and compile time polymorphism
from abc import ABC, abstractmethod
class Vehicle(ABC):
    '''ABstract class can't be initiated
       It's also called as an Interface'''
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def engine_status(self):
        pass
    
    @abstractmethod
    def vehicle_motion(self):
        pass 


class Car(Vehicle):
    def __init__(self, model, mileage, purchasingYear, registrationId) -> None:
        super().__init__()
        self.model = model 
        self.mileage = mileage 
        self.purchasingYear = purchasingYear
        self.registrationId = registrationId
        self.__speed = 90
    
    def drive(self):
        #print(f"The car is driving at a speed of {self._Car__speed}")
        #accessing the private variable like obj._MyClass__var is known as name mangling, this will work 
        # but if you are trying to access the variable within the class, then it's not a beat practice to use like that
        # instead use {self.__speed}
        print(f"the car is driving at a speed of {self.__speed}")
        
    def engine_status(self):
        return "the engine is worling normally"
    
    def vehicle_motion(self):
        return "the vehicle is in motion"
    