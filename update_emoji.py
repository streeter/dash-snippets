#!/usr/bin/env python

import codecs
import os
import plistlib

plist_path = os.path.relpath(
    os.path.join('.', 'Macmoji', 'emoji substitutions.plist'))

# Read the plist
plist = plistlib.readPlist(plist_path)

# For every emoji in the plist, create the snippet
for emoji in plist:
    title = emoji['phrase']
    shortcut = emoji['shortcut']

    filename = '{}.toml'.format(shortcut.replace(':', '').replace('+', ''))

    contents = u"""[snippet]
body = "{emoji}"
syntax = "None"
tag = "Emoji"
title = "{shortcut}"
""".format(emoji=title, shortcut=shortcut)

    path = os.path.join('snippets', 'Emoji', filename)

    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(contents)
