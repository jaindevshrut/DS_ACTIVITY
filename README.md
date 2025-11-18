# Flight Price Prediction - Data Science Activity

This repository showcases a comprehensive Data Science learning project for predicting flight ticket prices using various regression algorithms. The project demonstrates the complete data science workflow from exploratory data analysis to model deployment.

## 📊 Project Overview

This project analyzes flight booking data from various Indian airlines to predict ticket prices based on multiple features such as airline, route, departure time, number of stops, class, and booking urgency. The dataset is scraped from a popular flight booking website and contains structured information about flight travel details between cities in India.

## 🎯 Objective

To build and compare multiple machine learning models that can accurately predict flight ticket prices, helping travelers make informed booking decisions and airlines optimize their pricing strategies.

## 📁 Project Structure

```
DS_ACTIVITY/
│
├── airlines-flights-data-analysis-with-python.ipynb  # EDA & Data Cleaning
├── model_linear_regression.ipynb                      # Linear Regression Model
├── model_random_forest.ipynb                          # Random Forest Model
├── model_xgboost.ipynb                               # XGBoost Model
├── flight_predict_using_formula.py                   # Prediction Script
└── README.md                                         # Project Documentation
```

## 📋 Dataset Features

The dataset contains the following features:

1. **Airline**: Name of the airline company (6 unique airlines)
2. **Flight**: Flight code information (categorical)
3. **Source City**: Departure city (6 unique cities)
4. **Destination City**: Arrival city (6 unique cities)
5. **Departure Time**: Categorized departure time period (6 time labels)
6. **Arrival Time**: Categorized arrival time period (6 time labels)
7. **Stops**: Number of stops between source and destination (0, 1, or 2+ stops)
8. **Class**: Seat class - Business or Economy
9. **Duration**: Total travel time in hours (continuous)
10. **Days Left**: Days between booking date and travel date
11. **Price**: Ticket price in rupees (Target Variable)

## 🔬 Machine Learning Models

### 1. Linear Regression Model
- **Algorithm**: Ordinary Least Squares Linear Regression
- **Preprocessing**: StandardScaler for feature normalization
- **Features**: 80/20 train-test split
- **Use Case**: Baseline model for interpretable linear relationships
- **Advantages**: 
  - Simple and fast to train
  - Highly interpretable coefficients
  - Good for understanding feature impact

### 2. Random Forest Model
- **Algorithm**: Random Forest Regressor
- **Hyperparameter Tuning**: RandomizedSearchCV (5 iterations, 2-fold CV)
- **Key Parameters Tuned**:
  - n_estimators: [100, 150, 200, 250, 300]
  - max_depth: [10, 20, 30, 40, None]
  - min_samples_split: [2, 5, 10, 15]
  - min_samples_leaf: [1, 2, 4, 6]
  - max_features: ['sqrt', 'log2', None]
- **Advantages**:
  - Captures non-linear relationships
  - Provides feature importance
  - Robust to outliers
  - No feature scaling required

### 3. XGBoost Model
- **Algorithm**: XGBoost Regressor (Gradient Boosting)
- **Hyperparameter Tuning**: RandomizedSearchCV (5 iterations, 2-fold CV)
- **Key Parameters Tuned**:
  - n_estimators: [100, 200, 300]
  - max_depth: [3, 5, 7, 10]
  - learning_rate: [0.01, 0.05, 0.1]
  - subsample: [0.7, 0.8, 1.0]
  - colsample_bytree: [0.7, 0.8, 1.0]
  - min_child_weight: [1, 3, 5]
- **Advantages**:
  - Best performance on tabular data
  - Built-in regularization
  - Handles missing values
  - Excellent for complex patterns

## 📈 Model Evaluation Metrics

All models are evaluated using:
- **R² Score**: Variance explained by the model (higher is better)
- **RMSE**: Root Mean Squared Error in rupees (lower is better)
- **MAE**: Mean Absolute Error in rupees (lower is better)
- **MAPE**: Mean Absolute Percentage Error (lower is better)

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **XGBoost**: Gradient boosting framework
- **Pickle**: Model serialization

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```

### Running the Analysis

1. **Exploratory Data Analysis**:
   ```bash
   jupyter notebook airlines-flights-data-analysis-with-python.ipynb
   ```

2. **Train Linear Regression Model**:
   ```bash
   jupyter notebook model_linear_regression.ipynb
   ```

3. **Train Random Forest Model**:
   ```bash
   jupyter notebook model_random_forest.ipynb
   ```

4. **Train XGBoost Model**:
   ```bash
   jupyter notebook model_xgboost.ipynb
   ```

5. **Make Predictions**:
   ```bash
   python flight_predict_using_formula.py
   ```

## 📊 Key Insights

- **Feature Engineering**: Created categorical features for departure/arrival periods and booking urgency
- **Encoding**: Used label encoding and one-hot encoding for categorical variables
- **Model Performance**: XGBoost typically provides the best performance, followed by Random Forest and Linear Regression
- **Important Features**: Duration, days left before travel, airline, class, and number of stops are key price determinants

## 📝 Workflow Summary

1. **Data Collection**: Scraped flight booking data
2. **Data Cleaning**: Handled missing values, removed duplicates, cleaned inconsistent data
3. **Exploratory Data Analysis**: Visualized patterns, correlations, and distributions
4. **Feature Engineering**: Created derived features and encoded categorical variables
5. **Model Training**: Trained three regression models with hyperparameter tuning
6. **Model Evaluation**: Compared models using multiple metrics
7. **Model Selection**: Selected best model based on performance metrics
8. **Model Deployment**: Saved models for future predictions

## 🎓 Learning Outcomes

- End-to-end machine learning pipeline implementation
- Feature engineering for categorical and numerical data
- Hyperparameter tuning using RandomizedSearchCV
- Model comparison and selection strategies
- Best practices for regression tasks
- Model interpretation and feature importance analysis

## 👥 Contributors

This is a collaborative data science activity project.

## 📄 License

This project is for educational purposes as part of a Data Science course activity.

## 🔗 Acknowledgments

- Dataset source: Kaggle Airlines Flights Data
- Course: Data Science Lab (Semester V)
- Institution: CLLG

---

**Note**: This project demonstrates practical machine learning skills in a real-world domain (airline pricing), covering the complete data science workflow from data exploration to model deployment.
