#!/usr/bin/env python

import codecs
import collections
import itertools
import json
import re
import os

from slugger import Slugger

json_path = os.path.relpath(
    os.path.join('.', 'node_modules', 'emojilib', 'emojis.json'))
snippets_path = os.path.join('snippets', 'Emoji')

CONTENT_FORMAT = u"""[snippet]
body = "{emoji}"
syntax = "None"
tag = "Emoji"
title = ":{shortname}:"
"""

# These override other stuff
ALIASES = {
    'tada': [
        'celebration',
    ],
}

slugger = Slugger(lang='en_US')

# Read the json file
with open(json_path) as f:
    json_dict = json.loads(f.read())

emoji_keywords = collections.defaultdict(list)


def create_shortname(name):
    if re.match(r'^[a-zA-Z0-9\+\-\_]+$', name):
        return name

    return slugger.sluggify(name)


def write_emoji(emoji_symbol, emoji_name):
    filename = u'{}.toml'.format(emoji_name)
    contents = CONTENT_FORMAT.format(
        emoji=emoji_symbol, shortname=emoji_name)

    path = os.path.join(snippets_path, filename)

    with codecs.open(path, 'w', 'utf-8') as emoji_file:
        emoji_file.write(contents)


# Populate the set of keywords
for shortname, emoji_dict in json_dict.items():
    emoji = emoji_dict['char']

    valid_shortname = create_shortname(shortname)
    if not valid_shortname:
        print(u'Shortname {} is not a valid emoji title'.format(
            shortname))
        continue

    # Add the primary to the front of the array, since that is always the one
    # we want.
    emoji_keywords[valid_shortname].insert(0, emoji)

    local_aliases = ALIASES.get(valid_shortname, [])
    for alias in local_aliases:
        emoji_keywords[alias].insert(0, emoji)

    # Split the aliases up
    shortname_pieces = valid_shortname.split('_')

    # Add all aliases to the end of the array
    for keyword in itertools.chain(shortname_pieces, emoji_dict['keywords']):
        valid_keyword = create_shortname(keyword)
        if not valid_keyword:
            print(u'Shortname {} is not a valid emoji keyword'.format(
                keyword))
            continue
        emoji_keywords[valid_keyword].append(emoji)

# For every keyword, write it out.
for keyword, emojis in emoji_keywords.items():
    write_emoji(emojis[0], keyword)
