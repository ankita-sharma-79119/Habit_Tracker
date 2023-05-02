import datetime

class habit:
    def __init__(self, name, id=None, createdAt=datetime.date.today(), is_completed=False) -> None:
        self.__id=id
        self.__name=name
        self.__createdAt=createdAt
        self.__is_completed=is_completed

    def get_Id(self) -> str:
        return self.__id
    def get_Name(self) -> str:
        return self.__name
    def get_Created_At(self) -> str:
        return self.__createdAt
    def get_Is_Completed(self) -> str:
        return self.__is_completed
    
    @staticmethod
    def create_ui_format(name, createdAt, is_completed, id=None):
        return habit(name,
                     id,
                     createdAt,
                     is_completed)
    
    def create_db_format(self):
        return {
            "name" : self.__name,
            "createdAt": self.__createdAt.strftime("%Y-%m-%d"),
            "is_completed": self.__is_completed
        }
    
    def insert_db(self, app):
        id = app.db.habits.insert_one(self.create_db_format())
        self.__id =  id.inserted_id

    def update_db(self, app):
        app.db.habits.update_one({"_id": self.__id}, { "$set": { "is_completed": True } })
        self.__is_completed = True

    def __str__(self) -> str:
         return f""" id : {self.__id}, 
            name : {self.__name}, 
            createdAt : {self.__createdAt}
            is_completed: {self.__is_completed}"""