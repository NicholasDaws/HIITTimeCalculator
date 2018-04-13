class Timer(object):
  def __init__(self):
    print("Enter numbers as in seconds")
    self.work = int(input("Workout:"))
    self.rest = int(input("Rest:"))
    self.exercises = int(input("Number of exercises:"))
    self.waves = int(input("Enter how many times through:"))
    self.total = ((self.work + self.rest) * self.exercises) * self.waves
    
  def showAll(self):
    print("Work", self.work)
    print("Rest", self.rest)
    print("Excercises", self.exercises)
    print("Waves", self.waves)
    print("Total seconds:", self.total)
    
  def showTotalSeconds(self):
    print("Total seconds:", self.total)
    
  def showTime(self):
    minutes = self.total / 60
    seconds = self.total % 60
    print("Minutes:", int(minutes))
    print("Seconds:", int(seconds))
    

  
time = Timer()

time.showTime()
