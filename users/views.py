from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import UserRegistrationForm
from .models import UserRegistrationModel

import os
import logging
import warnings
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report
)


warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================
# USER REGISTRATION
# ============================
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been successfully registered')
        else:
            messages.error(request, 'Email or Mobile already exists')

    return render(request, 'UserRegistrations.html', {'form': UserRegistrationForm()})


# ============================
# USER LOGIN
# ============================
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')

        try:
            user = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            if user.status == "activated":
                request.session['loginid'] = loginid
                request.session['name'] = user.name
                return render(request, 'users/UserHomePage.html')
            else:
                messages.error(request, 'Account not activated')
        except:
            messages.error(request, 'Invalid Login ID or Password')

    return render(request, 'UserLogin.html')


def UserHome(request):
    return render(request, 'users/UserHomePage.html')


# ============================
# MODEL TRAINING
# ============================
def training(request):
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    csv_path = os.path.join(
        settings.MEDIA_ROOT,
        'online_course_ml_ready_-1_0_1_NO_CLICKS.csv'
    )

    if not os.path.exists(csv_path):
        return render(request, 'users/training.html', {
            'error': 'CSV file not found'
        })

    df = pd.read_csv(csv_path)

    FEATURES = [
        "daysOfTraining",
        "refToMaterials",
        "averageScore",
        "numOfIntermediateClasses"
    ]

    X = df[FEATURES]
    y = df["final_result_-1_0_1"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    model_name="RandomForestClassifier"
    accuracy = round(accuracy_score(y_test, y_pred), 4)
#    f1score=round(f1_score(y_test,y_pred),4)
    classificationreport=classification_report(y_test,y_pred)
    confusionmatrix=confusion_matrix(y_test,y_pred)
    # SAVE
    joblib.dump(model, os.path.join(settings.MEDIA_ROOT, 'RandomForest_model.joblib'))
    joblib.dump(scaler, os.path.join(settings.MEDIA_ROOT, 'scaler.joblib'))

    return render(request, 'users/training.html', {
        'model_name':model_name,
        'accuracy': accuracy,
        
        'classification_report':classificationreport,
        'confusion_matrix':confusionmatrix,
        'trained': True
    })


# ============================
# PREDICTION LOGIC
# ============================
def prediction(input_data):
    FEATURES = [
        "daysOfTraining",
        "refToMaterials",
        "averageScore",
        "numOfIntermediateClasses"
    ]

    model_path = os.path.join(settings.MEDIA_ROOT, 'RandomForest_model.joblib')
    scaler_path = os.path.join(settings.MEDIA_ROOT, 'scaler.joblib')
    csv_path = os.path.join(
        settings.MEDIA_ROOT,
        'online_course_ml_ready_-1_0_1_NO_CLICKS.csv'
    )

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        return {"error": "Model not trained yet. Please train the model first."}

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    df = pd.read_csv(csv_path)
    avg_values = df[FEATURES].mean()

    new_data = pd.DataFrame([[input_data[f] for f in FEATURES]], columns=FEATURES)
    new_data_scaled = scaler.transform(new_data)

    pred = int(model.predict(new_data_scaled)[0])

    grade_map = {
        1: "Excellent",
        0: "Moderate",
        -1: "Needs Improvement"
    }

    grade = grade_map[pred]
    suggestions = []

    # -------- NEEDS IMPROVEMENT (-1) → 5 --------
    if pred == -1:
        if input_data["averageScore"] < avg_values["averageScore"]:
            suggestions.append("Improve assessment scores by revising concepts and practicing mock tests.")

        if input_data["daysOfTraining"] < avg_values["daysOfTraining"]:
            suggestions.append("Increase the number of study days per week for better retention.")

        if input_data["refToMaterials"] < avg_values["refToMaterials"]:
            suggestions.append("Refer to additional learning materials such as videos, PDFs, and notes.")

        if input_data["numOfIntermediateClasses"] < avg_values["numOfIntermediateClasses"]:
            suggestions.append("Attend more intermediate-level classes to strengthen fundamentals.")

        suggestions.append("Practice regularly instead of last-minute preparation.")

        suggestions = suggestions[:5]

    # -------- MODERATE (0) → 3 --------
    elif pred == 0:
        suggestions = [
            "Maintain consistent study habits to improve overall performance.",
            "Focus more on weak areas identified in assessments.",
            "Increase engagement with course materials and practice exercises."
        ]

    # -------- EXCELLENT (1) → 1 --------
    elif pred == 1:
        suggestions = [
            "Excellent performance! Maintain consistency and continue practicing to sustain your results."
        ]

    return {
        "grade": grade,
        "suggestions": suggestions
    }


# ============================
# PREDICTION VIEW
# ============================
def prediction_view(request):
    FEATURES = [
        "daysOfTraining",
        "refToMaterials",
        "averageScore",
        "numOfIntermediateClasses"
    ]

    context = {"features": FEATURES}

    if request.method == "POST":
        input_data = {f: float(request.POST.get(f)) for f in FEATURES}
        result = prediction(input_data)
        context.update(result)

    return render(request, "users/predict.html", context)
