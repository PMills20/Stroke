from flask import Flask, render_template
import pickle
import pandas as pd

with open(f'model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/comparisons.html')
def main():
    return(render_template('comparisons.html'))
    age = 25
    hypertension = 0
    heart_disease = 1
    avgglucose = 93
    bmi = 30
    female = 1
    male = 0
    other = 0
    marriedNo = 1
    marriedYes = 0
    smokingUnknown = 0
    smokingFormer = 0
    smokingNever = 0
    smokes = 1
    inputs = pd.DataFrame([[age, hypertension, heart_disease, avgglucose, bmi, female, male, other, marriedNo, marriedYes,
    smokingUnknown, smokingFormer, smokingNever, smokes]], columns = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level',
    'bmi', 'gender_Female', 'gender_Male', 'gender_Other', 'ever_married_No', 'ever_Married_Yes', 'smoking_status_Unknown',
    'smoking_status_formerlysmoked', 'smoking_status_neversmoked', 'smoking_status_smokes'])
    prediction = model.predict(inputs)[0]

    return render_template('comparisons.html',
        original_input={'age':age, 'hypertension':hypertension, 'heart_disease':heart_disease, 'avg_glucose_level':avgglucose,
    'bmi':bmi, 'gender_Female':female, 'gender_Male':male, 'gender_Other':other, 'ever_married_No':marriedNo, 'ever_Married_Yes':marriedYes, 
    'smoking_status_Unknown': smokingUnknown,
    'smoking_status_formerlysmoked': smokingFormer, 'smoking_status_neversmoked':smokingNever, 'smoking_status_smokes':smokes},result=prediction,)

if __name__ == '__main__':
    app.run()