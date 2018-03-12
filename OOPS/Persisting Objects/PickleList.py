import pickle
some_data = ["a list", "containing", 5,
             "values including another list",
             ["inner", "list"]]
#Persisting the data           
with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)


# Extracting the persisted data
with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)
