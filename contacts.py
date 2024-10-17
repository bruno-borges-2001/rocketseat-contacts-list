from typing import TypedDict, List


class Contact(TypedDict):
    name: str
    phone: str
    email: str
    is_favorite: bool


def print_commands_list():
    print(
        "Commands:\n"
        "1 - Add a new contact\n"
        "2 - Show all contacts\n"
        "3 - Update a contact\n"
        "4 - Remove a contact\n"
        "0 - Exit\n"
    )


def create_contact() -> Contact:
    name = input('Enter the name: ')
    phone = input('Enter the phone: ')
    email = input('Enter the email: ')
    is_favorite = input('Is this a favorite contact? (y/N)').lower() == 'y'

    return {
        'name': name,
        'phone': phone,
        'email': email,
        'is_favorite': is_favorite
    }


def print_contact(contact: Contact, index: int = None):
    favorite = '❤' if contact['is_favorite'] else ''
    count = '' if index is None else index + 1
    print(f'{count}. {contact['name']} {favorite}')
    print(f'   - Phone: {contact['phone']}')
    print(f'   - Email: {contact['email']}')


def print_contact_list(contacts: List[Contact], only_favorites: bool = False):
    print('Contacts:')
    for index, contact in enumerate(contacts):
        if (only_favorites and not contact['is_favorite']):
            continue

        print_contact(contact, index)


def update_contact(original: Contact) -> Contact:
    copied = original.copy()
    is_satisfied = False

    while not is_satisfied:
        print("\n" * 100)

        print_contact(copied)

        print(
            "What field do you want to update?\n"
            "1. Name\n"
            "2. Phone\n"
            "3. Email\n"
            "4. Toggle Favorite"
        )

        field = input(">")

        match field:
            case "1":
                copied['name'] = input('Enter the new name: ')
            case "2":
                copied['phone'] = input('Enter the new phone: ')
            case "3":
                copied['email'] = input('Enter the new email: ')
            case "4":
                copied['is_favorite'] = not copied['is_favorite']
            case _:
                print('Invalid field, please try again')
                input('Press ENTER to continue...')
                continue

        print_contact(copied)
        is_satisfied = input(
            'Are you done updating? (Y/n)').lower() != 'n'

    return copied


def input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid number, please try again')


def main():
    contacts: List[Contact] = []

    while True:
        print_commands_list()
        command = input(">")
        print("\n" * 100)
        match command:
            case "1":
                is_satisfied = False
                contact = None

                while not is_satisfied:
                    contact = create_contact()
                    print_contact(contact)
                    is_satisfied = input(
                        'Is this information correct? (Y/n)').lower() != 'n'

                if contact:
                    contacts.append(contact)
                    print('Contact added successfully!')
            case "2":
                print_contact_list(contacts)
            case "3":
                print_contact_list(contacts)
                contactIndex = input_number('Enter the contact number: ') - 1

                if (contactIndex < 0 or contactIndex >= len(contacts)):
                    print('Invalid contact number')
                else:
                    contacts[contactIndex] = update_contact(
                        contacts[contactIndex])
                    print('Contact updated successfully!')
            case "4":
                print_contact_list(contacts)
                contactIndex = input_number('Enter the contact number: ') - 1

                if (contactIndex < 0 or contactIndex >= len(contacts)):
                    print('Invalid contact number')
                else:
                    contacts.pop(contactIndex)
                    print('Contact removed successfully!')
            case "0":
                print('Exiting...')
                break
            case _:
                print('Invalid command, please try again')
        input('Press ENTER to continue...')
        print('\n' * 100)


if __name__ == '__main__':
    main()
