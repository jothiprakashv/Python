# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.p", "wb" ) )

color = pickle.load( open( "save.p", "rb" ) )
print(color)



