def send_messages(films):
    for film in films:
        print(film.title())


def sent_messages(films):
    good_films = []
    while films:
        film = films.pop()
        good_film = film + " (good)"
        good_films.append(good_film)

    for good_film in good_films:
        films.append(good_film)


films = ["anne with an e", "harry potter", "sheldon"]
send_messages(films)

print("\n")
sent_messages(films)
send_messages(films)
