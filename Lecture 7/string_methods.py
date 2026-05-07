brand = "Shaw Theatres"
print(brand.lower())
print(brand.upper())

brand = brand.lower()  # new string produced
print(brand)

print("len of brand", len(brand))

print("start with sh?", brand.startswith("sh"))
print("start with SH?", brand.startswith("SH"))
print("start with es", brand.endswith("es"))
print("start with ES", brand.endswith("ES"))


