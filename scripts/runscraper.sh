
# Typical usage is to run the script and shut down the VM
# once the script is executed

python3 src/insta-comment-scraper.py

gcloud compute instances stop insta-worker-2 --zone=us-central1-a
