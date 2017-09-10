#!/usr/bin/env python

import wget
import os
import shutil

FONT_URL = "https://gitlab.com/smc/%s/-/jobs/artifacts/master/raw/ttfs/%s?job=generate-ttf"

font_details = {
        "rachana": ["Rachana-Regular", "Rachana-Bold"],
        "meera": ["Meera-Regular"],
        "manjari": ["Manjari-Regular", "Manjari-Bold", "Manjari-Thin"],
        "raghumalayalamsans": ["RaghuMalayalamSans-Regular"],
        "dyuthi": ["Dyuthi-Regular"],
        "keraleeyam": ["Keraleeyam-Regular"],
        "uroob": ["Uroob-Regular"],
        "chilanka": ["Chilanka-Regular"],
        "karumbi": ["Karumbi-Regular"]
        #TODO Fix Suruma
        }

for repo, fonts in font_details.items():
    folder = "downloads/fonts/" + repo + "/"
    shutil.rmtree(folder, ignore_errors=True)
    os.makedirs(folder)
    for font in fonts:
        for file_format in ["otf", "ttf", "woff", "woff2"]:
            filename = font + "." + file_format
            url = FONT_URL % (repo, filename)
            try:
                print("Downloading %s to %s" % (filename, folder))
                wget.download(url=url, out=folder, bar=None)
            except:
                print("File not found")
                continue

#TODO Add making a zip out of each folder
