import json
from sklearn import tree


class Classifier:
    def __init__(self):
        with open("animals.json", "r") as read_file:
            animals = json.load(read_file)

        features = []
        labels = []

        for animal in animals:
            animal["can_fly"] = 1 if animal["can_fly"] else 0
            animal["is_mammal"] = 1 if animal["is_mammal"] else 0

        features.append([animal["weight"], animal["can_fly"]])
        labels.append(animal["is_mammal"])

        self.classifier = tree.DecisionTreeClassifier()
        self.classifier = self.classifier.fit(features, labels)

    def is_mammal(self, weight, can_fly):
        can_fly = 1 if can_fly else 0
        print(can_fly)
        animal_type = self.classifier.predict(
            [[weight, can_fly]])[0]
        print(animal_type)
        return animal_type == 1


classifier = Classifier()
if classifier.is_mammal(7000, False):
    print("It's a mammal!")
else:
    print("It's a bird!")
