"""Module that contains function that generate the category accord to record id"""


def generate_category(record_id, categories):
    """Generate the category of a record according to the given record_id"""
    # Change the following if and else if statements according to your
    # needs.
    if int(record_id) in range(1000, 2000):
        categories.append("1000-1999")
    elif int(record_id) in range(2000, 3000):
        categories.append("2000-2999")
    elif int(record_id) in range(3000, 4000):
        categories.append("3000-3999")
    elif int(record_id) in range(4000, 5000):
        categories.append("4000-4999")
    elif int(record_id) in range(5000, 6000):
        categories.append("5000-5999")
