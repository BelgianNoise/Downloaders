# Include modules
import argparse, sys
import os.path
from os import path
import linecache
import re
import subprocess

# Initiate the parser
parser = argparse.ArgumentParser(description="Download (and encode) a list of m3u8 links. Created to help downloading from goplay.be. Default settings are configured to download/encode 540p streams.")
parser.add_argument( "-f", "--file", help="Name of the file that contains list of m3u8 links")
parser.add_argument("--downloadOnly", help="Only download, don't encode. Very light on the CPU", action="store_true")
parser.add_argument("--useDefaultFileNaming", help="Don't use my personalised naming conventions", action="store_true")
parser.add_argument("--ba", help="The audio bitrate to encode in in kbps")
parser.add_argument("--bv", help="The video bitrate to encode in in kbps")
parser.add_argument("--ca", help="The audio codec to be used")
parser.add_argument("--cv", help="The video codec to be used")
parser.add_argument("--preset", help="The encode preset to be sued")
args = parser.parse_args()

# Handle input variable FILE

file = args.file
if not file:
    file = "H:\\Films\\ffmpegger\\00_Downloadm3u8.txt"
    print(f"No value was provided for '-f' or '--file', using default '{file}'")
if not path.exists(file):
    sys.exit(f"File does not exist!  -  '{file}'")
if not file.endswith(".txt"):
    sys.exit(f"File is not of .txt format!  -  '{file}'")

# Handle input variable DOWNLOADONLY

downloadOnly = args.downloadOnly

# Handle input variable USEDEFAULTFILENAMING

useDefaultFileNaming = args.useDefaultFileNaming

# Handle input variable BA
bitrateAudio = args.ba
if not bitrateAudio:
    bitrateAudio = "80"
    print(f"No value was provided for '--ba', using default '{bitrateAudio}'")
# Handle input variable BV
bitrateVideo = args.bv
if not bitrateVideo:
    bitrateVideo = "800"
    print(f"No value was provided for '--bv', using default '{bitrateVideo}'")
# Handle input variable CA
codecAudio = args.ca
if not codecAudio:
    codecAudio = "aac"
    print(f"No value was provided for '--ca', using default '{codecAudio}'")
# Handle input variable CV
codecVideo = args.ca
if not codecVideo:
    codecVideo = "libx264"
    print(f"No value was provided for '--cv', using default '{codecVideo}'")
# Handle input variable PRESET
preset = args.preset
if not preset:
    preset = "veryslow"
    print(f"No value was provided for '--preset', using default '{preset}'")

# Log current settings
print("\n#######################\n")
if downloadOnly:
    print(f"Running in downloadOnly-mode with these settings:\n    File: {file}\n    Using default file naming: {useDefaultFileNaming}")
else:
    print(f"Running with these settings:\n    File: {file}\n    Audio Codec: {codecAudio}\n    Audio Bitrate: {bitrateAudio}kbps\n    Video Codec: {codecVideo}\n    Video Bitrate: {bitrateVideo}kbps\n    Encode Preset: {preset}\n    Using default file naming: {useDefaultFileNaming}")
print("\n#######################\n")

# Helper functions for below
def deleteFirstLineFromFile(file):
    read = open(file, "r")
    lines = read.readlines()
    read.close()
    del lines[0]
    new_file = open(file, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def getFirstLineFromFile(file):
    read = open(file, "r")
    lines = read.readlines()
    read.close()
    return lines[0] if len(lines) > 0 else None

def camelCasewithDots(string):
    split = string.replace('_', ' ').title().replace(' ', '.')
    return split

def generateOutputFileName(line, useDefaultFileNaming, downloadOnly):
    regexp = re.compile(r'.*\/(.*)_(\d{1,2})_(\d{1,2})_.*\/.*\/index.m3u8')
    match = regexp.match(line)
    print(f"match {match}")
    if match:
        name = camelCasewithDots(match.group(1))
        season = f"0{match.group(2)}" if len(match.group(2)) == 1 else match.group(2)
        episode = f"0{match.group(3)}" if len(match.group(3)) == 1 else match.group(3)
        if useDefaultFileNaming or downloadOnly:
            return f"{name}.S{season}E{episode}.mp4"
        else:
            return f"{name}.S{season}E{episode}.540p.WEB-DL.{bitrateVideo}kbps.{codecVideo[3:]}.BENOISE.mp4"
    else:
        regexp = re.compile(r'.*\/(.*)_.*\/.*\/index.m3u8')
        match = regexp.match(line)
        if match:
            name = camelCasewithDots(match.group(1))
            return f"{name}.mp4"
        else:
            return None

# Read first line from file
firstLine = getFirstLineFromFile(file)

while firstLine:
    if not len(firstLine.strip()) == 0:
        outputFileName = generateOutputFileName(firstLine, useDefaultFileNaming, downloadOnly)

        if outputFileName:
            print("\n################################################################\n")
            command = f"ffmpeg -i {firstLine}"
            if not downloadOnly:
                command += f" -b:a {bitrateAudio}k -c:a {codecAudio}"
                command += f" -b:v {bitrateVideo}k -c:v {codecVideo}"
                command += f" -preset {preset}"
            else:
                command += " -vcodec copy -acodec copy -c copy"

            command += f" {outputFileName}"
            print(f"Executing command: {command}")

            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, shell=True)
            out, error = process.communicate()
            
            print(f"Finished downloading and encoding: {outputFileName}")
        else:
            print(f"Invalid line: {firstLine}")

    deleteFirstLineFromFile(file)
    firstLine = getFirstLineFromFile(file)

print("\n################################################################\n")
print("    Done Downloading and encoding all files!")
        
