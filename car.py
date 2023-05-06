class Car:
    manufacturer = "Daimler"
    def __init__(self,year,model,color):
        self.year = year
        self.model = model
        self.color = color
        
    def start(self):
        return f"{self.model} from {self.manufacturer}is starting"
    def stop(self):
        return f"{self.model} is stopping"
    def accelerate(self):
        return f"{self.model} is accelerating at 5km/s"
        
        
        
        