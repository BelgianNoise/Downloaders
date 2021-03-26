import sys, requests, re, subprocess, os
import youtube_dl

def getList(url):
    response = requests.get(url)
    contents = response.content.decode('utf-8')
    matches = re.findall(r'<vrtnu-tile id=".*?" link="(.*?)"', contents)
    res = []
    helper = re.findall(r'a-z\/([^/]+)\/', url)[0]
    for m in matches:
        if helper in m:
            res.append(m)
    return res

def downloadList(listt, path, us, pw):
    os.chdir(path)
    for m in listt:
        print("Downloading: '" + re.findall(r'/([^/]*)/$', m)[0] + "'...")
        ydl_opts = {
            'username': us,
            'password': pw,
            'quiet': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'vrt.be{m}'])
        # command = f'youtube-dl vrt.be{m} --username {us} --password {pw}'
        # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, shell=True)
        # out, error = process.communicate()
        print("Finished downloading: " + re.findall(r'/([^/]*)/$', m)[0])
