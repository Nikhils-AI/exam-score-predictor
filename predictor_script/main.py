from joblib import load
import numpy as np

# load the final pipe from notebook
pipe = load('pipe.joblib')

# begin the python script
print("\t\tEXAM SCORE PREDICTOR\t\t")
print("+----------------------------------+")
print("Predict your exam score by answering \n"
      "the questions below!")

# query the user's age
age_range = tuple(range(0, 111))
age = input("\nWhat is your age? [0 - 110]: ")

while True:
    if age in age_range and isinstance():
        break
    age = input(f"Out of range: {age}\nWhat is your age? [0 - 110]: ")

age = int(age)

# query the user's gender
gender_choices = {'male', 'female', 'other'}
gender_conversion = {"male": 0, "female": 1, "other": 2}

gender = input("\nWhat is your gender? [male/female/other]: ").strip().lower()
while True:
    if gender in gender_choices:
        break
    gender = input(f"Invalid choice: {gender}\n"
                   f"Please enter one of [male/female/other]: ").strip().lower()

gender = gender_conversion[gender]

# query the user's study hours per day
hours_range = tuple(range(0, 25))
study_hours = input("\nOn average, how many hours did you study per day? "
                        "[0 - 24]: ")

while True:
    if study_hours in hours_range and type(study_hours) == 'int':
        break
    study_hours = input(f"Out of range: {study_hours}\n"
                            f"On average, how many hours did you study per day?"
                            f" [0 - 24]: ")

# query the user's social media hours per day
social_media_hours = int(input("\nOn average, how many hours did you spend on "
                               "social media per day? [0 - 24]: "))

while True:
    if social_media_hours in hours_range:
        break
    social_media_hours = int(input(f"Out of range: {social_media_hours}\n"
                            f"On average, how many hours did you spend on "
                            f"social media per day? [0 - 24]: "))

# query the user's netflix hours per day
netflix_hours = int(input("\nOn average, how many hours did you spend on "
                          "netflix per day? [0 - 24]: "))

while True:
    if netflix_hours in hours_range:
        break
    netflix_hours = int(input(f"Out of range: {netflix_hours}\n"
                              f"On average, how many hours did you spend on "
                              f"netflix per day? [0 - 24]: "))

# query the user's employment status
emp_status_choices = {'yes', 'no'}
emp_status_conversion = {'no': 0, 'yes': 1}

emp_status = input("\nDo you have a part-time job? [yes/no]: ").strip().lower()
while True:
    if emp_status in emp_status_choices:
        break
    emp_status = input(f"Invalid choice: {emp_status}\n"
                       f"Please enter one of [yes/no]: ").strip().lower()

emp_status = emp_status_conversion[emp_status]

# query the user's attendance percentage
attendance_pct_range = tuple(np.arange(0.00, 100.01, 0.01).round(2).tolist())
attendance_pct = float(input("\nWhat was your class attendance percentage? "
                           "[0.00 - 100.00]: "))

while True:
    if attendance_pct in attendance_pct_range:
        break
    attendance_pct = float(input(f"Out of range: {attendance_pct}\n"
                               "What was your class attendance percentage? "
                               "[0.00 - 100.00]: "))

# query the user's sleep hours per day
sleep_hours = int(input("\nOn average, how many hours did you sleep per night? "
                        "[0 - 24]: "))

while True:
    if sleep_hours in hours_range:
        break
    sleep_hours = int(input(f"Invalid choice: {sleep_hours}\n"
                            f"On average, how many hours did you sleep per"
                            f"night? [0 - 24]: "))

# query the user's diet quality
diet_quality_choices = {'poor', 'fair', 'good'}
diet_quality_conversion = {'poor': 0, 'fair': 1, 'good': 2}

diet_quality = input("\nWhat is your diet quality? [poor/fair/good]:"
                     " ").strip().lower()

while True:
    if diet_quality in diet_quality_choices:
        break
    diet_quality = input(f"Invalid choice: {diet_quality}\n"
                         f"Please enter one of [poor/fair/good]: "
                         f"").strip().lower()

diet_quality = diet_quality_conversion[diet_quality]

# query the user's exercise_frequency
exercise_freq_range = tuple(range(0, 8))
exercise_freq = int(input("\nHow many days per week do you exercise? "
                          "[0 - 7]: "))

while True:
    if exercise_freq in exercise_freq_range:
        break
    exercise_freq = int(input(f"Invalid choice: {exercise_freq}\n"
                              f"How many days per week do you exercise? "
                              f"[0 - 7]: "))

# query the user's parental education level
parent_edu_choices = {'high school', 'bachelor', 'master'}
parent_edu_conversion = {'high school': 0, 'bachelor': 1, 'master': 2}

parent_edu = input("\nWhat is your parents' highest education level? "
                   "[high school/bachelor/master]: ").strip().lower()

while True:
    if parent_edu in parent_edu_choices:
        break
    parent_edu = input(f"Invalid choice: {parent_edu}\n"
                       f"Please enter one of [high school/bachelor/master]: "
                       f"").strip().lower()

parent_edu = parent_edu_conversion[parent_edu]

# query the user's internet quality
internet_quality_choices = {'poor', 'average', 'good'}
internet_quality_conversion = {'poor': 0, 'average': 1, 'good': 2}

internet_quality = input("\nWhat is your internet quality? [poor/average/good]"
                         ": ").strip().lower()

while True:
    if internet_quality in internet_quality_choices:
        break
    internet_quality = input(f"Invalid choice: {internet_quality}\n"
                             f"Please enter one of [poor/average/good]: "
                             f"").strip().lower()

internet_quality = internet_quality_conversion[internet_quality]

# query the user's mental health rating
mental_health_range = tuple(range(0, 11))
mental_health = int(input("\nWhat is your mental health rating? "
                          "[0 (Worst) - 10 (Best)]: "))

while True:
    if mental_health in mental_health_range:
        break
    mental_health = int(input(f"Invalid choice: {mental_health}\n"
                              f"What is your mental health rating?"
                              f"[0 (Worst) - 10 (Best): "))

# query the user's extracurricular participation
extra_curr_choices = {'yes', 'no'}
extra_curr_conversion = {'no': 0, 'yes': 1}

extra_curr = input("\nDid you participate in any extracurricular activities? "
                   "[yes/no]: ").strip().lower()

while True:
    if extra_curr in extra_curr_choices:
        break
    extra_curr = input(f"Invalid choice: {extra_curr}\n"
                           f"Please enter one of the following [yes/no]: "
                           f"").strip().lower()

extra_curr = extra_curr_conversion[extra_curr]

# synthesize results into numpy array
results = np.array([age, gender, study_hours, social_media_hours,
                    netflix_hours, emp_status, attendance_pct, sleep_hours,
                    diet_quality, exercise_freq, parent_edu, internet_quality,
                    mental_health, extra_curr]).reshape(1, -1)

# output exam score prediction with pipe
score_prediction = pipe.predict(results)[0]

if score_prediction < 0:
    score_prediction = 0

if score_prediction > 100:
    score_prediction = 100

print(f"Predicted Exam Score: {score_prediction}")











