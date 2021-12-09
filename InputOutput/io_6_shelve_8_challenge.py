import shelve

books = shelve.open("books")
books["recipes"] = {
    "scrambled_eggs": ["eggs", "butter", "salt", "cheese"],
    "ground_beef": ["ground beef", "salt", "pepper", "lard"],
    "chicken_breast": ["chicken breast", "butter", "sea salt"],
    "beef_liver": ["beef liver", "onions", "sea salt"],
    "sausages": ["sausages"],
}
books["maintenance"] = {
    "stuck": ["oil"],
    "loose": ["gaffer tape"],
}
print(books["recipes"])
print(books["maintenance"])
books.close()