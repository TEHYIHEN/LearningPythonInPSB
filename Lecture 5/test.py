full_dot = '●'
empty_dot = '○'


def create_character():
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name too long"
    elif " " in name:
        return "The character name should not contain spaces"
    else:
        return "All pass"


name = input("Name:")
print(create_character())