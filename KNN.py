import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('Wine dataset.csv')

X = df.drop('class', axis = 1)
y = df['class']  

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.2,      
    random_state = 1,    
    stratify = y          
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train_scaled, y_train)

#print(knn.score(X_test_scaled, y_test))

param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'minkowski']
}

grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv = 5, scoring = 'accuracy')

grid.fit(X_train_scaled, y_train)

print("Лучшие параметры:", grid.best_params_)
print("Лучшая точность на кросс-валидации:", grid.best_score_)

best_knn = grid.best_estimator_

test_accuracy = best_knn.score(X_test_scaled, y_test)

print(f"Итоговая точность на тестовой выборке: {test_accuracy}")