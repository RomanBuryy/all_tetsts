def filter_dict(members: list):
    members = list(filter(lambda x, y="o": y in x["name"], members))
    return members
