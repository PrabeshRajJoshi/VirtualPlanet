# Python module containing creator functions and relevant classes to build objects within a street
import numpy as np

class StreetObjectCategories:
    '''
    class containing information on the various categories of objects found in a street 
    '''
    def __init__(self):
        self._Buildings = ["House", "School", "Shopping Mall", "Office"]
        self._NonBulidings = ["Park", "Empty", "Parking Lot", "Farm Land"]
    
    def AddBuilding(self, CategoryName):
        if CategoryName not in self._Buildings:
            self._Buildings.append(CategoryName)

    def AddNonBuilding(self, CategoryName):
        if CategoryName not in self._NonBulidings:
            self._NonBulidings.append(CategoryName)

    def GetBuildings(self):
        return self._Buildings

    def GetNonBuildings(self):
        return self._NonBulidings
    
    def GetAll(self):
        return self._Buildings + self._NonBulidings


def CreateStreetObjects(StreetContainer, categories_list):
    '''
    Function to create random StreetObject in all streets found in StreetContainer
    '''
    StreetList = StreetContainer.GetStreets()
    print("Creating street objects in %i streets of %s ..."%(len(StreetList),StreetContainer.Name))

    for street in StreetList:
        street.SpawnStreetObjects(categories_list)
        street.print_info()

def CreateApartments(BuildingsContainer):
    '''
    Function to create random Apartments in all buildings found in BuildingsContainer
    \t anywhere between 1 and 20 apartments are created!
    '''
    BuildingsList = BuildingsContainer.GetBuildings()
    NumAptMin = 1
    NumAptMax = 20
    print("Creating apartment objects in %i buildings in %s ..."%(len(BuildingsList),BuildingsContainer.Name))
    # Create apartments in buildings
    for building in BuildingsList:
        building.SpawnApartments(np.random.randint(NumAptMin, NumAptMax))

def CreateResidents(ApartmentsContainer):
    '''
    Function to create random Residents in all apartments found in ApartmentsContainer
    \t anywhere between 1 and 5 residents are created!
    '''
    ApartmentsList = ApartmentsContainer.GetApartments()
    NumResidendsMin = 1
    NumResidentsMax = 5
    print("Populating %i apartments in %s ..."%(len(ApartmentsList),ApartmentsContainer.Name))
    # Create residents in apartments
    for apartment in ApartmentsList:
        apartment.SpawnResidents(np.random.randint(NumResidendsMin, NumResidentsMax))
