from dataclasses import dataclass
import re


@dataclass(frozen=True, slots=True, repr=True, init=True)
class Hotel:
    name: str
    taxes: dict
    rank: int


hotels = [
    Hotel(
        name='Lakewood',
        taxes={
            'Regular': {
                'mon': 110.00,
                'tues': 110.00,
                'wed': 110.00,
                'thur': 110.00,
                'fri': 110.00,
                'sat': 90.00,
                'sun': 90.00,
            },
            'Rewards': {
                'mon': 80.00,
                'tues': 80.00,
                'wed': 80.00,
                'thur': 80.00,
                'fri': 80.00,
                'sat': 80.00,
                'sun': 80.00,
            },
        },
        rank=3
    ),
    Hotel(
        name='Bridgewood',
        taxes={
            'Regular': {
                'mon': 160.00,
                'tues': 160.00,
                'wed': 160.00,
                'thur': 160.00,
                'fri': 160.00,
                'sat': 60.00,
                'sun': 60.00,
            },
            'Rewards': {
                'mon': 110.00,
                'tues': 110.00,
                'wed': 110.00,
                'thur': 110.00,
                'fri': 110.00,
                'sat': 50.00,
                'sun': 50.00,
            },
        },
        rank=4
    ),
    Hotel(
        name='Ridgewood',
        taxes={
            'Regular': {
                'mon': 220.00,
                'tues': 220.00,
                'wed': 220.00,
                'thur': 220.00,
                'fri': 220.00,
                'sat': 150.00,
                'sun': 150.00,
            },
            'Rewards': {
                'mon': 100.00,
                'tues': 100.00,
                'wed': 100.00,
                'thur': 100.00,
                'fri': 100.00,
                'sat': 40.00,
                'sun': 40.00,
            },
        },
        rank=5
    ),
]


# DO NOT change the function's name
def get_cheapest_hotel(reservation: str) -> str:
    try:
        client_type = re.search(r'^(\w+):', reservation).group(1)
    except AttributeError:
        client_type = 'Regular'  # Default client type

    reservation_weekdays = re.findall(r'\(([a-z]{3,4})\)', reservation)

    for i, hotel in enumerate(hotels):
        price = 0.00
        for day in reservation_weekdays:
            price += hotel.taxes[client_type][day]
        if i == 0:
            cheapest_hotel = hotel
            min_price = price
        elif price < min_price:
            cheapest_hotel = hotel
        elif price == min_price:
            if hotel.rank > cheapest_hotel.rank:
                cheapest_hotel = hotel

    return cheapest_hotel.name


def main():
    reservation = 'Rewards: 11May2009(tues), 27Mar2009(wed), 28Mar2009(thurs)'
    print(get_cheapest_hotel(reservation))


if __name__ == '__main__':
    main()
