from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        result = []

        for record in self.data.values():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                bday_this_year = bday.replace(year=today.year)

                if bday_this_year < today:
                    bday_this_year = bday_this_year.replace(year=today.year + 1)

                if today <= bday_this_year <= next_week:
                    congrats_date = bday_this_year
                    if congrats_date.weekday() >= 5:
                        congrats_date += timedelta(days=(7 - congrats_date.weekday()))
                    result.append({
                        "name": record.name.value,
                        "congrats_date": congrats_date.strftime("%d.%m.%Y")
                    })

        return result