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

input_file = os.path.join('testdata', 'ids.txt')

with open(input_file, 'r') as f:
    ids_list = f.read()
    ids_list = ids_list.split('\n')

FIELD_SEPARATOR = "xxFLDxx"

META_DATA_PATTERN = (
    "{shortcode}" + FIELD_SEPARATOR +
    "{date_utc}" + FIELD_SEPARATOR +
    "{profile}" + FIELD_SEPARATOR +
    "{caption}" + FIELD_SEPARATOR + 
    "{likes}" + FIELD_SEPARATOR + 
    "{comments}"
)

# login with instaloader -l "your-instagram-login"
# the session cookie will be saved to ~/.config/instaloader/session-your-username 
LOGIN_USER_NAME = "your-instagram-username"

L = Instaloader(
    dirname_pattern=os.path.join('testdata', '{profile}'),
    filename_pattern="{shortcode}",
    download_pictures=True,
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=True,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern=META_DATA_PATTERN
)

L.load_session_from_file(LOGIN_USER_NAME)

for username in ids_list:
    print("Downloading data for :", username)
    L.download_profile(username)