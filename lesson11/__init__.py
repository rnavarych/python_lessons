try:
    with open('myfile.txt') as fn:
        file_data = fn.read()
    print(file_data)
# except FileNotFoundError:
#     print('The data_file is missing')
# except PermissionError:
#     print('This is not allowed')
except Exception as err:
    print('exception ', str(err))
