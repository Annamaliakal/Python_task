class learnormentor():

    stat="none"
    def __init__(self):
        print("Enter your name:")
        name=input()
        self.name=name
        
    
    def addStacks(self):
        print("Enter your stack of interest:\n1.Python \n2.Go \n3.Flutter \n4.Web")
        s=input()
        self.stack=s
        
        
    def setMentorOrLearner(self):
        print("Are you a mentor or learner (enter input as such):")
        self.stat=input()
        self.status=self.stat

        
        
    def setAvailableTime(self):
        
        if self.status=="mentor": #can use stat or self.status since only after calling setMentorOrLearner() we will call this function
            print("Time of availability:")
            t=input()
            self.time=t
            
            
    def getMentor(self,stack,time):
        if self.stat=="mentor":                 #cannot use self.status since error occurs if getMentor() is called before setMentorOrLearner() 
            if(self.stack==stack and self.time==time):
                print("Mentor available")
                print("Details:")
                print("Mentor Name",self.name)
            else:
                print("None available")
        
     

        
