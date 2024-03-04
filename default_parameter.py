# Belajar default argument value

def say_hello(firstName="Arjun", lastName=""):
    print(f"Hello, {firstName} - {lastName}!")

say_hello("Arjun")
say_hello(lastName="Gunawan", firstName="Aresha")