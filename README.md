# 🧾 **Exam Score Predictor**

The _Exam Score Predictor_ is a machine learning-powered Python script that enables the user to predict their expected exam score based on their habits and lifestyle. 

## 📌 **Features**

- Predicts exam score (0 - 100%) using a trained machine learning linear regression model
- Clean script interface
- Takes inputs such as study hours, social media hours, sleep hours, etc. as feature values
- Built using Python, Pandas, NumPy, Matplotlib, and Joblib

---

## 🛠️ **Windows Installation**

1. Clone the repo:
   ```cmd
   git clone https://github.com/Nikhils-AI/exam-score-predictor.git
   cd exam-score-predictor

2. Create and activate a virtual environment:
   ```cmd
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   ```cmd
   pip install -r requirements.txt

4. Run script:
   ```cmd
   cd scripts
   python main.py

---

## 📁 **Project Structure**

<pre><code>
exam-score-predictor/
│
├── data/
│ └── student_habits_performance.csv      # Contains the raw CSV 
│
├── model/
│ └── pipe.joblib                         # The final pipeline 
│
├── notebooks/
| └── exam_score_predictor.ipynb          # jupyter notebook for inspecting data and selecting final model
|
|── scripts/
| |── conversion_safety.py                # module containing helper functions to verify safe data type conversion
| └── main.py                             # main script file
|
|── .gitignore
|── README.md
└──requirements.txt
</code></pre>
   

   
