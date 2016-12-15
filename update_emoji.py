#!/usr/bin/env python

import codecs
import collections
import json
import re
import os

json_path = os.path.relpath(
    os.path.join('.', 'node_modules', 'emojilib', 'emojis.json'))
snippets_path = os.path.join('snippets', 'Emoji')

CONTENT_FORMAT = u"""[snippet]
body = "{emoji}"
syntax = "None"
tag = "Emoji"
title = ":{shortname}:"
"""

# Read the json file
with open(json_path) as f:
    json_dict = json.loads(f.read())

emoji_keywords = collections.defaultdict(set)


def valid_emoji_shortname(shortname):
    pattern = re.compile(r'^[A-Za-z0-9_\-]+$')
    return pattern.match(shortname) is not None


def write_emoji(title, shortname):
    if not valid_emoji_shortname(shortname):
        return
    filename = u'{}.toml'.format(shortname)
    contents = CONTENT_FORMAT.format(emoji=title, shortname=shortname)

    path = os.path.join(snippets_path, filename)

    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(contents)


# For every emoji in the json, create the snippet
for shortname, emoji in json_dict.items():
    title = emoji['char']

    for keyword in emoji['keywords']:
        emoji_keywords[keyword].add(title)

    write_emoji(title, shortname)

# For every keyword, see if there is only one emoji, if so, write it out
for keyword, emojis in emoji_keywords.items():
    if len(emojis) != 1:
        continue

    write_emoji(emojis.pop(), keyword)
