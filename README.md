# tanuki
**Tanuki Music Downloader**
=====================================

A simple GUI application for downloading music videos and audio files from 
YouTube.

**Description**
---------------

This application allows users to download music videos and audio files 
from YouTube. It uses the `yt_dlp` library to handle video downloads and 
includes features such as best quality settings, output directory 
selection, and post-processing for audio extraction.

**Features**

*   Download music videos in high-quality
*   Download audio-only tracks with customizable quality settings
*   Customizable output directory (default: `~/Music/ytRacoonDownloads`)
*   Supports HTTPS and HTTP connections
*   Handles SSL certificate errors

**Requirements**
----------------

*   Python 3.6+
*   Kivy 1.9+ (for GUI development)
*   yt_dlp library (`pip install yt-dlp`)

**Installation**
---------------

1.  Clone or download the repository.
2.  Install required dependencies: `pip install kivy yt-dlp`
3.  Run the application using `python tanuki.py`

**Usage**
--------

1.  Launch the application.
2.  Enter the YouTube video URL in the input field.
3.  Select the desired download options (best quality, audio-only, etc.) 
and output directory.
4.  Click "Download Video" or "Download Audio Only" to start the download 
process.

**Troubleshooting**
------------------

*   Make sure you have the required dependencies installed.
*   Check that the output directory is writable by the application.
*   If encountering errors during downloads, try restarting the 
application or checking the console logs for more information.

**Contributing**
---------------

Feel free to contribute to this project by submitting pull requests or 
issues. Contributions are welcome and appreciated!

**License**
-----------

This project is licensed under the [MIT 
License](https://opensource.org/licenses/MIT).

**Changelog**
-------------

*   v1.0: Initial release with basic functionality.
*   Future updates will include feature improvements, bug fixes, and 
    security patches.
