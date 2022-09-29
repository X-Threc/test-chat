from ds.test_func import max_for_dicts, filter_dicts
messages=[
    {'name': 'Jack', 'time': 10, 'text': '123'},
    {'name': 'Jack', 'time': 20, 'text': '1234'},
    {'name': 'Jack', 'time': 30, 'text': '1235'},
    {'name': 'Jack', 'time': 40, 'text': '1236'},
    {'name': 'Jack', 'time': 50, 'text': '1237'},
]
print(max_for_dicts(messages,'time'))
print(filter_dicts(messages,'time',30))


