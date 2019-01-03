import urllib.request

import re
from gtts import gTTS


def stripper(data):
    """ remove html/xml as well as header
        note: printing unicode doesn't work as expected, but it'll translate to audio fine.
        note: currently doesn't remove header info/ select body.
    """
    return re.sub('<[^<]+?>', '', re.sub('<head>+?</nav>', '', data))

    
def reader(
    a_file,
    a_url,
):
    """
    inputs:
        a_file-- string specifying filename to save the text-to-speech
        a_url-- url to convert to speech
    """
    print("accessing", a_url)
    with urllib.request.urlopen(a_url) as the_url:
        blabla = the_url.read()
        
    blabla = blabla.decode("utf-8")

    blabla = stripper(blabla)
    tts = gTTS(text=blabla, lang='en')
    print("calling Google's api and saving result-- this is the slow part.", a_file)
    tts.save(a_file)


if __name__ == "__main__":
    pass  # don't call this script directly, use main.py instead.
