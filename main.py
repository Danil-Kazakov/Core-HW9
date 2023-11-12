user_info = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter user name"
        except (ValueError, IndexError):
            return "Give me name and phone please"
    return wrapper

@input_error
def add_contact(command):
    _, name, phone = command.split()
    name = name.title()
    user_info[name] = phone
    return f"Added contact: {name} | {phone}"

@input_error
def change_phone(command):
    _, name, phone = command.split()
    name = name.title()
    if name in user_info:
        user_info[name] = phone
        return f"Changed phone for contact: {name}: {phone}"
    else:
        return f"Contact not found for {name}"

@input_error
def get_phone(command):
    _, name = command.split()
    name = name.title()
    if name in user_info:
        return f"Phone number for {name}: {user_info[name]}"
    else:
        return f"Contact not found for {name}"

def show_all():
    if user_info:
        result = "Contacts:\n"
        for name, phone in user_info.items():
            result += f"{name} | {phone}\n"
        return result.strip()
    else:
        return "No contacts found"

def main():
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print (add_contact(command))
        elif command.startswith("change"):
            print (change_phone(command))
        elif command.startswith("phone"):
            print (get_phone(command))
        elif command.startswith("show all"):
            print (show_all())
        elif command in ("good bye", "close", "exit"):
            print ("Good bye!")
            break
        else:
            print ("Invalid command")

if __name__ == "__main__":
    main()