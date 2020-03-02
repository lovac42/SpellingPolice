# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import os
from aqt import mw
from aqt.qt import *
from aqt.utils import openFolder, showInfo

from .const import *


class DictionaryManager:
    def __init__(self):
        self.setupMenu()

        self._dicts = [
            i[:-5] for i in os.listdir(DICT_DIR) if RE_DICT_EXT_ENABLED.search(i)
        ]

    def setupMenu(self):
        a = QAction("Dictionary Configuration", mw)
        a.triggered.connect(self.showConfig)
        mw.form.menuTools.addAction(a)

    def showConfig(self):
        p=mw.web._page.profile()
        b=p.isSpellCheckEnabled()
        p.setSpellCheckEnabled(False)
        p.setSpellCheckLanguages({})
        d = DictionaryDialog()
        self._dicts = d.getDictionaries()
        p.setSpellCheckEnabled(b)
        p.setSpellCheckLanguages(self._dicts)

    def getDictionaries(self):
        return self._dicts




class DictionaryDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self._setupDialog()
        self._update()
        self.exec_()

    def getDictionaries(self):
        return self._dict

    def _setupDialog(self):
        self.setWindowTitle("Dictionaries")
        self.setWindowModality(Qt.WindowModal)
        self.resize(250, 250)

        layout = QVBoxLayout()
        self.list = QListWidget()
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.list.itemDoubleClicked.connect(self._toggle)

        bws_btn = QPushButton('Browse')
        bws_btn.clicked.connect(self._browse)
        en_btn = QPushButton('Enable')
        en_btn.clicked.connect(self._enable)
        dis_btn = QPushButton('Disable')
        dis_btn.clicked.connect(self._disable)

        control_box = QHBoxLayout()
        control_box.addWidget(bws_btn)
        control_box.addWidget(en_btn)
        control_box.addWidget(dis_btn)

        layout.addWidget(self.list)
        layout.addLayout(control_box)
        self.setLayout(layout)

    def _update(self):
        self._dict = []
        self.list.clear()

        try:
            DICT_FILES=os.listdir(DICT_DIR)
        except FileNotFoundError:
            showInfo("Missing or no read/write permission to dictionary folder.")
            return

        for d in DICT_FILES:
            if RE_DICT_EXT_ENABLED.search(d):
                item = QListWidgetItem(d)
                item.setData(Qt.UserRole, d)
                self.list.addItem(item)
                self._dict.append(d[:-5])

        for d in DICT_FILES:
            if RE_DICT_EXT_DISABLED.search(d):
                item = QListWidgetItem(d)
                item.setData(Qt.UserRole, d)
                self.list.addItem(item)

    def _browse(self):
        if os.path.exists(DICT_DIR):
            openFolder(DICT_DIR)
        elif ALT_BUILD_VERSION:
            from aqt import moduleDir
            openFolder(moduleDir)

        if ALT_BUILD_VERSION:
            showInfo(ALT_BUILD_INSTRUCTIONS, title="Instructions", textFormat="rich")

    def _enable(self):
        sel = [i for i in range(self.list.count())
                if self.list.item(i).isSelected()]
        if sel:
            for i in sel:
                fn=self.list.item(i).text()
                if RE_DICT_EXT_DISABLED.search(fn):
                    f=os.path.join(DICT_DIR, fn)
                    os.rename(f, f[:-9])
        self._update()

    def _disable(self):
        sel = [i for i in range(self.list.count())
                if self.list.item(i).isSelected()]
        if sel:
            for i in sel:
                fn=self.list.item(i).text()
                if RE_DICT_EXT_ENABLED.search(fn):
                    f=os.path.join(DICT_DIR, fn)
                    os.rename(f, f+'.disabled')
        self._update()

    def _toggle(self):
        fn=self.list.currentItem().text()
        if RE_DICT_EXT_ENABLED.search(fn):
            self._disable()
        else:
            self._enable()
