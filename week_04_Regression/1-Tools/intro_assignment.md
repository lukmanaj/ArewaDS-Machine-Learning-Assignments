# Regression with Scikit-learn

Instructions

Take a look at the Linnerud dataset in Scikit-learn. This dataset has multiple targets: 'It consists of three exercise (data) and three physiological (target) variables collected from twenty middle-aged men in a fitness club'.

In your own words, describe how to create a Regression model that would plot the relationship between the waistline and how many situps are accomplished. Do the same for the other datapoints in this dataset.

## Answer

The linnerud dataset has three targets: ['Weight', 'Waist', 'Pulse']
and three features: ['Chins', 'Situps', 'Jumps']

To plot the relationship between the waistline and number of situps accomplished, I just need to select X such that it is the number of situps and then select y as 'Waist'.
This can be accomplished by modifying the line here in the lesson for both X and y since in our case here, y has multiple targets, unlike the diabetes dataset we worked on in the lesson:

```py
X = X[:,np.newaxis,1]
y = y[:,np.newaxix,1]

```

For the other features, we edit the numbers to reflect the position in the arrays above, for both features (X) and targets (y)

Then we proceed with the code as usual:

```py
# split the data into training and testing sets
X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.3)

# train the model
model = linear_model.LinearRegression()
model.fit(X_train,y_train)

# predict using test data
y_pred = model.predict(X_test)

# finally plot
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Number of situps')
plt.ylabel('Waistline')
plt.title('A Graph Plot of Relationship between Waistline and Number of situps')
plt.show()

```

The same applies for the other data points, we just swap out the line below:

```py

X = X[:,np.newaxis,1]
y = y[:,np.newaxix,1]

```

In total, the following combinations are possible:

- Weight - Chins
- Weight - Situps
- Weight - Jumps
- Waist - Chins
- Waist - Jumps
- Pulse - Chins
- Pulse - Situps
- Pulse - Jumps
