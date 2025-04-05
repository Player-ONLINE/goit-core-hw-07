from decorators import input_error
from models.record import Record

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return "Contact not found."

@input_error
def show_phones(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return ", ".join([p.value for p in record.phones])
    return "Contact not found."

@input_error
def show_all(book):
    if not book.data:
        return "No contacts found."
    return "\n".join([str(record) for record in book.data.values()])

@input_error
def add_birthday(args, book):
    name, bday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(bday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.birthday:
        return "Birthday not set."
    return record.birthday.value

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays this week."
    return "\n".join([f"{item['name']}: {item['congrats_date']}" for item in upcoming])