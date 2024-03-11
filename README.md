# Course-Videos-Downloader

## Table of Contents

### 1. [Objective](#objective)
### 2. [Setup](#setup)
### 3. [Run](#run)
### 4. [Codebase](#codebase)
### 5. [Collaborate](#collaborate)
### 6. [References](#references)

## Objective

Script that downloads all available videos from the selected courses

## Setup

Here's the setup:

1. *Install Python:* You can download and install Python from the official website: [Python.org](https://www.python.org/).

2. *Install an IDE:* You can choose between VSCode, or any other IDE you prefer. You can download VSCode from [here](https://code.visualstudio.com/).

3. *Get API key:* You can get your API key from [here](https://elearning.unimib.it/user/managetoken.php) on "Moodle mobile web service" voice.
4. *Install Requirements:* You can install the needed libraries using pip:
   
   ```pip install -r requirements.txt```

If you're using VSCode, after following these simple steps, everything should be ready to go!

## Run

1. Add your mail and pw to the .env file and insert the personal token. 
2. You can add the courses you want to download in the all_courses_20202021.json file. 
3. Then you run the version2.py file, and you'll get all the videos of the courses you chose.
4. You can find the videos information in the out_links.json file. 
5. Lastly, run the index.py file that will run a chromium instance and start downloading here. 
6. From here, you can just wait until the script ends and check the command line to see the logs.

When the script is finished, check the **brokenLinks.json** file to check the videos that couldn't be downloaded, and you can manually check the videos. (Probably broken videos, password videos, or access denied) 
or just replace the videos in **out_links.json** with the ones you want to retry downloading.

## Codebase

- moodlev2: Contains Python scripts related to course management.
  - **course.py**: Defines a Course class representing a course with a unique identifier (course_id) and a name (name). The constructor initializes these properties, and the obj_dict method returns a dictionary representing the course object.
  - **moodlemib.py**: Defines a Util class with a static method get_courses_from_file that reads a JSON file containing course information and returns a list of Course objects, each initialized with data extracted from the JSON file.
  - **util.py**: Similar to moodlemib.py, this file defines a Util class with a static method get_courses_from_file for reading course information from a JSON file and returning a list of Course objects.
  - **video.py**: Defines a Video class representing a video with a link, name, and the associated course. 
- **video**: Folder that contains the destination files with all the course videos.
- **.env**: A file to be created containing email, password, and token for executing the script.
- **all_courses_20202021.json**: Contains the courses to be utilized.
- **brokenlinks.json**: Contains broken links.
- **index.py**: The script responsible for actual dumping.
- **out_links.json**: Contains all internal course links.
- **version2.py**: Script for loading courses to be dumped.


## Collaborate


If you stumble upon any errors or have ideas for enhancements, I'm open to collaboration and input from the community. 
You can contribute by:

- *Reporting Issues:* If you come across any bugs or issues, please submit them 
through GitHub's issue tracker for this project repository.

- *Pull Requests:* Feel free to submit pull requests with fixes, enhancements, 
or new features. We appreciate any contributions that improve the project.

Collaboration is essential for the continued development and improvement of this project.

## References

Special thanks to [Brock](https://github.com/BrockDeveloper), [Koalas](https://github.com/koalas11), [Depa](https://github.com/Depa31) and [Damiano](https://github.com/DamianoPellegrini) for their contributions to the project.
