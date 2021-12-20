## Understanding Machine Learning Algorithms
### With the [Top 100 anime rating dataset](https://github.com/apeksha235/data_science/blob/main/Week_5/final_anime_dataset.csv) several Machine Learning Algorithms have been implemented. These are the following: 
- Linear Regression 
- TheilSen Regressor 
- RANSAC Regressor
- Huber Regressor
- Passive Aggresive Regressor
- Gaussian Process Regressor
- Support Vector Machine
- NU Support Vector Regression 
- KNNeighbours as Regressor
- Stochastic Gradient Descent
- Kernel Ridge Regression 
- Decision Tree
- Random Forest
- Extra Trees
- Bagging Regressor
- ADABoost Regressor
- XGBoost 
- Gradient Boosting

### I took the ```Mean Squared Error``` for every model, and analysed the loss for each. Here are my conclusions: 
 - As shown above ``` Mean Squared Error``` has one of the lowest values in the Boosting techniques and Linear regression models. Hence they are the best working model for this dataset.
 - The highest loss is mainly witnessed in bagging trees since the input data for prediction contains 95% categorical features this results in sparse data reducing the efficiency of these tree based models.

## Link to the kaggle notebook: [click here](https://www.kaggle.com/apeksha23/machine-learning-algorithms-on-anime-dataset)
