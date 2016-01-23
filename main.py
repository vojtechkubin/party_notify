import fake_db
from datetime import date
from person import Person, Person_encoder


def main():
    data = (fake_db.load('data.json'))
    data2 = {}
    persona = Person('first_name', 'second_name', str(date.today()), 'kokos', 'mail@hacking.fg', '777999555', 'facebook')
    #data2['persona'] = str(Person_encoder(indent=4).encode(persona))
    data2['persona'] = persona
    data2['personb'] = persona
    fake_db.save(data2, 'data2.json')

if __name__ == '__main__':
    main()
