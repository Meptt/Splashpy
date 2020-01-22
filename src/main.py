import json
import os
import ctypes
from urllib import request
import tkinter


screen = tkinter.Tk()
screen_width = screen.winfo_width()
screen_height = screen.winfo_height()

# unsplash api key
api_key = '11424b845fa388c2191aefe2d41bfff9dfe6a47cc51d0023463e5783871b2c4d'


# Constants
TMP = os.path.join(os.getcwd() + "\\image.jpg")
URL = 'https://api.unsplash.com/photos/random?client_id=' + api_key

# Change the Background script
def set_wallpaper_windows(filename):  # pragma: no cover
        """Set a file as windows Wallpaper."""

        SPI_SETDESKWALLPAPER = 0x14  # which command (20)
        SPIF_UPDATEINIFILE = 0x2  # forces instant update
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                                   0,
                                                   filename,
                                                   SPIF_UPDATEINIFILE)

# Wallpaper downloader and info getter
def get_wallpaper():
	wallpaper = request.urlopen(URL)
    json_string = wallpaper.read()
    wallpaper.close()
    parsed_json = json.loads(json_string)
    print(f"""Details : Photo From : {parsed_json['user']['name']}
    	Vieved Users : {parsed_json['views']}
    	Download Count : {parsed_json['downloads']}
    	Camera : {parsed_json['exif']['model']}
	Width : {parsed_json['width']} Height : {parsed_json['height']}""")
    photodetails = parsed_json['urls']['full']
    request.urlretrieve(photodetails, TMP) # Location where we download the image to.

# main block
try:
	if screen_height >= parsed_json['height']:
		get_wallpaper()
	else:
		print("Try again")

except KeyboardInterrupt:
    print("Eroororororororororor")
