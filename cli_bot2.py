import re
from typing import List, Dict, Tuple, Callable

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid value."
        except IndexError:
            print("Enter the argument for the command")
            return ""
    return inner

# Парсинг введення користувача
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    args = parts[1].split() if len(parts) > 1 else []
    return cmd, args

# Валідація номера телефону
def validate_phone(phone: str) -> bool:
    return bool(re.match(r'^\+?\d{10,15}$', phone))


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if not validate_phone(phone):
        raise ValueError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if not validate_phone(phone):
        raise ValueError
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    raise KeyError


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts: Dict[str, str] = {}
    commands: Dict[str, Callable[[List[str], Dict[str, str]], str]] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": lambda _, contacts: show_all(contacts)
    }

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            if not user_input:
                print("Enter the argument for the command")
                continue
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command in commands:
                result = commands[command](args, contacts)
                if result:
                    print(result)
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
