from moodle import Moodle
from moodle.core.course.content import Section, Module
from moodlev2.video import Video
from moodlev2.course import Course
import os
from dotenv import load_dotenv

load_dotenv()

class MoodleMiB():


    def __init__(self,url: str = 'https://elearning.unimib.it/webservice/rest/server.php',
                  token: str = os.environ["token"]):

        self.url = url
        self.token = token

        try:
            self.moodle = Moodle(url, token)
        except Exception:
            raise Exception("Failed to initialize the APIv2") from None
        

    def get_video_links(self, course: Course) -> list[Video]:

        # get list of main sections of the course
        main_course_sections = self.moodle.core.course.get_contents(course.id)

        # video list
        videos: list[Video] = []

        for main_section in main_course_sections:

            # maybe there's modules in the main page, is good to avoid them
            if main_section.__class__ == Section:
                videos.extend(self._iterate_section(main_section, course))

        return videos


    def _iterate_section(self, section: Section, course: Course) -> list[Video]:
        
        videos: list[Video] = []

        modules = section.modules

        for module in modules:

            if module is None:
                print("ciao")

            if module.modname == "kalvidres":
                videos.append( Video(module.url, module.name, course))

        return videos