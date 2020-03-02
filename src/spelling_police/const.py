# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import re, os
from pathlib import Path


RE_DICT_EXT_ENABLED = re.compile(r'\.bdic$', re.I)

RE_DICT_EXT_DISABLED = re.compile(r'\.bdic\.disabled$', re.I)


from aqt.qt import qtminor
if qtminor > 9: #Standard build version
    DICT_DIR = os.environ["QTWEBENGINE_DICTIONARIES_PATH"]
else: #Alternate build version
    from aqt import moduleDir
    # Wins only, prob won't work on mac or linux
    DICT_DIR = os.path.join(moduleDir, "qtwebengine_dictionaries")

try:
    Path(DICT_DIR).mkdir(parents=True, exist_ok=True)
except:
    print("Can't create dictionary folder, check permissions.")
