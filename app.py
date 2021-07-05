from flask import Flask, render_template,url_for,request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask("car_model")  #Flask Object

#Loading ml model
model = pickle.load(open('car_price_model.pkl','rb'))

@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')

#creating object for standardScaler
standard_to = StandardScaler()

#HTTP POST request method

@app.route("/predict",methods=['POST'])

def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Year = 2021-Year
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']

        #Fuel_Type(feature) is categorised into petrol, diesel, cng, therefore we have done one-hot encoding on it while building model
        if(Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol =1
            Fuel_Type_Diesel=0
        elif(Fuel_Type_Petrol =='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0

        #seller type is also categorical data
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if(Seller_Type_Individual =='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        
        # Transmission manual is also categorical data
        Transmission_Mannual = request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual =1
        else:
            Transmission_Mannual=0
        
        prediction = model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output = round(prediction[0],2)

        #condition of invalid values
        if output<0:
            return render_template('index.html',prediction_text='sorry you cannot sell this car')
        else:
            return render_template('index.html',prediction_text='you can sell this car at {} lakh' .format(output))

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

