from sklearn import tree
features = [[300,2],[450,2],[200,8],[150,9]]
labels = ['sports-car','sports-car','minivan','minivan']

train = tree.DecisionTreeClassifier()
train = train.fit(features,labels)
print (train.predict([[500,2]]))
