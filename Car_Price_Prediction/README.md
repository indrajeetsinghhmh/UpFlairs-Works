# Car Price Predictor



<img src="https://i.pinimg.com/564x/8b/37/c6/8b37c6ff0e943508b58723bb5eca0e57.jpg">



# Aim

This project aims to predict the Price of an used Car by taking it's Company name, it's Model name, Year of Purchase, and other parameters.

<img src="https://miro.medium.com/v2/resize:fit:1400/1*hZn1cA0drtsQkwN_vKgRWQ.jpeg">

## How to use?

1. Clone the repository
2. Install the required packages in "requirements.txt" file.

Some packages are:
 - numpy 
 - pandas 
 - scikit-learn

3. Run the "application.py" file
And you are good to go. 

# Description

## What this project does?

1. This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
2. It then predicts the possible price of the car. For example, the image below shows the predicted price of our Hyundai Grand i10. 

<img src="https://github.com/rajtilakls2510/car_price_predictor/blob/master/predict.png">

## How this project does?

1. First of all the data was scraped from Quikr.com (https://quikr.com) 
Link for data: https://github.com/indrajeetsinghhmh/UpFlairs-Works/Car_Price_Prediction/quikr_car.csv

2. The data was cleaned (it was super unclean :( ) and analysed.

3. Then a Linear Regression model was built on top of it which had 0.92 R2_score.

Link for notebook: https://github.com/indrajeetsinghhmh/UpFlairs-Works/Car_Price_Prediction/Quikr%20Analysis.ipynb

4. This project was given the form of an website built on Flask where we used the Linear Regression model to perform predictions.

