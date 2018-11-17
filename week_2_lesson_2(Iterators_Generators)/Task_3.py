def percentage_of_progress(members:list):
    members = list(map(lambda x: {'age': x['age'], 'name': x['name'], 'load': x["age"]*0.5}, members))
    return members
