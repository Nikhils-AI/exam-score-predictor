# **Exam Score Predictor**

The _Exam Score Predictor_ is a machine learning-powered Python script that enables the user to predict their expected exam score based on their habits and lifestyle. 

## **Features**

- Predicts exam score (0 - 100%) using a trained machine learning linear regression model
- Clean script interface
- Takes inputs such as study hours, social media hours, sleep hours, etc. as feature values
- Built using Python, Pandas, Scikit-learn, and Joblib

---

## **Windows Installation**

1. Clone the repo:
   '''cmd
   git clone https://github.com/Nikhils-AI/exam-score-predictor.git
   cd exam-score-predictor

2. Create and activate a virtual environment:
   '''cmd
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   '''cmd
   pip install -r requirements.txt

4. Run script:
   python scripts/main.py

   ## **Project Structure**

   exam-score-predictor/
│
├── data/
│ └── student_habits_performance.csv # raw dataset
│
├── model/
│ └── pipe.joblib # trained pipeline
│
├── notebooks/
| └── exam_score_predictor.ipynb # where model was trained
|
|── scripts/
| |── conversion_safety.py # module containing functions
  └── main.py # script file
|
|── .gitignore
|
├── requirements.txt
└──README.md
   
