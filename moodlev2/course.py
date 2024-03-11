

class Course():


    def __init__(self, course_id: int, name: str):

        self.id = course_id
        self.name = name


    def obj_dict(self):
        return self.__dict__