def filter_objects_by_key_value(collection, source):
    filtered_objects = []
    for obj in collection:
        if all(obj.get(key) == value for key, value in source.items()):
            filtered_objects.append(obj)
    return filtered_objects

collection = [
    {"first": "Romeo", "last": "Montague"},
    {"first": "Mercutio", "last": None},
    {"first": "Tybalt", "last": "Capulet"},
    {"first": "Test", "last": "Capulet"}
]

source_object = {"last": "Capulet"}

filtered_result = filter_objects_by_key_value(collection, source_object)
print(filtered_result) 