def make_album(artist, title):
    return {'artist': artist.title(), 'title': title.title()}

while True:
    print("\nIntroduction your favorite album: ")
    print("(enter 'q' at any time to quit)")
    
    album_name = input("What is the name of album? ")
    if album_name == 'q':
        break
    
    person_album = input("Who made it? ")
    if person_album == 'q':
        break
    
    print(make_album(person_album, album_name))
    # print(album_dict)

print("\nThank you for your respond!")
    