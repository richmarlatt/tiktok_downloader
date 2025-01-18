import os
import json
import requests
import argparse


# Function to download a video from a URL
def download_video(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}")


# Main function to parse JSON and download videos
def main(json_file_path):
    # Create directory if it doesn't exist
    os.makedirs('TikTok_Videos', exist_ok=True)

    # Read and parse the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Navigate to the Video.Videos.VideoList section
    video_list = data.get('Video', {}).get('Videos', {}).get('VideoList', [])

    # Loop through each video item
    for video in video_list:
        link = video.get('Link')
        print(f"Found link: {link}")
        if link:
            # Extract a shorter file name from the URL
            video_id = link.split('/')[-1].split('?')[0]  # Get the last part of the URL path before query params
            video_name = os.path.join('TikTok_Videos', video_id + '.mp4')
            print(f"Saving video as: {video_name}")
            # Download and save the video
            download_video(link, video_name)


# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Download videos from a JSON file.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    return parser.parse_args()


if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()
    # Check if the JSON file argument is provided
    if not args.json_file:
        print("Error: No JSON file provided.")
        print("Usage: python tiktok_downloader.py <user_data_tiktok.json>")
        exit(1)
    # Run the main function with the provided JSON file
    main(args.json_file)
