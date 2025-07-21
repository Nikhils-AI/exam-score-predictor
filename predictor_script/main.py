from joblib import load
import numpy as np

# load in estimator from notebook
model = load('pipe.joblib')

# begin python script
print("\t\tEXAM SCORE PREDICTOR\t\t")
print("+----------------------------------+")
print("Predict your exam score by answering \n"
      "the questions below!\n")

# query age
age = int(input("What is your age? ").strip())

# query genderS
genders = {'male', 'female', 'other'}
gender_conversion = {"male": 0, "female": 1, "other": 2}

gender = input("What is your gender? [male/female/other]: ").strip().lower()
while True:
    if gender in genders:
        break
    gender = input(f"Invalid choice: {gender}. Please enter one of "
                   f"[male/female/other]: ")

gender = gender_conversion[gender]

# query study hours per day
study_hours = int(input("On average, how many hours did you study per day? "))

# query social media hours per day
social_media_hours = int(input("On average, how many hours did you spend on "
                               "social media per day? "))

# query netflix hours per day
netflix_hours = int(input("On average, how many hours did you spend on "
                          "netflix per day? "))




