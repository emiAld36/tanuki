from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
import os
import yt_dlp
import platform

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
            size_hint=(2, .7)
        )
        self.window.add_widget(self.user)

        # Button widget for video download
        self.button = Button(
            text="Download Video",
            size_hint=(1, 0.5),
            bold=True,
            background_color='blue'
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Button widget for audio-only download
        self.audio_button = Button(
            text="Download Audio Only",
            size_hint=(1, 0.5),
            bold=True,
            background_color='blue'
        )
        self.audio_button.bind(on_press=self.callback_audio)
        self.window.add_widget(self.audio_button)
        
        # Status label to show download status
        self.status_label = Label(
            text="",
            font_size=15,
            color='white'
        )
        self.window.add_widget(self.status_label)

        return self.window

    def get_download_path(self):
        """Returns the default download path based on the operating system."""
        if platform.system() == "Darwin":  # macOS
            return os.path.expanduser("~/Downloads")
        elif platform.system() == "Windows":  # Windows
            return os.path.join(os.path.expanduser("~"), "Downloads")
        else:  # Linux or other systems (optional)
            return os.path.expanduser("~/Downloads")

    def show_popup(self, title, message):
        """Shows a simple popup with the download status"""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.3))
        popup.open()

    def callback(self, instance):
        """Handles video downloads."""
        dir = self.get_download_path()
        url = self.user.text.strip()  # Get user input and remove spaces
        self.status_label.text = "Downloading video..."
        
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  # Download best quality
                'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),  # Save path
                'quiet': False,  # Show output logs
                'nocheckcertificate': True  # Bypass SSL certificate errors
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "Download complete!"
            self.show_popup("Success", "Video download complete!")
        except Exception as e:
            self.status_label.text = "Error downloading video."
            self.show_popup("Error", f"Error downloading video: {e}")

    def callback_audio(self, instance):
        """Handles audio-only downloads."""
        dir = self.get_download_path()
        url = self.user.text.strip()  # Get user input and remove spaces
        self.status_label.text = "Downloading audio..."
        
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
            self.status_label.text = "Audio download complete!"
            self.show_popup("Success", "Audio download complete!")
        except Exception as e:
            self.status_label.text = "Error downloading audio."
            self.show_popup("Error", f"Error downloading audio: {e}")

if __name__ == "__main__":
    Tanuki().run()
