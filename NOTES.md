# Pyinstaller
c:\Users\kinga\AppData\Roaming\Python\Python38\Scripts\pyinstaller.exe --onefile vrtUI.py

ffmpeg -i infile outfile

ffmpeg -i in.mp4 -vf "scale=1920x1080:flags=lanczos,unsharp=7:7" -b:a 150k -b:v 2000k out.mp4

#specify bitrate
-b:a <bitrate>k
-b:v <bitrate>k

# double the volume
-filter:a "volume=2"

# scale width to 2/3 of input file and hight to keep aspect ratio
-filter:v "scale=w=2/3*in_w:h=-1"

# rotate 45 degrees
-filter:v "rotate=45*PI/180"

# sharpen
-filter "unsharp=lx=10:ly=10"

# blur
-filter "unsharp=la=-1.5"

# audio visualisation
ffmpeg -i xx.mp3 -filter_complex "showwaves=mode=cline:size=1280x720:colors=#FFFFFF|#DDDDDD" output.mp4

# audio in pianokeys
-filter_complex "showcqt"

# upscalen
-vf scale=1920x1080:flags=lanczos
