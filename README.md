# Course-Videos-Downloader

Script that downloads all available videos from the selected courses

# Setup
```pip install -r requirements.txt```

# Procedure
* Add your mail and pw to the .env file and insert the personal token.
* You can add the courses you want to download in the **all_courses_20202021.json** file.
* Then you run the **version2.py** file, and you'll get all the videos of the courses you chose.
* You can find the videos information in the **out_links.json** file.
* Lastly, run the **index.py** file that will run a chromium instance and start downloading here.
* From here, you can just wait until the script ends and check the command line to see the logs.

When the script is finished, check the brokenLinks.json file to check the videos that couldn't be downloaded, and you can manually check the videos. (Probably broken videos, password videos, or access denied) 
or just replace the videos in **out_links.json** with the ones you want to retry downloading.

Special thanks to Brock, Koalas, Depa and Damiano for their contributions to the project.
