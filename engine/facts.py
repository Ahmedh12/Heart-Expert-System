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

####################################################Utility Exceptions####################################################
class InvalidFact(Exception):
    pass
##########################################################################################################################


class age(Fact): #Age
    def validate(self):
        try:
            age = float(self["age"])
            if age < 0:
                raise InvalidFact("Age cannot be negative.")
            return True, ""
        except ValueError:
            raise InvalidFact("Age must be a number.")
            # return False, "Age must be a number."

class sex(Fact): #Sex
    def validate(self):
        try:
            sex = int(self["sex"])
            if sex not in [0, 1]:
                raise InvalidFact("Gender should only be 0 for `Female` or 1 for `Male`")
        except ValueError:
            raise InvalidFact("Gender should only be 0 for `Female` or 1 for `Male`")


class cp(Fact):  # Chest pain type (0-3)
    def validate(self):
        try:
            cp = int(self["cp"])
            if cp not in [0, 1, 2, 3]:
                raise InvalidFact("Chest pain type must be an integer between 0 and 3.")
        except ValueError:
            raise InvalidFact("Chest pain type must be a number.")

class trestbps(Fact):  # Resting blood pressure
    def validate(self):
        try:
            bp = float(self["trestbps"])
            if bp <= 0:
                raise InvalidFact("Blood pressure must be a positive number.")
        except ValueError:
            raise InvalidFact("Blood pressure must be a number.")

class chol(Fact):  # Serum cholesterol
    def validate(self):
        try:
            chol = float(self["chol"])
            if chol <= 0:
                raise InvalidFact("Cholesterol must be a positive number.")
        except ValueError:
            raise InvalidFact("Cholesterol must be a number.")

class fbs(Fact):  # Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    def validate(self):
        try:
            fbs = int(self["fbs"])
            if fbs not in [0, 1]:
                raise InvalidFact("Fasting blood sugar must be 0 or 1.")
        except ValueError:
            raise InvalidFact("Fasting blood sugar must be 0 or 1.")

class restecg(Fact):  # Resting electrocardiographic results (0-2)
    def validate(self):
        try:
            ecg = int(self["restecg"])
            if ecg not in [0, 1, 2]:
                raise InvalidFact("Resting ECG result must be 0, 1, or 2.")
        except ValueError:
            raise InvalidFact("Resting ECG result must be a number.")

class thalach(Fact):  # Maximum heart rate achieved
    def validate(self):
        try:
            rate = float(self["thalach"])
            if rate <= 0:
                raise InvalidFact("Maximum heart rate must be a positive number.")
        except ValueError:
            raise InvalidFact("Maximum heart rate must be a number.")

class exang(Fact):  # Exercise induced angina (1 = yes; 0 = no)
    def validate(self):
        try:
            exang = int(self["exang"])
            if exang not in [0, 1]:
                raise InvalidFact("Exercise-induced angina must be 0 or 1.")
        except ValueError:
            raise InvalidFact("Exercise-induced angina must be 0 or 1.")

class oldpeak(Fact):  # ST depression induced by exercise
    def validate(self):
        try:
            val = float(self["oldpeak"])
            if val < 0:
                raise InvalidFact("Oldpeak must be non-negative.")
        except ValueError:
            raise InvalidFact("Oldpeak must be a number.")

class slope(Fact):  # Slope of the peak exercise ST segment (0-2)
    def validate(self):
        try:
            slope = int(self["slope"])
            if slope not in [0, 1, 2]:
                raise InvalidFact("Slope must be 0, 1, or 2.")
        except ValueError:
            raise InvalidFact("Slope must be a number.")

class ca(Fact):  # Number of major vessels colored by fluoroscopy (0–3)
    def validate(self):
        try:
            ca = int(self["ca"])
            if ca not in [0, 1, 2, 3]:
                raise InvalidFact("Number of vessels must be between 0 and 3.")
        except ValueError:
            raise InvalidFact("Number of vessels must be a number.")

class thal(Fact):  # Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)
    def validate(self):
        try:
            thal = int(self["thal"])
            if thal not in [1, 2, 3]:
                raise InvalidFact("Thal must be 1 (normal), 2 (fixed defect), or 3 (reversible defect).")
        except ValueError:
            raise InvalidFact("Thal must be a number.")

class diagnosis(Fact):  # Target diagnosis (0 = no disease, 1 = disease)
    pass