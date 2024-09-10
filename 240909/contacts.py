'''
"name": {"phone":"53574873543", "email": "sadfs": "sfres@fsde.com", **kwargs}
add_contact(name, phone, email=None, **kwargs)
view_contact(name)
update_contact(name, phone, email, **kwargs)
delete_contact(name)
list_contacts()
load_json
save_json
'''
import json


def load_json():
    global contact_book
    with open('contact_book.json', 'r', encoding='utf8') as contact_data:
        contact_book = json.load(contact_data)

def save_json():
    with open('contact_book.json', 'w', encoding='utf8') as contact_data:
        json.dump(contact_book, contact_data, indent=4)


def add_contact(name, phone, email=None):
    if name not in contact_book:
        contact_book[name] = {'phone': phone, 'email': email}
        save_json()
        print(f'Contact {name} was added.')
    else:
        print(f'contact {name} alredy exist.')

def view_contact(name):
    if name in contact_book:
        print(name)
        print(f'Phone: {contact_book[name]['phone']}')
        if contact_book[name].get('email'):
              print(f'Contact {name} does not exist.')
    else:
        print(f'Contact {name} does not exist.')


def update_contact(name, phone=None, email=None):
    data = {}
    if name in contact_book:
        if phone:
            data['phone'] = phone
        if email:
            data['email'] = email
        if data:
            contact_book[name].update(data)
            save_json
            print(f'Contact {name} was updated.')
        else:
            print(f'Nothing to update.')
    else:
        print(f'Contact {name} does not exist')

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        save_json()
        print(f'Contact {name} was deleted.')
    else:
        print(f'Contact {name} does not exist')
def list_contacts():
    for num, name in enumerate(sorted(contact_book.keys()),1):
        print(f'{num}.{name}')


contact_book = {}

load_json()
#add_contact('Jack', '555-555-5555')
#add_contact('Sarah', '555-555-5555', 'sarah@gfhg.com')
#view_contact('Jack')
#view_contact('Bob')
#update_contact('Jack', email='jack@hdgfg.com')
#update_contact('Sarah', '555-345-87654' ,' sarah444@jdhh.com')
#update_contact('Bob', '555-88765-54')
