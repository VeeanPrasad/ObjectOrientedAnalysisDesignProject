import uuid

# The singleton pattern was implemented for Pin Generation. 
# We need to have only one instance of our class for every single quiz and a single DB connection shared by multiple objects 
# to store the unique pin generated for each quiz.

class PinGenerator:
   __instance = None

   @staticmethod
   def getInstance():
      if PinGenerator.__instance == None:
         PinGenerator()
      return PinGenerator.__instance

   def __init__(self):
      if PinGenerator.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         PinGenerator.__instance = self

   def get_uuid(self):
       return str(uuid.uuid4())[:5]

   @staticmethod
   def generate_pin():
       pin_generator = PinGenerator.getInstance()
       return pin_generator.get_uuid()
