from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('House Prediction.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    Bedrooms = int(request.form.get('Bedrooms'))
    Bathrooms = int(request.form.get('Bathrooms'))
    Square_Foot_Living = int(request.form.get('Square Foot Living'))
    Square_Foot_Plot = int(request.form.get('Square Foot Plot'))
    Floors = int(request.form.get('Floors'))
    Waterfront = int(request.form.get('Waterfront'))
    View = int(request.form.get('View'))
    Condition = int(request.form.get('Condition'))
    Square_Foot_Above = int(request.form.get('Square Foot Above'))
    Square_Foot_Basement = int(request.form.get('Square Foot Basement'))
    Year_Built = int(request.form.get('Year Built'))
    Year_Renovation = int(request.form.get('Year Renovation'))
    City = int(request.form.get('City'))

    # prediction
    results = model.predict(np.array([Bedrooms,Bathrooms,Square_Foot_Living,Square_Foot_Plot,Floors,Waterfront,View,Condition,Square_Foot_Above,Square_Foot_Basement,Year_Built,Year_Renovation,City]).reshape(1,13))
    

    return render_template('House Prediction.html',result=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)