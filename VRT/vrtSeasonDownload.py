import sys, requests, re, subprocess, os
import youtube_dl

def getList(url):
    response = requests.get(url)
    contents = response.content.decode('utf-8')
    matches = re.findall(r'<nui-tile href="(.*?)"', contents)
    res = []
    for m in matches:
        res.append(m)
    return res

def downloadList(listt, path, us, pw):
    os.chdir(path)
    for m in listt:
        print("Downloading: '" + re.findall(r'/([^/]*)/$', m)[0] + "'...")
        # ydl_opts = {}
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     ydl.download(["vrt.be" + m])
        command = "youtube-dl vrt.be" + m + " --username "+us+" --password "+pw
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, shell=True)
        out, error = process.communicate()
        print(out)
