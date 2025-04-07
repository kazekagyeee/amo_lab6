from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Загрузка датасета
iris = load_iris()
X = iris.data
y = iris.target

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Тестовый пример для предсказания
test_sample = np.array([[1, 1, 1, 1]])

# Получение предсказания
prediction = model.predict(test_sample)

# Вывод результата
print(f"Предсказанный класс ириса: {prediction[0]}")
print(f"Название класса: {iris.target_names[prediction[0]]}") 