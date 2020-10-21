import json

if __name__ == '__main__':
    data = [
        {'name': 'xiaoming1', 'age': '18'},
        {'name': 'xiaoming2', 'age': '18'},
        {'name': 'xiaoming3', 'age': '18'},
        {'name': 'xiaoming4', 'age': 18},
        None,
        True
    ]
    data_in_json = json.dumps(data)
    print(type(data_in_json), data_in_json)

    data_in_json = '''{"name": "xiaoming1", "age": "18"}'''

    data = json.loads(data_in_json)
    print(type(data), data)
