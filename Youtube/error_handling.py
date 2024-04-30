try:
    with open('test.txt', 'r') as my_file:
        print(my_file.read())
except Exception as e:
    print(e)
finally:
    print('Codes Run well')
