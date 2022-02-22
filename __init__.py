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
    json_path: str = "/Users/oliver/git/anki-kindle-import/out.json"
    f: str = open(json_path)
    arr = json.load(f, object_pairs_hook=OrderedDict)
    # json.dumps(arr);
    print('hello')
    for i in range(0, len(arr), 2):
        sentence = arr[i]["Highlight"]["sentence"]
        terms = arr[i+1]["Note"]["terms"]
        # for each term
        for term in terms:
            print(term)




    # # get the number of cards in the current collection, which is stored in
    # # the main window
    # totalCards = mw.col.cardCount()
    # tags = mw.col.tags.all();

    # list = {}
    # # dict that we can sort
    # for tag in tags:
    #     numOfCardWithTag = mw.col.find_cards("tag:" + tag).__len__()
    #     list[tag] = numOfCardWithTag
    # out = "name:percentage of total (cards in total)\n"
    # # sort the dict
    # for x,y in sorted(list.items(), key=lambda x: x[1], reverse=True):
    #     out += "{}:{:.2%} ({})\n".format(x, y / totalCards, y)
    # showInfo(out)

# create a new menu item, "test"
action = QAction("Import cards from kindle clippings (exported by anki-kindle-import-rs)", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, importCards)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
