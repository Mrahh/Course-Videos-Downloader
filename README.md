# Course-Videos-Downloader
Script that downloads all avaiable videos from the selected courses 

* Add your mail and pw in .env file and insert the personal token
* You can add the courses you want to download in all_courses_20202021.json file
* Then you run version2.py file and you'll get all the videos of che courses you chose
* You can find the videos info in out_links.json file
* Lastly run the index.py file that will run a chromium instance and start downloading here
* From here you can just wait until the script ends and just check the command line to see the logs

When the script finished, check the brokenLinks.json file to check the videos that couldnt get downloaded
and you can manually check the videos. (Probably broken videos, password videos or access denied) or
just replace the videos in out_links.json with the ones you want to retry to download
