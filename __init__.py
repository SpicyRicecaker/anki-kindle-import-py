# import the main window object (mw) from aqt
import json
from collections import OrderedDict
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.
def importCards() -> None:
    json_path: str = "/Users/oliver/git/anki-kindle-import-rs/out.json"
    f: str = open(json_path, 'r+', encoding='utf-8')
    arr = json.load(f, object_pairs_hook=OrderedDict)
    # json.dumps(arr);
    print('hello')
    for i in range(0, len(arr), 2):
        sentence = arr[i]["Highlight"]["sentence"]
        terms = arr[i+1]["Note"]["terms"]
        # for each term
        for term in terms:
            # code with inspiration from https://www.juliensobczak.com/write/2016/12/26/anki-scripting.html

            # set the note type for the card we're about to create to basic
            modelBasic = mw.col.models.by_name('Basic')

            # focus our misc. deck
            deck = mw.col.decks.by_name("misc")
            if (deck):
                mw.col.decks.select(deck['id'])

            # set our current model to basic. But this doesn't make sense,
            # shouldn't it e mw.col.model instead?
            mw.col.decks.current()['mid'] = modelBasic['id']

            # create a note with the focused model
            note = mw.col.newNote()

            # set the front and back accordingly 
            note["Front"] = term["definition"];
            note["Back"] = term["term"] + '<br><br>' + sentence;

            # add tags to card 
            tags = "book"
            note.set_tags_from_str(tags)
            # note.tags = mw.col.tags.split(tags)
            # m = note.note_type()
            # m['tags'] = note.tags
            # mw.col.models.save(m)

            # Add the note
            mw.col.addNote(note)
            mw.col.update_note(note)
    showInfo("successfully added notes")

# create a new menu item, "test"
action = QAction("Import cards from kindle clippings (exported by anki-kindle-import-rs, in a very specific folder)", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, importCards)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
