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
They may or may not include type depending on how the site present them.

Words from **freevocabulary** were extracted using the script.js file, but first the HTML was cleaned out. The HTML wont be available in this repo since the site does not belong to me. You are free to look around and check how it was made.
