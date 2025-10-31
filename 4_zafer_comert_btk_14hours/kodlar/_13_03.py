# import operations
from operations import add

def greet():
    print("Merhaba.")
    
if __name__=="__main__":
    print("Ana program")
    greet()
    # print(f"Toplam : {operations.add(1,2,3)}")
    print(f"Toplam : {add(1,2,3,4)}")