"""Collecting images, meta data and comments by id from Instagram

Loop over each id in an input .txt file and collect their posts from Instagram
For each profile a separate directory is created

For each profile, we collect:
1. The images they posted
2. Counts of the different types of engagement, i.e., likes and comments they received
3. Text of the comments received on the images

This script is meant to be called from the shell script that 
manages the VM (see /scripts/runscraper.sh)
"""

import os

from instaloader import Instaloader

# The input file contains ids of users to collect data from
# one instagram id per line

input_file = os.path.join('data', 'raw', '2019-03-31_instagram-ids.txt')

with open(input_file, 'r') as f:
    ids_list = f.read()
    ids_list = ids_list.split('\n')

L = Instaloader(dirname_pattern=os.path.join('data', 'raw', '{profile}'),
                filename_pattern="{shortcode}",
                download_pictures=True,
                download_videos=False,
                download_video_thumbnails=False,
                download_geotags=False,
                download_comments=True,
                save_metadata=False,
                compress_json=False,
                post_metadata_txt_pattern="{profile},{date_utc},{shortcode},{likes},{comments}")

for username in ids_list:
    print("Downloading data for :", username)
    L.download_profile(username)