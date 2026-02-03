class calc:
    def __init__(self):
        pass

    def __call__(self, x):
        y =  2*x+3
        return y
    

class LibraryGate():
    def __init__(self, reqLevel):
        self._reqLevel= reqLevel
        self._count = 0

    def __call__(self, name, accessLevel):
        if accessLevel in self._reqLevel:
            self._count += 1
            print(f"Welcome {name}")
            return True
        else:
            print("Denied!")
            return False
        


