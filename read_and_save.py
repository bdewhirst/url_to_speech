import urllib.request

from gtts import gTTS
from bs4 import BeautifulSoup


def reader(
    a_file, a_url,
):
    """
    inputs:
        a_file-- string specifying filename to save the text-to-speech
        a_url-- url to convert to speech
    """
    print("accessing", a_url)
    with urllib.request.urlopen(a_url) as the_url:
        raw_page = the_url.read()

    parsed_html = BeautifulSoup(raw_page, features="html.parser")
    title = parsed_html.head.find("title").text  # for testing purposes, only convert the title.

    tts = gTTS(text=title, lang="en")
    print("calling Google's api and saving result-- this is the slow part.", a_file)
    tts.save(a_file)
