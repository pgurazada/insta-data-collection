import os
import pandas as pd

from pathlib import Path
from instaloader import Instaloader

from tqdm import tqdm

USERNAME = ""
FIELD_SEPARATOR = "xxFLDxx"

META_DATA = ("{shortcode}" + FIELD_SEPARATOR +
             "{date_utc}" + FIELD_SEPARATOR +
             "{profile}" + FIELD_SEPARATOR +
             "{caption}")

insta_data_file = Path("data",
                       "processed",
                       "insta-ids.csv")

insta_data = (pd.read_csv(insta_data_file,
                          header=None,
                          names=['insta_id']))

L = Instaloader(dirname_pattern=os.path.join('data', 'raw', '{profile}'),
                filename_pattern="{shortcode}",
                download_pictures=False,
                download_videos=False,
                download_video_thumbnails=False,
                download_geotags=False,
                download_comments=False,
                save_metadata=False,
                compress_json=False,
                post_metadata_txt_pattern=META_DATA)

L.load_session_from_file(USERNAME)

insta_ids = insta_data.insta_id.unique()

for insta_id in tqdm(insta_ids):
    try:
        L.download_profile(insta_id)
    except Exception:
        continue
