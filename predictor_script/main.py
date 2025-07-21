from joblib import load
import numpy as np

# load the model from notebook
model = load('pipe.joblib')

# begin the python script
print("\t\tEXAM SCORE PREDICTOR\t\t")
print("+----------------------------------+")
print("Predict your exam score by answering \n"
      "the questions below!\n")

# query the user's age
age_range = tuple(range(0, 111))
age = int(input("What is your age? [0-110]: "))

while True:
    if age in age_range:
        break
    age = int(input(f"Out of range: {age}\nWhat is your age? [0-110]: "))

# query the user's gender
gender_choices = {'male', 'female', 'other'}
gender_conversion = {"male": 0, "female": 1, "other": 2}

gender = input("What is your gender? [male/female/other]: ").strip().lower()
while True:
    if gender in gender_choices:
        break
    gender = input(f"Invalid choice: {gender}. Please enter one of "
                   f"[male/female/other]: ").strip().lower()

gender = gender_conversion[gender]

# query the user's study hours per day
hours_range = tuple(range(0, 25))
study_hours = int(input("On average, how many hours did you study per day? "
                        "[0-24]: "))

while True:
    if study_hours in hours_range:
        break
    study_hours = int(input(f"Out of range: {study_hours}\n"
                            f"On average, how many hours did you study per day?"
                            f" [0-24]: "))

# query the user's social media hours per day
social_media_hours = int(input("On average, how many hours did you spend on "
                               "social media per day? [0-24]: "))

while True:
    if social_media_hours in hours_range:
        break
    social_media_hours = int(input(f"Out of range: {social_media_hours}\n"
                            f"On average, how many hours did you spend on"
                            f"social media per day? [0-24]: "))

# query the user's netflix hours per day
netflix_hours = int(input("On average, how many hours did you spend on "
                          "netflix per day? "))

while True:
    if netflix_hours in hours_range:
        break
    netflix_hours = int(input(f"Out of range: {netflix_hours}\n"
                              f"On average, how many hours did you spend on"
                              f"netflix per day? [0-24]: "))

# query the user's employment status
emp_status_choices = {'yes', 'no'}
emp_status_conversion = {'no': 0, 'yes': 1}

emp_status = input("Do you have a part-time job? [yes/no]: ").strip().lower()
while True:
    if emp_status in emp_status_choices:
        break
    job_status = input(f"Invalid choice: {emp_status}. Please enter one of"
                       f"[yes/no]: ").strip().lower()

job_status = emp_status_conversion[emp_status]

# query the user's attendance percentage
attendance_pct_range = tuple(range(0, 101))
attendance_pct = int(input("What was your class attendance percentage? "
                           "[0-100]: "))

while True:
    if attendance_pct in attendance_pct_range:
        break
    attendance_pct = int(input(f"Out of range: {attendance_pct}\n"
                               "What was your class attendance percentage? "
                               "[0-100]: "))

# query the user's sleep hours per day
sleep_hours = int(input("On average, how many hours did you sleep per night? "
                        "[0-24]: "))

while True:
    if sleep_hours in hours_range:
        break
    sleep_hours = int(input(f"Invalid choice: {sleep_hours}\n"
                            f"On average, how many hours did you sleep per"
                            f"night? [0-24]: "))

# query the user's diet quality
diet_quality_choices = {'poor', 'fair', 'good'}
diet_quality_conversion = {'poor': 0, 'fair': 1, 'good': 2}

diet_quality = input("What is your diet quality? [poor/fair/good]:"
                     " ").strip().lower()

while True:
    if diet_quality in diet_quality_choices:
        break
    diet_quality = input("Invalid choice. Please enter one of [poor/fair/good]"
                         ": ").strip().lower()

diet_quality = diet_quality_conversion[diet_quality]

# query the user's exercise_frequency
exercise_freq_range = tuple(range(0, 8))
exercise_freq = int(input("How many days per week do you exercise? [0-7]: "))

while True:
    if exercise_freq in exercise_freq_range:
        break
    exercise_freq = int(input(f"Invalid choice: {exercise_freq}\n"
                              f"How many days per week do you exercise? [0-7]"
                              ": "))










