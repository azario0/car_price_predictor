# Car Price Predictor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning project to predict the price of second-hand cars. This repository includes a Jupyter Notebook for model training and a Flask web application to serve the best-performing model for real-time predictions.

  <!-- Optional: Add a screenshot or GIF of your web app here -->

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [License](#license)
- [Contact](#contact)

## Project Description
This project aims to build an accurate and reliable model for predicting the price of used cars based on their features like manufacturer, model, age, mileage, and fuel type.

The process involves:
1.  Loading and exploring the car sales dataset.
2.  Performing feature engineering by creating an 'Age' feature from the 'Year of manufacture'.
3.  Preprocessing the data using `StandardScaler` for numerical features and `OneHotEncoder` for categorical features.
4.  Training and evaluating four different regression models: Linear Regression, Ridge, RandomForest, and GradientBoosting.
5.  Saving the best model (RandomForest Regressor) as a pipeline using `joblib`.
6.  Developing a user-friendly web interface with Flask that uses the saved model to provide price predictions on new data.

## Features
- **Data Preprocessing:** Robust preprocessing pipeline to handle both numerical and categorical data.
- **Multiple Model Training:** Compares the performance of four different regression algorithms.
- **Model Persistence:** Saves the entire preprocessing and prediction pipeline for easy deployment.
- **Web Application:** A clean and simple Flask web app for users to get instant price predictions.
- **Detailed Analysis:** A Jupyter Notebook (`notebook.ipynb`) documenting the entire workflow from data loading to model evaluation.

## Dataset
The model is trained on the **Mock Dataset of Second Hand Car Sales** from Kaggle.
- **Link:** [https://www.kaggle.com/datasets/msnbehdani/mock-dataset-of-second-hand-car-sales](https://www.kaggle.com/datasets/msnbehdani/mock-dataset-of-second-hand-car-sales)

The dataset includes the following columns: `Manufacturer`, `Model`, `Engine size`, `Fuel type`, `Year of manufacture`, `Mileage`, and `Price`.


## Technologies Used
- **Programming Language:** Python 3
- **Libraries:**
  - **Data Analysis & ML:** Pandas, NumPy, Scikit-learn, Joblib
  - **Web Framework:** Flask
  - **Development Environment:** Jupyter Notebook

## Usage

### Running the Flask Web Application

Once the setup is complete, you can start the web server to use the prediction tool.

**1. Start the Flask server:**
```bash
python car_price_predictor/app.py
```

**2. Access the application:**
Open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

You will see a form where you can input the details of a car. After submitting the form, the application will display the predicted price.

## Model Performance
Four different models were trained and evaluated. The **RandomForest Regressor** provided the best performance by a significant margin, capturing the complex relationships in the data effectively.

| Model                 | Mean Absolute Error (MAE) | R-squared (R²) |
| --------------------- | ------------------------- | -------------- |
| Linear Regression     | 5786.31                   | 0.7102         |
| Ridge                 | 5786.14                   | 0.7102         |
| **RandomForest**      | **286.04**                | **0.9986**     |
| Gradient Boosting     | 1037.39                   | 0.9899         |

The high R² score of 0.9986 indicates that the RandomForest model explains almost all the variance in the car prices, making it highly reliable for this prediction task.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
Created by [azario0](https://github.com/azario0) - feel free to reach out