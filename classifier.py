import json
from sklearn import tree
        

def is_mammal(weight, can_fly):
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

    animal_type = classifier.predict([[weight, can_fly]])[0]
    
    return animal_type == 1

# temporary, for testing
if is_mammal(6500, True):
    print("It's a mammal!")
else:
    print("It's a bird!")
