
from sklearn.linear_model import LinearRegression

# Input data: study hours
X = [[1], [2], [3], [4], [5]]

# Output data: marks
y = [35, 45, 55, 65, 75]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

# Display the result
print("Study hours: 6")
print("Predicted marks:", prediction[0])
