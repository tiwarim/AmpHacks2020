import sklearn 
import numpy as np
import pandas as pd
from sklearn import model_selection, neighbors, metrics
import matplotlib.pyplot as plt


data = pd.read_csv("Totally Not Fake Data - Sheet1.csv")
labels = data["Label"]
#labels = labels.drop(index=0)
#data = data.split(",")
del data['Label']
#data = data.drop(index=0)

X_train, X_test, y_train, y_test = model_selection.train_test_split(data,labels,test_size=0.2,train_size=0.8)
X_test, X_validation, y_test, y_validation = model_selection.train_test_split(X_test, y_test, test_size=0.5)

def select_knn_model(X_train, X_validation, y_train, y_validation, metric="euclidean"):
    bestAccuracy=0;
    chosenK = 0;
    for i in range(1,21):
        knn = neighbors.KNeighborsClassifier(n_neighbors=i, metric=metric)
        knn = knn.fit(X_train, y_train)
        y_train_pred = knn.predict(X_train)
        y_valid_pred = knn.predict(X_validation)

        training_accuracy = metrics.accuracy_score(y_train, y_train_pred)
        validation_accuracy = metrics.accuracy_score(y_validation, y_valid_pred)

        if (validation_accuracy > bestAccuracy):
            bestAccuracy= validation_accuracy
            chosenK = i

        plt.scatter(i, validation_accuracy, color="green")
        plt.scatter(i, training_accuracy, color="blue")


    plt.show()
    knn = neighbors.KNeighborsClassifier(n_neighbors=chosenK, metric=metric)
    knn = knn.fit(X_train, y_train)
    print("best k", chosenK)
    return knn

#X_train, X_test, X_validation, y_train, y_test, y_validation = load_data()
knn = select_knn_model(X_train, X_validation, y_train, y_validation, metric="cosine")
y_test_pred = knn.predict(X_test)
test_accuracy = metrics.accuracy_score(y_test, y_test_pred)
print(test_accuracy)