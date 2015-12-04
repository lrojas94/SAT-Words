# SAT Words Repo
The idea of this repo is to have a JSON file with all words displayed in http://www.freevocabulary.com/ as well as those from http://www.majortests.com/sat/wordlist.php

## Format
All Words are displayed in the following format:
```js
{
    "word": "abase",
    "type": "v.",
    "definition": "To lower in position, estimation, or the like; degrade."
}
```
They may or may not include type depending on how the site has them.
All words were extracted using the **html.html** file and the **script.js** script. Please note that the script requires JQuery in order to work.
