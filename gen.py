#!/usr/bin/env python

import os
import sys
import json
import pprint

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

if __name__ == '__main__':
    notes = get_notes('./notes')

    datastruct = {}
    for fname in notes:
        datastruct[fname] = []

    pprint.pprint(datastruct)

