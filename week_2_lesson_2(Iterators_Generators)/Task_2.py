def upper_name(members:list):
    members = list(map(lambda x: {'age': x['age'], 'name': x['name'].upper()}, members))
    return members






