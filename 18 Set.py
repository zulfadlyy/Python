# Set = collection which are UNORDERED and UNINDEXED. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup", "knife"}

# You can make adjustments to sets:
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dishes.update(utensils)
# dinner table = utensils.union(dishes) \\ This joins 2 sets together.


for x in utensils:
    print(x)

# print(utensils.difference(dishes)) \\ This checks the difference between 2 sets.
# print(f"The similarity is: {utensils.intersection(dishes)}") \\ This checks the similarities between 2 sets.

