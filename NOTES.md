
ffmpeg -i in.mp4 -vf "scale=1920x1080:flags=lanczos,unsharp=7:7" -b:a 80k -b:v 2000k -c:a aac -c:v libx264 -preset veryslow out.mp4


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

# Merge audio and video, video can not have audio
ffmpeg -i video.mp4 -i audio.m4a -c:v copy -c:a aac output.mp4

# cutting video (ss = start time, t = duration)
ffmpeg -i video.mp4 -ss 00:02:54 -t 00:00:05 -async 1 -c copy cut.mp4