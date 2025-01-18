# TikTok Video Downloader

This tool helps you download all your TikTok videos using the data file from your TikTok account. Follow these simple instructions to get started.

## Before You Begin

You'll need to:
1. Download your TikTok data (instructions below)
2. Install Python on your computer
3. Download the video downloader script

## Getting Your TikTok Data

For a detailed guide with screenshots showing exactly how to download your TikTok data, please see:
[How To Download Your TikTok Data](How_To_Download_Your_TikTok_Data.md)

Quick steps:
1. Open TikTok and go to your Profile
2. Click on the hamburger menu (three lines) in the top right
3. Go to Settings and Privacy
4. Scroll down to "Download your data"
5. Select "Request data" and choose JSON format
6. Wait for TikTok to prepare your data (you'll receive a notification)
7. Download your data when it's ready
8. Unzip the downloaded file and locate the `user_data_tiktok.json` file

## Installing Python (Windows 11)

1. Visit the official Python website: https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. After the download completes, open the installer
4. **Important**: Check the box that says "Add Python to PATH" at the bottom of the installer
5. Click "Install Now"
6. Wait for the installation to complete
7. To verify the installation:
   - Press the Windows key + R
   - Type `cmd` and press Enter
   - In the black window that appears, type `python --version`
   - If you see a version number, Python is installed correctly!

## Installing Python (MacOS)

1. Visit the official Python website: https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. After the download completes, open the installer package
4. Follow the installation prompts
5. To verify the installation:
   - Open Terminal (press Command + Space, type "Terminal", press Enter)
   - Type `python3 --version`
   - If you see a version number, Python is installed correctly!

## Downloading and Running the Video Downloader

1. Download `tiktok_downloader.py` from this GitHub repository:
   - Click the green "Code" button above
   - Select "Download ZIP"
   - Unzip the downloaded file

2. Place your `user_data_tiktok.json` file in the same folder as `tiktok_downloader.py`

3. Running the script:

### Windows:
- Open Command Prompt:
  - Press Windows key + R
  - Type `cmd` and press Enter
  - Type `cd` followed by a space
  - Drag the folder containing the script into the Command Prompt window
  - Press Enter
- Run the script by typing:
  ```
  python tiktok_downloader.py user_data_tiktok.json
  ```

### MacOS:
- Open Terminal:
  - Press Command + Space
  - Type "Terminal" and press Enter
  - Type `cd` followed by a space
  - Drag the folder containing the script into the Terminal window
  - Press Enter
- Run the script by typing:
  ```
  python3 tiktok_downloader.py user_data_tiktok.json
  ```

## What Happens Next

- The script will create a folder called "TikTok_Videos" where it will save all your videos
- You'll see the progress as each video downloads
- Wait until the script finishes - the time will depend on how many videos you have
- Your videos will be saved with their original titles in the TikTok_Videos folder

## Troubleshooting

If you see an error message:

1. Make sure Python is installed correctly by checking the version:
   - Windows: Open Command Prompt and type `python --version`
   - Mac: Open Terminal and type `python3 --version`

2. Check that both files are in the same folder:
   - `tiktok_downloader.py`
   - `user_data_tiktok.json`

3. Make sure you typed the command exactly as shown above

4. If you're still having issues, try:
   - Restarting your computer
   - Reinstalling Python
   - Making sure you checked "Add Python to PATH" during Windows installation

## Need Help?

If you're still having trouble, please:
1. Take a screenshot of any error messages
2. Create an issue on this GitHub repository
3. Include your operating system (Windows/Mac) and what steps you've tried

## Safety Note

Always download software from official sources:
- Python: https://www.python.org/downloads/
- This tool: Only from this GitHub repository
