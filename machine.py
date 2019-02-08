from sklearn import tree

cannot_fly = 0
can_fly = 1

# weight in grams + wings or not

# birds
magpie = [210, can_fly]
crow = [550, can_fly]
ostrich = [150000, cannot_fly] # tricky
albatross = [7000, can_fly]

# mammals
rat = [250, cannot_fly]
bat = [12, can_fly] # tricky
elephant = [6000000, cannot_fly]
moose = [500000, cannot_fly]

features = [magpie, crow, ostrich, albatross, rat, bat, elephant, moose]

bird = 0
mammal = 1

labels = [bird, bird, bird, bird, mammal, mammal, mammal, mammal]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

while(True):
    input_weight = input("Enter the animal's weight: ")
    input_can_fly = input("Enter 1 if the animal can fly or 0 if it cannot: ")

    animal_type = classifier.predict([[input_weight, input_can_fly]])[0]

    sentence_start = "The animal is probably a "

    guess = 'bird!' if animal_type == bird else 'mammal!'

    print sentence_start + guess
