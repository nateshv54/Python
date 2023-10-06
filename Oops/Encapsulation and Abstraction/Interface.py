from abc import *
class Database(ABC):
    @abstractmethod
    def connect_service(self):
        pass
    @abstractmethod
    def disconnect_service(self):
        pass

class Mysql(Database):
    def connect_service(self):
        print("Mysql Db connected")
    def disconnect_service(self):
        print("Mysql Db disconnected")

class Oracle(Database):
    def connect_service(self):
        print("Oracle Db connected")
    def disconnect_service(self):
        print("Oracle Db disconnected")

database_name=input("Enter database name: ")
x1=globals()[database_name]
obj=x1()
obj.connect_service()
obj.disconnect_service()

'''
Enter database name: Mysql
Mysql Db connected
Mysql Db disconnected'''