data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for item in data:
    if "Flower" in item:
        flowers.append(item)
    else:
        shrubs.append(item)

flowers = [item.replace(" - Flower", "") for item in flowers]
shrubs = [item.replace(" - Shrub", "") for item in shrubs]
# Replacing parts of strings in a list

print(flowers)
print(shrubs)

'''
print(flowers.removesuffix(" - Flower"))
print(shrubs.removesuffix(" - Shrub"))
'''