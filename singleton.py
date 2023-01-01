class DataBase():
    __instance = None

    @staticmethod
    def getInstance():
        if DataBase.__instance == None:
            return DataBase()
        return DataBase.__instance
    
    def __init__(self, list_=None):

        if DataBase.__instance != None:
            pass
        else:
            DataBase.__instance = self
            self.list_of_labs = list_
    
    def __str__(self):
        return f"There are {DataBase.__instance.list_of_labs} labs in database."

    def add_labs(self, labs: list):
        self.__instance.list_of_labs += labs
        print("You successfully added new labs to the database.")


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def add_to_db(self, db: DataBase, labs):
        db.add_labs(labs)


user1 = User("Oleg", "Ivanov")
user2 = User("Olga", "Ivanova")

db1 = DataBase(["Singleton", "Observer", "Factory Method"])
print(db1)
user1.add_to_db(db1, ["Builder", "Prototype"])

db2 = DataBase(["Singleton", "Observer", "Decorator"])
print(db2)

user1.add_to_db(db2, ["Decorator"])
print(db1)

