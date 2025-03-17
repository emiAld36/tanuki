from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
import yt_dlp


#this app was intented to be used for downloading music for sampling
#this app saved downloads in the music fold of macOS
#if you are on windows, or would like a different path
#please change path below

class Tanuki(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Image widget
        self.window.add_widget(Image(source="racoonLogo.png"))

        # Label widget
        self.greeting = Label(
            text="Enter video URL",
            font_size=20,
            color='white'
        )
        self.window.add_widget(self.greeting)

        # User input
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)

        # Button widget for video download
        self.button = Button(
            text="Download Video",
            size_hint=(1, 0.5),
            bold=True,
            background_color='red'
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Button widget for audio-only download
        self.audio_button = Button(
            text="Download Audio Only",
            size_hint=(1, 0.5),
            bold=True,
            background_color='red'
        )
        self.audio_button.bind(on_press=self.callback_audio)
        self.window.add_widget(self.audio_button)

        return self.window

    def get_download_path(self):
        """Returns the path to the ytRacoonDownloads folder inside ~/Music."""
        dir_path = os.path.join(os.path.expanduser("~"), "Music", "ytRacoonDownloads")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)  # Create directory if it does not exist
        return dir_path

    def callback(self, instance):
        """Handles video downloads."""
        dir = self.get_download_path()
        url = self.user.text.strip()  # Get user input and remove spaces

        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  # Download best quality
                'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),  # Save path
                'quiet': False,  # Show output logs
                'nocheckcertificate': True  # Bypass SSL certificate errors
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Download complete!")
        except Exception as e:
            print(f"Error downloading video: {e}")

    def callback_audio(self, instance):
        """Handles audio-only downloads."""
        dir = self.get_download_path()
        url = self.user.text.strip()  # Get user input and remove spaces

        try:
            ydl_opts = {
                'format': 'bestaudio/best',  # Download audio only
                'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),  # Save path
                'quiet': False,  # Show output logs
                'nocheckcertificate': True,  # Bypass SSL certificate errors
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Audio download complete!")
        except Exception as e:
            print(f"Error downloading audio: {e}")

if __name__ == "__main__":
    Tanuki().run()
