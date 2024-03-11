from moodlev2.course import Course


class Video():

    def __init__(self, link:str, name:str, course: Course):

        self.link = link
        self.name = name
        self.course = course

    def obj_dict(self):

        return {"link": self.link, 
                "name": self.name,
                "course": self.course.obj_dict()}