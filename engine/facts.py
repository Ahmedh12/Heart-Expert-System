from experta import Fact

fact_names = [
    "age", "sex", "cp", "trestbps", "chol", 
    "fbs", "restecg", "thalach", "exang", 
    "oldpeak", "slope", "ca", "thal", "diagnosis"]

fact_names_description = {
    "age": "Age",
    "sex": "Gender",
    "cp": "Chest Pain Type",
    "trestbps": "Resting Blood Pressure",
    "chol": "Serum Cholestoral",
    "fbs": "Fasting Blood Sugar",
    "restecg": "Resting Electrocardiographic Results",
    "thalach": "Maximum Heart Rate Achieved",
    "exang": "Exercise Induced Angina",
    "oldpeak": "ST Depression Induced by Exercise Relative to Rest",
    "slope": "Slope of the Peak Exercise ST Segment",
    "ca": "Number of Major Vessels (0-3) Colored by Fluoroscopy",
    "thal": "Thalassemia",
    "diagnosis": "Diagnosis"
}

class age(Fact): #Age
    def validate(self, age):
        try:
            age = float(age)
            if age < 0:
                return False, "Age should be a non-negative value."
            return True, ""
        except ValueError:
            return False, "Age must be a number."

class sex(Fact): #Sex
    def validate(self, sex):
        try:
            sex = int(sex)
            if sex not in [0, 1]:
                return False, "Sex should be either 0 for male or 1 for female."
            return True, ""
        except ValueError:
            return False, "Sex must be either 0 or 1."

class cp(Fact): #Chest Pain
    pass

class trestbps(Fact): #Resting Blood Pressure
    pass

class chol(Fact): #Serum Cholestoral
    pass

class fbs(Fact): #Fasting Blood Sugar
    pass

class restecg(Fact): #Resting Electrocardiographic Results
    pass

class thalach(Fact): #Maximum Heart Rate Achieved
    pass

class exang(Fact): #Exercise Induced Angina
    pass

class oldpeak(Fact): #ST Depression Induced by Exercise Relative to Rest
    pass

class slope(Fact): #Slope of the Peak Exercise ST Segment
    pass

class ca(Fact): #Number of Major Vessels (0-3) Colored by Fluoroscopy
    pass

class thal(Fact): #Thalassemia
    pass

class diagnosis(Fact): #Diagnosis
    pass