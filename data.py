import json
from utils import csv_to_json

if __name__ == "__main__":
    # path
    csv_path = './data/bad_clips_keypoints.csv'
    json_path = './data/bad_clips.json'

    # json file
    json_data = csv_to_json(csv_path, json_path)