from ..db_fields import DB_Field

class IntField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"

    def is_valid(self):
        if isinstance( self.get_kwarg("value"), int) and self.get_validators_result():
            return True
        return False

    def db_value(self):
        if self.is_valid():
            return self.get_kwarg("value") 
        return False

    def get_value(self,value):
        pass