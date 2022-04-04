import json


class MyClass:
    a = 10

    # Constructor
    def __init__(self, a=20):
        self.a = a

    def func(self):
        print(self.a)


def class_func():
    obj1 = MyClass()
    obj1.func()
    obj2 = MyClass(40)
    obj2.func()


def control_func():
    num = -1

    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

        # X is not defined
        try:
            print(x + 1)
        except:
            print("exception: variable x is used bot not defined")


def json_func():
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(f'age = {y["age"]}')

    # A Python dict:
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)


def range_func():
    numbers = range(1, 6)
    print(list(numbers))  # Output: [1, 2, 3, 4, 5]
    print(tuple(numbers))  # Output: (1, 2, 3, 4, 5)
    print(set(numbers))  # Output: {1, 2, 3, 4, 5}
    numbers2 = range(1, 6, 2)  # With a step parameter
    print(list(numbers2))  # Output: [1, 3, 5]


def dictionary_func():
    # empty dictionary
    my_dict = {}
    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}
    person = {'name': 'Jack', 'age': 26, 'salary': 4534.2}
    print(person['age'])  # Output: 26


def set_func():
    # A set is an unordered collection of items where every element is unique.
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)
    my_set.add(4)
    print(my_set)


def string_func():
    str = 'programiz'
    print('str = ', str)

    print('str[0] = ', str[0])  # Output: p

    print('str[-1] = ', str[-1])  # Output: z

    # slicing 2nd to 5th character
    print('str[1:5] = ', str[1:5])  # Output: rogr

    # slicing 6th to 2nd last character
    print('str[5:-2] = ', str[5:-2])  # Output: am


def print_hi(name):
    integer = 5
    str = '456'
    print(f'Hi, {name} and integer = {integer} and str after explicit conversion = {int(str)}')
    # Output: <class 'int'>
    print(type(5))

    square = lambda x: x ** 2
    print(f'Square of 5 is {square(5)}')

    # Output: <class 'float'>
    print(type(5.0))

    new_list = [1, "Harper", 3.4]
    print(new_list)
    new_list.append("Horatio")
    print(f'Index of Harper is: {new_list.index("Harper")}')
    print(f'Index of Horatio is: {new_list.index("Horatio")}')
    new_list.append(["Leon", "Saori"])
    print(new_list)

    # create a list
    prime_numbers = [2, 3, 5]
    numbers = [1, 4]
    # The append method adds an item to the end of the list.
    numbers.extend(prime_numbers)
    print('List after extend():', numbers)

    # Tuple is similar to a list except you cannot change elements of a tuple once it is defined.
    # Whereas in a list, items can be modified. Basically, lists are mutable whereas tuples are immutable.
    language = ("French", "German", "English", "Polish")
    print(language)

    prime_numbers = [2, 3, 5]
    numbers = prime_numbers.copy()
    print('Copied List:', numbers)
    # inputString = input('Enter a sentence:')
    # print('The inputted string is:', inputString)


if __name__ == '__main__':
    print_hi('Leon')
    string_func()
    set_func()
    dictionary_func()
    range_func()
    control_func()
    json_func()
    class_func()
