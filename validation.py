class Validation:
    def __init__(self,data):
        self.data = data

    #checks if data is of specifie length
    def length_check(self,length):
        if len(self.data) == length:
            return True
        return False

    #checks if data is empty
    def presence_check(self):
        if len(self.data) == 0:
            return False
        return True

    #checks if data is within specfied range
    def range_check(self,value):
        if len(self.data)>=value:
            return True
        return False