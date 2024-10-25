#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe


class perro:
    
    __name = None
    __hambre = True
    __sleepy = False
    
    def __init__(self, aname = "firulais") -> None:
        self.__name = aname
        

    
    def Ladrar(self):
        print(f"{self.__name}: guau guau, te mataré")
       
    
        

if __name__ == "__main__":
    
    
    g1 = perro()
    g1.Ladrar()