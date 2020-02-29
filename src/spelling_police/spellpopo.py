# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


# TODO:
#   Auto download dicts from github

# Good news everyone!
# Dicts config has been moved to GUI manager
#    Tools > Dictionary Configuration
# No need to restart or edit anything now.


from aqt.qt import *
from aqt import mw
from aqt.webview import AnkiWebView
from anki.hooks import wrap, addHook
from anki.lang import _
from functools import partial

from .dict import DictionaryManager
from .config import Config

ADDON_NAME='SpellingPolice'
conf = Config(ADDON_NAME)

dictMan = DictionaryManager()


def replaceMisspelledWord(page, sug_word):
    page.replaceMisspelledWord(sug_word)

def onContextMenuEvent(web, menu):
    p=web._page.profile()

    # For Edit field during review
    if mw.state == "review":
        if not conf.get("check_during_review", False):
            return
        p.setSpellCheckLanguages(dictMan.getDictionaries())

    b=p.isSpellCheckEnabled()
    menu.addSeparator()
    a=menu.addAction(_("Spelling Police"))
    a.setCheckable(True)
    a.setChecked(b)
    a.triggered.connect(lambda:p.setSpellCheckEnabled(not b))

    if b and conf.get("duck_mode", False):
        firstAct=menu.actions()[0]
        data=web._page.contextMenuData()
        for sug_word in data.spellCheckerSuggestions():
            a=menu.addAction(sug_word)
            menu.insertAction(firstAct, a)
            a.triggered.connect(partial(replaceMisspelledWord, web._page, sug_word))
            if conf.get("bold_text", True):
                f=a.font()
                f.setBold(True)
                a.setFont(f)
        menu.insertSeparator(firstAct)

addHook("EditorWebView.contextMenuEvent", onContextMenuEvent)
addHook("AnkiWebView.contextMenuEvent", onContextMenuEvent)


def setupBDIC(web, *args, **kwargs):
    p=web._page.profile()
    p.setSpellCheckEnabled(conf.get("auto_startup", False))
    p.setSpellCheckLanguages(dictMan.getDictionaries())

AnkiWebView.__init__=wrap(AnkiWebView.__init__, setupBDIC, "after")

