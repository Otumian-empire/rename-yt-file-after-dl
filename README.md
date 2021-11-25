# Rename youtube-file after download
After downloading videos from yt, you realized that the order of the video has changed. It will take you time to rename all of them one after the other.

## run script
- download or put `script.py` into the said videos folder
- open the folder in the terminal
- run `python script.py yt-playlist-url`

## You can modify the scripts
This scripts reorders the file names by adding numbers to the beginning from 1 to n, where n is the number of files there is. 
`new_video_title = str(counter+1) + " " + video_title`, this line does the renaming and a counter variable before the loops. Create a list for the new names and change the code to use index instead of `in` keyword. If there is other approaches too, let me know how.
