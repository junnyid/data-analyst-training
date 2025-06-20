def make_album(artist, title, numbers=None):
    dict_album = {"artist": artist.title(), "title": title.title()}
    if numbers:
        dict_album["numbers"] = numbers
    return dict_album


album = make_album("bensone", "beautiful thing", numbers=10)
print(album)
