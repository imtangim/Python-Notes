class NameofClass():
    #__init___ allows to create a instance of actual object. it means it will initiate as soon as class has been called or starts
    def __init__(self,param1,param2): 
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        #perform some action
        print(self.param1)