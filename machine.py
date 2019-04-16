import json
from sklearn import tree

with open("animals.json", "r") as read_file:
    animals = json.load(read_file)

features = []
labels = []

for animal in animals:
    animal["can_fly"] = 1 if animal["can_fly"] else 0
    animal["is_mammal"] = 1 if animal["is_mammal"] else 0

    features.append([animal["weight"], animal["can_fly"]])
    labels.append(animal["is_mammal"])

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

while(True):
    input_weight = input("Enter the animal's weight in grams: ")
    input_can_fly = input("Enter 1 if the animal can fly or 0 if it cannot: ")

    animal_type = classifier.predict([[input_weight, input_can_fly]])[0]

    sentence_start = "The animal is probably a "
    guess = 'mammal!' if animal_type == 1 else 'bird!'
    print(sentence_start + guess)
