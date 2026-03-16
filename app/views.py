# Libraries
from django.shortcuts import render,redirect
from django.http import HttpResponse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import PassiveAggressiveClassifier
import os

import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from .models import User




################ Home #################
def home(request):
	return render(request,'home1.html')
def login(request):
	return render(request,'loginform.html')
def loginCheck(request):
	if request.method=="POST":
		print('printtttttttttttttttttttttttttttttttt')
		username= request.POST.get('username')
		password= request.POST.get('email')
		try:
			user_object = User.objects.get(firstname=username,password=password)
			print(user_object)
		except:
			#user_object = None
			print('hello')
		if user_object is not None:
			print('hiiiiiiii')
			request.session['useremail'] = user_object.email
			return redirect('home')
			print('hiiiiiiii')
	return render(request,'home.html')	
def logout(request):
	return render(request,'index.html')	
def reg(request):
	return render(request,'register.html')

######## SVM ######
def save(request):
	if request.method == 'POST':
		print('printtttttttttttttttttttttttttttttttt')
		print('checkkkkkkkkkkkkkkkkk')
		username= request.POST.get('username')
		password= request.POST.get('password')
		address= request.POST.get('address')
		email= request.POST.get('email')
		age= request.POST.get('age')
		gender= request.POST.get('gender')
		phone= request.POST.get('phone')
		user=User()
		user.firstname= request.POST.get('username')
		user.password= request.POST.get('password')
		user.address= request.POST.get('address')
		user.email= request.POST.get('email')
		user.age= request.POST.get('age')
		user.gender= request.POST.get('gender')
		user.phone= request.POST.get('phone')
		user.save()		
		return render(request,'loginform.html')
	return render(request,'loginform.html')	

######## SVM ######
def nvb(request):
	return render(request,'pacweb1.html')


from django.shortcuts import render
from django.conf import settings
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def pac(request):
    if request.method == 'POST':

        # Get form values
        headline1 = int(request.POST.get('headline1'))
        headline2 = int(request.POST.get('headline2'))
        headline3 = int(request.POST.get('headline3'))
        headline4 = int(request.POST.get('headline4'))
        headline5 = int(request.POST.get('headline5'))
        headline6 = float(request.POST.get('headline6'))
        headline7 = float(request.POST.get('headline7'))
        headline8 = int(request.POST.get('headline8'))

        # Load dataset
        file_path = os.path.join(settings.BASE_DIR, 'diabetes.csv')
        df = pd.read_csv(file_path)
        df = df.fillna(0)

        # Features and target
        X = df[['Pregnancies','Glucose','BloodPressure','SkinThickness',
                'Insulin','BMI','DiabetesPedigreeFunction','Age']].values
        y = df['Outcome'].values  # make 1D

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Model
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=4,
            random_state=42
        )

        model.fit(X_train, y_train)

        # Test input
        atest = [[headline1, headline2, headline3, headline4,
                  headline5, headline6, headline7, headline8]]

        prediction = model.predict(atest)

        # Convert prediction to readable output
        if prediction[0] == 0:
            result = "Not Diabetic"
        else:
            result = "Diabetic"

        accuracy = model.score(X_test, y_test)

        context = {
            'predictedvalue': result,
            'accuracy': round(accuracy * 100, 2)
        }

        return render(request, 'result.html', context)

    return render(request, 'form.html')			
def svm(request):	
	return render(request,'cvd.html')		
def dec(request):
	if request.method == 'POST':
		if request.method == 'POST':
			headline1= request.POST.get('headline1')
			headline2= request.POST.get('headline2')
			headline3= request.POST.get('headline3')
			headline4= request.POST.get('headline4')
			headline5= request.POST.get('headline5')
			headline6= request.POST.get('headline6')
			headline7= request.POST.get('headline7')
			headline8= request.POST.get('headline8')
			headline9= request.POST.get('headline9')
			headline10= request.POST.get('headline10')
			headline11= request.POST.get('headline11')
			headline12= request.POST.get('headline12')
			headline13= request.POST.get('headline13')

			print(headline1)
			
			
			headline1= int(headline1)
			headline2 = int(headline2)
			headline3 = int(headline3)
			headline4 = int(headline4)	
			headline5 = int(headline5)	
			headline6 = int(headline6)	
			headline7 = int(headline7)	
			headline8 = int(headline8)	
			headline9 = int(headline9)	
			headline10 = float(headline10)	
			headline11 = int(headline11)	
			headline12 = int(headline12)	
			headline13 = int(headline13)	

			from django.shortcuts import render
			from django.http import HttpResponse
			import pandas as pd
			import numpy as np
			import matplotlib.pyplot as plt
			from sklearn.model_selection import train_test_split
			from sklearn.feature_extraction.text import TfidfVectorizer
			import itertools
			from sklearn import metrics
			import os
			import seaborn as sns
			from sklearn.model_selection import train_test_split
			from sklearn.metrics import confusion_matrix
			from django.conf import settings
			file_path = os.path.join(settings.BASE_DIR, 'cvd.csv')
			df = pd.read_csv(file_path)
			df1=df.fillna(0)

			dfle = df1.copy()
			dfle
			dfle
			print(dfle)
			X = dfle[['Age','Sex','Chestpaintype','BP','Cholesterol','FBSover120','EKGresults','MaxHR','Exerciseangina','STdepression','SlopeofST','Numberofvesselsfluro','Thallium']].values
			X
			y = dfle[['HeartDisease']]		
			y

			#atest=[[0,0,0,0,0,5849,0,320,360,1,0]]
			#atest1=[[0,0,0,0,0,12500,3000,320,360,1,1]]
			#train_test separation
			X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
			atest=[[headline1,headline2,headline3,headline4,headline5,headline6,headline7,headline8,headline9,headline10,headline11,headline12,headline13]]
			#train_test separation
			X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
			linear_clf = RandomForestClassifier(n_estimators = 100, max_depth =4, random_state=42, min_samples_split = 5, oob_score = True, n_jobs = -1, max_features = "auto",criterion = 'entropy', max_leaf_nodes = 30,class_weight='balanced_subsample',min_samples_leaf = 10)
			linear_clf.fit(X_train, y_train)
			pred = linear_clf.predict(X_test)
			print('=====================================================================')
			pred1 = linear_clf.predict(atest)
			#pred2 = linear_clf.predict(atest1)
			print(pred1)
			result=''
			print(linear_clf.score(X_train, y_train))
			d={'predictedvalue':pred1,'accuracy':linear_clf.score(X_train, y_train)}	
	return render(request,'result.html',d)
