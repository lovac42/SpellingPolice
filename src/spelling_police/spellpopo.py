# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1



# Enable/Disable as necessary, but avoid language conflicts
DICT_FILES = {
    "en-US-3-0",
    # "en-GB-3-0",

    # Add your beloved dicts here:
    # "xx-XX-3-0",
    # "xx-XX-3-0",

    # "fr-FR-3-0"
}

CHECK_ON_STARUP = False



from aqt.qt import *
from aqt.webview import AnkiWebView
from anki.hooks import wrap, addHook
from anki.lang import _


def onContextMenuEvent(editor, menu):
    p=editor._page.profile()
    b=p.isSpellCheckEnabled()
    menu.addSeparator()
    a=menu.addAction(_("Spelling Police"))
    a.setCheckable(True)
    a.setChecked(b)
    a.triggered.connect(lambda:p.setSpellCheckEnabled(not b))

addHook("EditorWebView.contextMenuEvent", onContextMenuEvent)


def setupBDIC(web, parent=None):
    p=web._page.profile()
    p.setSpellCheckEnabled(CHECK_ON_STARUP)
    p.setSpellCheckLanguages(DICT_FILES)

AnkiWebView.__init__=wrap(AnkiWebView.__init__, setupBDIC, "after")
