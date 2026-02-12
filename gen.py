#!/usr/bin/env python

import re
import os
import sys
import json
import pprint
import subprocess
from pathlib import Path

def get_notes(root):
    result = []
    for root, dirs, fnames in os.walk(root):
        if '.git' in root:
            continue

        #print(f'root: {root}')
        #print(f'dirs: {dirs}')
        #print(f'fnames: {fnames}')

        for dir in dirs:
            pass
        for fname in fnames:
            #fpath = os.path.join(root, fname)
            #result.append(fpath)
            result.append(fname)

    return result

def foo():
    dir2fpaths = {}
    for fpath in dirtree('.'):
        if fpath.endswith('.excalidraw'):
            continue
        dname, _ = os.path.split(fpath)
        dname = dname.replace('./', '')
        dir2fpaths[dname] = dir2fpaths.get(dname, []) + [fpath]

    print('''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>title</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <script src="../d3/d3.min.js"></script>
        <script src="myscript0.js"></script>
      </head>
      <body>
        <!-- page content -->
    ''')

    for dname in dir2fpaths:
        print(f'<b>{dname}:</b>')

        for fpath in dir2fpaths[dname]:
            _, fname = os.path.split(fpath)
            basename, ext = os.path.splitext(fname)
            print(f'<a href="{fpath}">{basename}</a> | ')

        print('<br>')

    print('''
      </body>
    </html>
    ''')

def last_content_modification_date(filepath: str, follow_renames: bool = True) -> str:
    """
    Returns the ISO 8601 date of the last commit that changed the file's contents.
    """
    args = ["git", "log", "-1", "--format=%ci", "--", filepath]
    if follow_renames:
        args.insert(2, "--follow")

    try:
        result = subprocess.run(
            args,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        tmp = result.stdout.strip()
        m = re.match(r'^(\d\d\d\d-\d\d-\d\d)', tmp)
        assert m, breakpoint()
        return m.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")
        return None

# Example
print(last_content_modification_date("src/main.py"))

if __name__ == '__main__':
    notes = get_notes('./notes')

    #datastruct = {}
    #for fname in notes:
    #    datastruct[fname] = []

    datastruct = {}
    for fname in notes:
        fpath = os.path.join('notes', fname)
        mtime = last_content_modification_date(fpath)
        datastruct[fname] = mtime

    pprint.pprint(datastruct)