def randomf(request):
    from django.shortcuts import render
    from django.http import HttpResponse
    import pandas as pd
    import numpy as np
    import os
    from django.conf import settings
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn import metrics

    # Load dataset
    file_path = os.path.join(settings.BASE_DIR, 'kidney_disease.csv')
    df = pd.read_csv(file_path)

    # Handle missing values
    df1 = df.fillna(0)

    # Copy dataframe
    dfle = df1.copy()
    print(dfle)

    # Features and target
    X = dfle[['id', 'age', 'bp', 'sg', 'al', 'su',
              'bgr', 'bu', 'sc', 'sod', 'pot']].values

    y = dfle['classification'].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Prediction
    pred = model.predict(X_test)

    print('=====================================================')
    print(pred)

    # Accuracy
    accuracy_score = metrics.accuracy_score(y_test, pred)
    print(accuracy_score)

    data = {'accuracy': accuracy_score}

    return render(request, 'acc1.html', data)
def mnb(request):
    return render(request, 'acc1.html')
def graph(request):
    from django.conf import settings
    import os
    import pandas as pd
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split

    # Load dataset
    file_path = os.path.join(settings.BASE_DIR, 'Hypertension.csv')
    df = pd.read_csv(file_path)

    # Features and target
    X = df.iloc[:, 0:12]
    y = df.iloc[:, 12]

    # Scale data
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=1
    )

    # Create ANN model
    model = Sequential()
    model.add(Dense(20, input_shape=(12,), activation='relu'))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(
        loss='binary_crossentropy',
        optimizer='sgd',
        metrics=['accuracy']
    )

    # Train
    model.fit(X_train, y_train, epochs=3, batch_size=10, verbose=0)

    # Evaluate
    val_loss, val_acc = model.evaluate(X_test, y_test, verbose=0)

    context = {
        'accuracy': round(val_acc * 100, 2)
    }

    return render(request, 'acc1.html', context)
def accuracy(request):
    from django.shortcuts import render
    from django.http import HttpResponse
    import pandas as pd
    import numpy as np
    import os
    from django.conf import settings
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import metrics

    # Load dataset
    file_path = os.path.join(settings.BASE_DIR, 'stroke.csv')
    df = pd.read_csv(file_path)

    # Handle missing values
    df1 = df.fillna(0)

    # Encoding categorical data
    dfle = df1.copy()
    le = LabelEncoder()

    dfle['gender'] = le.fit_transform(dfle['gender'])
    dfle['ever_married'] = le.fit_transform(dfle['ever_married'])
    dfle['work_type'] = le.fit_transform(dfle['work_type'])
    dfle['Residence_type'] = le.fit_transform(dfle['Residence_type'])
    dfle['smoking_status'] = le.fit_transform(dfle['smoking_status'])

    # Features and target
    X = dfle[['id', 'gender', 'age', 'hypertension', 'heart_disease',
              'ever_married', 'work_type', 'Residence_type',
              'avg_glucose_level', 'bmi', 'smoking_status']].values

    y = dfle['stroke'].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = AdaBoostClassifier(
        DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=8,
            min_samples_leaf=10
        ),
        n_estimators=500,
        random_state=3,
        learning_rate=0.001
    )

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    pred = model.predict(X_test)

    # Accuracy
    accuracy_score = metrics.accuracy_score(y_test, pred)

    data = {'accuracy': accuracy_score}

    return render(request, 'acc1.html', data)
def accuracy1(request):
	return render(request,'index.html')	
			