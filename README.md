This is a simple project to practice data analysis and data analytics. I have used YouTube Dataset in this project. 

## Files
1. youtubedata.txt is the file with the raw data.
2. preprocessed.csv is the file with preprocessed data which is produced by 'preprocessing.py'.
3. preprocessing.py is a python file in which some data preprocessing has been performed on the data from 'youtubedata.txt' and the preprocessed data is stored in 'preprocessed.csv'
4. Program.py is the python file in which most of the analytics is performed on the preprocessed data in 'preprocessed.csv'. This file produces many csv files as output.
5. categoriesbycontroscore.csv is the file which contains the 'Video Categories' arranged in order of decreasing controversial score. This score was obtained by dividing 'number of comments' by 'number of views'. This file is the result of 'Program.py'.
6. categoriesbyrating.csv is the file which contains the 'Video Categories' arranged in order of decreasing average rating for that category. This file is the result of 'Program.py'.
7. sortedbypopularity.csv is the file which contains the data with all attributes but the data is arranged in order of decreasing popularity score. This score was obtained by a simple formula(mentioned in 'Program.py'). This file is the result of 'Program.py'.
8. top10videosbyrating.csv is the file which contains the top 10 videos arranged in order of decreasing rating score. This file is the result of 'Program.py'.


## YouTube Dataset ('youtubedata.txt')

Variable | Description
----------|--------------
Video id | a unique id for a video
uploader of the video | name of the channel by whoom the video was uploaded
Interval between the day of establishment | time since the video was uploaded
Category of the video | which category or the topic the video belongs to
Length of the video | Length of the video in minutes
Number of views for the video | the number of times the video has been watched
Rating on the video | a rating score given by viewers, out of 5
Number of ratings given for the video | number of ratings given by viewwers
Number of comments | number of comments for the video
Related video ids | ids of other videos related to the video								
