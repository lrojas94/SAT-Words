from StringIO import StringIO
import pycurl
import json
from lxml import html

def getHTML(url):
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()
    return content

def main():
    baseURL = 'http://www.majortests.com/sat/wordlist-'
    filename = "majortests_words.json"

    print "Starting..."

    result = []
    for i in range(1,11):
        url = baseURL + str(i).zfill(2)
        pageContent = getHTML(url)
        tree = html.fromstring(pageContent)
        words = tree.xpath('//table[@class="wordlist"]/tr/th/text()')
        definitions = tree.xpath('//table[@class="wordlist"]/tr/td/text()')
        for i in range(0,len(words)):
            item = {}
            item['word'] = words[i]
            item['definition'] = definitions[i]
            item['type'] = ''
            result.append(item)
        print "Data obtained from: " + url
    print "Writing to file..."
    output = {"results" : result}
    f = open(filename,'w')
    f.write(json.dumps(output,sort_keys=True,indent=4, separators=(',', ': ')))
    f.close()
    print "Done"


if __name__ == "__main__":
    main()
