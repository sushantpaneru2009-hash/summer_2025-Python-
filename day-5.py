# slicing
# my_data = "ram","shyam","hari","radha"
# print(my_data )
# print(my_data[0:2


# animal =  Lion ","Tiger","Elephant","Dog","Cat","eagle","Parrot","crocodile","frog","Shark","Butterfly","Bee,Octopus",crab","Penguin"]
# animal = ["Lion", "Tiger", "Elephant", "Dog", "Cat", "eagle", "Parrot", "crocodile", "frog", "Shark", "Butterfly", "Bee", "Octopus", "crab", "Penguin"]
# print( animal[5:10])


# print(animal[4])
# animal[4] = "cow"
# print(animal[4])



# name = "my name is sushant"
# age = " i am years old 18"
# address = "i live in kathmandu, nepal"
# hobby = "my hobby is coding"
# print(name,age,address,hobby)

# name = "sushant"
# age = 18
# address = "kathmandu, nepal"
# hobby = "coding"
# print(f"my name is {name}, i am {age} years old, i live in {address}, my hobby is {hobby}")

my_data = {
    "name": "sushant",
    "age": 18,
    "address": "kathmandu, nepal",
    "hobby":[ "coding",
             "reading",
             "hiking",
             "travelling"]
            

}
print (f"my name is {my_data['name']}, i am {my_data['age']} years old i am from {my_data['address']}, my hobby is {my_data["hobby"][0:3]}")


