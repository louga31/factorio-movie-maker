# screenshot_combiner.py

"""
Recombines the output screenshots from Factorio into a viewable video.
"""

import imageio

import os
import re


# Change this to wherever the images are
filepath = "C:\\Users\\tfsch\\AppData\\Roaming\\Factorio\\script-output\\video-output"

writer = imageio.get_writer("output.mp4", fps=25) # 25 fps in my case

file_list = []
for file in os.listdir(filepath):
    file_list.append(os.path.join(filepath, file))

# Sort by indexed number instead of lexographically
def natural_sort(s):
    def tryint(s):
        try:
            return int(s)
        except ValueError:
            return s
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]
file_list.sort(key=natural_sort)

for file in file_list:
    print(file)
    writer.append_data(imageio.imread(file))

writer.close()