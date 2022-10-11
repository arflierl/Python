

musicians = {"name": ["Jerry Garcia", "Miles Daves", "Joe Pass",
                      "Kenny G", "Yo-Yo Ma", "Billy Joel", "Robert Johnson"],
             "instrument": ["guitar", "trumpet", "guitar", "saxophone", "cello",
                            "piano", "guitar"], "genre": ["various", "Jazz", "Jazz",
                                                          "Jazz", "classical", "various",
                                                          "blues"]}
names = musicians.get("name")
instruments = musicians.get("instrument")
genres = musicians.get("genre")

def keyword_counter(x: dict, MyValue) -> int:
    keyword_count = 0
    for key in musicians.keys():
        if key == MyValue:
            keyword_count += 1
    for musician in names:
        if musician == MyValue:
            keyword_count += 1
    for instrument in instruments:
        if instrument == MyValue:
            keyword_count += 1
    for genre in genres:
        if genre == MyValue:
            keyword_count += 1


    print(keyword_count)


keyword_counter(musicians, "Jazz")
keyword_counter(musicians, "saxophone")
keyword_counter(musicians, "genre")

