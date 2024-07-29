class Guid(Person):
    def __init__(self,seniority,salary,name,id):
        super(Guid, self).__init__(name,id)
        self.seniority=seniority
        self.salary=salary
        self.Group=[]
        self.NumOfExercisers=0

    def GetName(self):
        return self.Name



