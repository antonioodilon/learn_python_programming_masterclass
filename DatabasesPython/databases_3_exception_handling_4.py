import databases_3_exception_handling_3 as database

flock = database.Flock()
duck1 = database.Duck()
duck2 = database.Duck()
duck3 = database.Duck()
duck4 = database.Duck()
duck5 = database.Duck()
duck6 = database.Duck()
duck7 = database.Duck()
penguin = database.Penguin()

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(penguin)  # Expect type Duck, got Penguin instead
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()