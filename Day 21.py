class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhhale')



class Fish(Animal):
    def __init__(self):
        super().__init__()


    def breathe_under_water(self):
        super().breathe()
        print("doing this under water")




    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

nemo.breathe_under_water()




