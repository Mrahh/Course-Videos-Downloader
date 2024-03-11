from moodlev2.moodlemib import MoodleMiB
from moodlev2.video import Video
from moodlev2.util import Util
import json
import attrs

if __name__ == "__main__":

    all_videos_list: list[Video] = []

    moodle_connection = MoodleMiB()

    courses = Util.get_courses_from_file("all_courses_20202021.json")
    
    for course in courses:
        all_videos_list.extend(moodle_connection.get_video_links(course))


    json_string = json.dumps([ob.obj_dict() for ob in all_videos_list], indent=4)
    print(json_string)

    with open("out_links.json", "w") as out_file:
        out_file.write(json_string)
        