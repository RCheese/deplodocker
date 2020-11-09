def stainer(data: dict, section: list):
    # TODO: use cases of another requirements management. Now poetry only
    if section:
        data = {k: v for k, v in data.items() if k in section}
    return data
