from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializes the MongoClient.
        self.client = MongoClient('mongodb://%s:%s@localhost:35524'%(user,password))
        self.database = self.client['AAC']

    # Implements the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # Data should already be in the dictionary. 
            print("Animal created successfully.")
        else:
            raise Exception("Data parameter is empty, cannot save.")
            
    # This is a readme.
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False})  # Data should already be in the dictionary.   
            return data
        else:
            raise Exception("Hint is empty, cannot read.")
            
            
    # This will find all appropriate items that match the dictionary.
    def delete(self, _data):
        if _data is not None:
            data = self.read(_data) # Checks to see if the animal actually exists.
            if data is None:
                print("Animal unable to be located.")
                return
            #if found delete the animal or animals
            self.database.animals.delete_many(_data)  # The data here should be already in the dictionary.
            data = self.read(_data) #This will confirm if the animal was actually deleted.
            return data
        else:
            raise Exception("Hint is empty, cannot read.")
            
    # This is utilized to properly update the identification of the collection.
    def update(self, _keys,_data):
        if _data is not None and _keys is not None:
            self.database.animals.update_many(_keys,{'$set':_data})  # Checks for the document to update information.
            data = self.read(_data)
            return data
        else:
            raise Exception("Key and data is neccessary to modify the collection.")