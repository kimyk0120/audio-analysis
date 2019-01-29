# Keunwoo Choi
# This example crawl snoring sound by searching keyword 'snore'.

from __future__ import print_function
import freesound  # $ git clone https://github.com/MTG/freesound-python
import os
import sys

api_key = 'YOUR_API_KEY'
folder = 'data_freesound/'  # folder to save

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(api_key)

try:
    os.mkdir(folder)
except:
    pass

# Search Example
print("Searching for 'snore':")
print("----------------------------")

results_pager = freesound_client.text_search(
    query="snore",
    # filter="tag:tenuto duration:[1.0 TO 15.0]",
    sort="rating_desc",
    fields="id,name,previews,username"
)
print("Num results:", results_pager.count)
print("\t----- PAGE 1 -----")
for sound in results_pager:
    print("\t-", sound.name, "by", sound.username)
    filename = sound.id + '_' + sound.name.replace(u'/', '_') + ".mp3"
    if not os.path.exists(folder + filename):
        sound.retrieve_preview(folder, filename)

for page_idx in range(results_pager.count):
    print("\t----- PAGE {} -----".format())
    results_pager = results_pager.next_page(page_idx + 2)
    for sound in results_pager:
        print("\t-", sound.name, "by", sound.username)
        filename = sound.id + '_' + sound.name.replace(u'/', '_') + ".mp3"
        if not os.path.exists(folder + filename):
            sound.retrieve_preview(folder, filename)
print()
