from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24", "+79261234567"),
    Smartphone("Google", "Pixel 8", "+79361234567"),
    Smartphone("Xiaomi", "14", "+79461234567"),
    Smartphone("OnePlus", "12", "+79561234567"),
]

for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. "
        f"{smartphone.phone_number}"
    )
