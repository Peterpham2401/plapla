class MappingDict(dict):
    def gd(self, key):
        result = self.get(key)
        if result is None:
            return MappingDict({})
        elif isinstance(result, dict):
            return MappingDict(result)
        return result

    def g(self, key):
        return self.get(key)

def handle_date_timezone(date):
    if date is None:
        return None
    if date.endswith("+07:00"):
        return date
    if date.endswith("Z"):
        return date[:-1] + "+07:00"
    return date + "+07:00"
