import Bag

bag = Bag.Bag()

with open("License.txt", "r") as file:
    for line in file:
        for word in line.split():
            bag.add(word)

print(str(bag))