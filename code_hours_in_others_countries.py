def tell_me_the_hour(country, hour):
    if country == 1:
        return print(hour - 1)
    elif country == 2:
        return print(hour + 1)

def run():
    country = int(input('México to Colmbia = 1 or Colombia to México = 2: '))
    hour_in_country_1 = int(input('Put the hour in your country: '))
    print(tell_me_the_hour(country, hour_in_country_1))

if __name__ == '__main__':
    run()