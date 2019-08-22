"""Collecting profile information of users who liked posts on Instagram

We loop over the directories of users for whom the engagement data was
collected in src/insta-comment-scraper.py and for each of these posts
we build a list of profiles who likes these posts.

This is useful if the intent is to recreate the sub-network of users
who like or comment on the posts from a person of interest

This script is meant to be called from the shell script that 
manages the VM (see /scripts/runscraper.sh)
"""

import re
import os
import glob
import pickle 

from instaloader import Instaloader
from instaloader import Post

from tqdm import tqdm

# The input file contains ids of users to collect data from
# one instagram id per line

input_file = os.path.join('data', 'raw', '2019-03-31_instagram-ids.txt')


with open(input_file, 'r') as f:
    ids_list = f.read()
    ids_list = ids_list.split('\n')
    

L = Instaloader()

for username in ids_list:
    print("Downloading data for :", username)
    
    post_likes = {}

    data_dir = os.path.join("data", "raw", username)
    ce_files_lst = glob.glob(os.path.join(data_dir, "*.txt"))
    
    for ce_file in tqdm(ce_files_lst):
        try:
            post_shortcode = re.sub(data_dir+'/', 
                                    '', 
                                    os.path.splitext(ce_file)[0])
        
            post = Post.from_shortcode(L.context, post_shortcode)
            profiles_that_liked_post = []
        
            for profile in post.get_likes():
                profiles_that_liked_post.append(profile.userid)
            
            post_likes[post_shortcode] = profiles_that_liked_post
        except Exception:
            continue
        
    with open(data_dir+"-likes.p", 'wb') as handle:
        pickle.dump(post_likes, handle, protocol=pickle.HIGHEST_PROTOCOL)
            