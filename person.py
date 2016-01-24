import json


class Person(object):
    def __init__(self, first_name, second_name, birthday_date, nameday_date, mail, tel_number, facebook, person_id):
        self.first_name = first_name
        self.second_name = second_name
        self.birthday_date = birthday_date
        self.nameday_date = nameday_date
        self.mail = mail
        self.tel_number = tel_number
        self.facebook = facebook

        self.person_id = person_id

