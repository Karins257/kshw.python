from address import Address
from mailing import Mailing


mailing = Mailing(
    to_address=Address("101000", "Москва", "Мясницкая", "20", "12"),
    from_address=Address(
        "190000",
        "Санкт-Петербург",
        "Большая Морская",
        "18",
        "7",
    ),
    cost=450,
    track="RU123456789",
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.postal_code}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
