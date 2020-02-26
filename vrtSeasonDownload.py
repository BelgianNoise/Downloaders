import sys, requests, re, subprocess, os

url = ""
path = "/mnt/h/Films"
if len(sys.argv) > 1:
    url = sys.argv[1]
    if len(sys.argv) > 2:
        path = sys.argv[2]
else:
    sys.exit("This script requires at least 1 parameter:\n   1: The link to the vrt.nu page\n   2: (Optional) The path you want to download the videos to. This defaults to '"+path+"' for my own convenience.\n\n !!! This script requires you to have youtube-dl installed (apt install youtube-dl) !!!")

username = str(input('username: '))
password = str(input('password: '))

response = requests.get(url)
contents = response.content
matches = re.findall(r'<nui-tile href="(.*?)"', contents)
print("All videos being downloaded("+str(len(matches))+"): ")

for m in matches:
    print(m)

os.chdir(path)
for m in matches:
    print("Downloading: '" + re.findall(r'/([^/]*)/$', m)[0] + "'...")
    command = "youtube-dl vrt.be" + m + " --username "+username+" --password "+password 
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
