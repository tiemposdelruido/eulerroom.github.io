#!/usr/bin/python

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
import getopt
import sys
import string


gd = gdata.spreadsheet.service.SpreadsheetsService()
gd.email = 'alex@slab.org'
gd.password = 'otgshp00'
gd.source = 'grab_roster'
gd.ProgrammaticLogin()

key = 'tC6dGwi4qexL3AM0J3TL-Mg'
feed = gd.GetWorksheetsFeed(key)
id_parts = feed.entry[0].id.text.split('/')
worksheet_id = id_parts[len(id_parts) - 1]
feed = gd.GetListFeed(key, worksheet_id)

print "players = ["
for i, entry in enumerate(feed.entry):
    text = ''

    if entry.custom['homepage'].text:
        text = text + '<a href="%s">%s</a>' % (entry.custom['homepage'].text, entry.custom['name'].text)
    else:
        text = text + entry.custom['name'].text

    string.replace(text, "'", "\\'")
    
    text = "'%s'" % text
    if i < (len(feed.entry) - 1):
        text = text + ','
    print text
print '];'
