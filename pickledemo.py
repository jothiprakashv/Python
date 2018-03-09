# Save a dictionary into a pickle file.
import pickle
import Circle

favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.p", "wb" ) )
color = pickle.load( open( "save.p", "rb" ) )
print(color)

c1=Circle.Circle(4)
pickle.dump(c1,open("circle.p","wb"))
c=pickle.load(open("circle.p","rb"))

print(c.getRadius())
print(c.area())


