## Spelling Police: Tough love spell checker for the editor

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/intro.png?raw=true">

## About:
If you read "The Shallows", it describes the over reliance of spell checkers in modern software. Well, the over reliance of a lot of things in modern tools... But the basic idea is that auto-correct is making us stupid.

This addon follows that idea and is off by default, but when turned on, spelling police nags you and points out all your spelling errors. It does not fix spelling mistakes for you. That's your job. This tough love approach will help you to learn to spell better.

## Dictionaries:
It uses .bdic files which is used by chrome.

You can download some of them here: https://github.com/cvsuser-chromium/third_party_hunspell_dictionaries  

Here is one example file: https://github.com/cvsuser-chromium/third_party_hunspell_dictionaries/blob/master/en-US-3-0.bdic

There are more user-created dictionaries posted in this [issue](https://github.com/lovac42/SpellingPolice/issues/8). 

## Setup:
Go to `Tools > Dictionary Configurations` and click the browse button. Put all your .bdic files into this "dictionaries" folder. You may need to restart the first time after installing new dictionaries.

Once you have it setup, enable or disable the dictionaries of your choice. More than one is allowed, but try to avoid language conflicts (e.g. Chinese and Japanese).

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/setup.png?raw=true">  

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/dictMan.png?raw=true">  

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/folder.png?raw=true">  


### Setup Instruction for Alternate Versions of Anki:
Alternate versions of Anki uses qt5.9 that requires a special folder called `qtwebengine_dictionaries` to be created in the anki.exe folder. It uses the qtwebengine_dictionaries directory relative to the executable. This addon will try to create it, but you will need Read-Write permissions to do so. The same applies to mac and linux, but the folder location may differ depending on your distro.


## Screenshots:

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/cmenu.png?raw=true">  

<img src="https://github.com/lovac42/SpellingPolice/blob/master/screenshots/during_review.png?raw=true">  

