# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


# TODO:
#   Auto download and scan files in dict dir
#   write GUI frame for lang selections

# Enable/Disable as necessary, but avoid language conflicts
DICT_FILES = {
    "en-US-3-0",
    # "en-GB-3-0",

    # Add your beloved dicts here:
    # "xx-XX-3-0",
    # "xx-XX-3-0",

    # "fr-FR-3-0"
}


from aqt.qt import *
from aqt.webview import AnkiWebView
from anki.hooks import wrap, addHook
from anki.lang import _
from functools import partial

from .config import Config

ADDON_NAME='SpellingPolice'
conf = Config(ADDON_NAME)


def replaceMisspelledWord(page, sug_word):
    page.replaceMisspelledWord(sug_word)

def onContextMenuEvent(editor, menu):
    p=editor._page.profile()
    data=editor._page.contextMenuData()
    b=p.isSpellCheckEnabled()
    menu.addSeparator()
    a=menu.addAction(_("Spelling Police"))
    a.setCheckable(True)
    a.setChecked(b)
    a.triggered.connect(lambda:p.setSpellCheckEnabled(not b))
    if b and conf.get("duck_mode", False):
        firstAct=menu.actions()[0]
        for sug_word in data.spellCheckerSuggestions():
            a=menu.addAction(sug_word)
            menu.insertAction(firstAct, a)
            a.triggered.connect(partial(replaceMisspelledWord, editor._page, sug_word))
            if conf.get("bold_text", True):
                f=a.font()
                f.setBold(True)
                a.setFont(f)
        menu.insertSeparator(firstAct)

addHook("EditorWebView.contextMenuEvent", onContextMenuEvent)


def setupBDIC(web, parent=None):
    p=web._page.profile()
    p.setSpellCheckEnabled(conf.get("auto_startup", False))
    p.setSpellCheckLanguages(DICT_FILES)

AnkiWebView.__init__=wrap(AnkiWebView.__init__, setupBDIC, "after")
