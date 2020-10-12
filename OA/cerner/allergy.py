"""
对病人信息的统计，找到某个地区的病人，找到某个年龄的病

"""


from enum import Enum
from abc import ABC

class Severity(Enum):
    HIGH, MEDIUM, LOW = 1, 2, 3

class DiseaseName(Enum):
    D1, D2, D3, D4 = 1, 2, 3, 4

class AllergyName(Enum):
    A1, A2, A3, A4 = 1, 2, 3, 4

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person:
    def __init__(self, first_name: str, last_name: str, age: int, address: Address, number: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__address = address
        self.__number = number

    def get_age(self):
        return self.__age

class Disease:
    def __init__(self, name: DiseaseName):
        self.name = name

class Allergy:
    def __init__(self, name: AllergyName, severity: Severity):
        self.__name = name
        self.__severity = severity

class Patient(Person):
    def __init__(self, first_name: str, last_name: str, age: int, address: Address, number: int, diseases: list, allergy: list):
        super().__init__(first_name, last_name, age, address, number)
        self.__disease = diseases
        self.__allergy = allergy

    def get_disease(self):
        return self.__disease


class Search(ABC):
    def search_patient_by_location(self, address: Address):
        None
    def search_disease_by_age(self, age: int):
        None


class Catelog(Search):
    def __init__(self):
        self.__patients = []
        self.__age_disease = {}

    def add_patient(self, patient: Patient):
        self.__patients.append(patient)
        age = patient.get_age()
        if age not in self.__age_disease:
            self.__age_disease[age] = set()
        self.__age_disease[age].add(patient.get_disease())
        
    def search_patient_by_location(self, address):
        pass

    def search_disease_by_age(self, age):
        return self.__age_disease[age]
    

