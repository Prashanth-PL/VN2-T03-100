
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is , {self.name}")
        print(f"Train is  {self.train}")


prashanthApplication = RailwayForm()
prashanthApplication.name = "Prashanth"
prashanthApplication.train = "Rajdhani Express"
prashanthApplication.printData()

