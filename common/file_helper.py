import csv


def read_test_data_from_csv(data_file):
    test_data = []
    filename = 'data/users.csv'
    try:
        with open(filename, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            next(data)  # skip the header
            for row in data:
                test_data.append(row)
        return test_data

    except FileNotFoundError:
        print('File not found', filename)
    except Exception as e:
        print(e)

