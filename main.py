import read_and_save
from constants import *  # if it is in all-caps, it is a constant from this file.


pages_to_read = {
    "charlie_eg1.mp3": "2011/05/virtually-there.html",
    "charlie_eg2.mp3": "2011/05/why-are-your-houses-so-heavy.html",
}


def main():
    """
    Call google's TTS api over a dictionary of filename -- url pairs.
    """
    for a_file, a_url in pages_to_read.items():
        full_file = FILE_STEM + a_file
        full_url = URL_STEM + a_url
        read_and_save.reader(full_file, full_url)
    print("Done saving pages to urls")


if __name__ == "__main__":
    main()
