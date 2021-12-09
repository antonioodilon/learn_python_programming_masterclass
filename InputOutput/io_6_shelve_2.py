import shelve

with shelve.open("strategy_games") as strategy_games:
    strategy_games["Name"] = "Tsardoms Total War"
    strategy_games["Favourite faction"] = "Roman Empire"
    strategy_games["Favourite unit"] = "Oikeioi Bodyguard"
    strategy_games["Hours played"] = 30
    strategy_games["Hors played"] = 30

    del(strategy_games["Hors played"])  # Hors played has been deleted

    for key, value in strategy_games.items():
        print(key, value)

    print(strategy_games["Favourite faction"])
    print(strategy_games["Hours played"])
    # print(strategy_games["Hors played"])