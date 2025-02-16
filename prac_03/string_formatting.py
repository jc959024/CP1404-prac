name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format() (don't do this unless you need to):
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
