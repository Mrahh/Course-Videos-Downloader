import json
from moodlev2.course import Course

class Util():

    def get_courses_from_file(json_file: str) -> list[Course]:

        courses: list[Course] = []

        with open(json_file) as file:

            raw_courses = json.load(file)

            for raw_course in raw_courses:
                courses.append( Course(raw_course["link"], raw_course["course"]))

        return courses