list = [10,20, 30,40,50];
print(list);
print(type(list))

# indexes in python also have negative values like last element have -1
print(list[-1]);

# append is used to add the element in the list
list.append(200);
print(list);

# remove is used to remove the element in the list
list.remove(200)
print(list);


# tuple data_type stored in() tuple also have indexes like list int the form of positive and negative.
# tuple are immutable in nature like we can not append or remove the element in the tuple.
t = (10, 20.9, "python", True);
print(t);
print(type(t))

# set in python taken in the flower braces, sets are unordered in nature, it does not contain index values.
# sets are immutable in nature, like we can add and remove
# set automatically not allow to add duplicate value

s = {10,20,30,40,50};
print(s);
print(type(s))
s.add(200);
print(s);
s.remove(50);
print(s);
s.add(10);
print(s);

# Dictionary in python

d = {"Dennish Ritchie": "C", "Guido Van Rossum": "python", "James Gosling":"Java"};
print(d);

d["Brendan Eich"] = "JavaScript";
print(d);