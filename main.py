import glob, os, subprocess
servers = []
p = []
files = glob.glob("./*.json")
for i in files:
    if os.path.isdir(i.replace(".json", "")):
        servers.append(i)
