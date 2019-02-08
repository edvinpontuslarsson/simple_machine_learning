from sklearn import tree

bumpy = 0
smooth = 1

features = [[140, smooth], [130, smooth], [150, bumpy], [170, bumpy]]

apple = 0
orange = 1

labels = [apple, apple, orange, orange]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

# Should be an orange, 1
print classifier.predict([[150, 0]])
