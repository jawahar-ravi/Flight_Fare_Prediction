# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:11:29 2022

@author: jawah
"""
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')
 
@app.route('/predict', methods= ["GET", "POST"])
@cross_origin()
def predict():
    
    if request.method == 'POST':
        
        #Source --> starting location
        Source = request.form['Source']
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
        
        
        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0
     
        
        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0
  
            
        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
            
            
        # Destination 
        Destination = request.form['Destination']
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        
        
        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
     
        
        elif (Destination == 'New Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
         
        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0


        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
          
            
        # Departure Date
        Departure_date = request.form['Dep_Time']
        Journey_day = int(pd.to_datetime(Departure_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(Departure_date, format= "%Y-%m-%dT%H:%M").month)
        
        #Departure time
        departure_hour = int(pd.to_datetime(Departure_date, format="%Y-%m-%dT%H:%M").hour)
        departure_minute = int(pd.to_datetime(Departure_date, format="%Y-%m-%dT%H:%M").minute)
        
        
        #Arrival time 
        date_arr = request.form['Arrival_Time']
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)        
        
        # Duration
        Duration_hrs = abs(Arrival_hour - departure_hour)
        Duration_mins = abs(Arrival_minute - departure_minute)
        
        #Total stops
        Total_stops = request.form['stops']
        
        
        # Airline
        Airline = request.form['airline']
        if(Airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (Airline=='IndiGo'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (Airline=='Air India'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (Airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
                  
        elif (Airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
            
        elif (Airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            

        elif (Airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (Airline=='Multiple carriers Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            

        elif (Airline=='Jet Airways Business'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (Airline=='Vistara Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Trujet = 0 
            
            
        elif (Airline=='Trujet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1
            
            ##['Total_Stops', 'Journey_day', 'Journey_month', 'departure_hour',
    ##   'departure_minute', 'Arrival_hour', 'Arrival_minute', 'Duration_hrs',
     #  'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
      # 'Airline_Jet Airways', 'Airline_Jet Airways Business',
      # 'Airline_Multiple carriers',
      # 'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
      # 'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
      # 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
       #'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       #'Destination_Kolkata', 'Destination_New Delhi']
       
        prediction = model.predict([[ Source_Delhi,
                                     Source_Kolkata,
                                     Source_Mumbai,
                                     Source_Chennai,
                                     Destination_Cochin,
                                     Destination_Delhi,
                                     Destination_New_Delhi,
                                     Destination_Hyderabad,
                                     Destination_Kolkata,
                                     Airline_Jet_Airways,
                                     Airline_IndiGo,
                                     Airline_Air_India,
                                     Airline_Multiple_carriers,
                                     Airline_SpiceJet,
                                     Airline_Vistara,
                                     Airline_GoAir,
                                     Airline_Multiple_carriers_Premium_economy,
                                     Airline_Jet_Airways_Business,
                                     Airline_Vistara_Premium_economy,
                                     Airline_Trujet,
                                     Journey_day,
                                     Journey_month,
                                     departure_hour,
                                     departure_minute,
                                     Arrival_hour,
                                     Arrival_minute,
                                     Duration_hrs,
                                     Duration_mins,
                                     Total_stops
                                     ]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Your Flight ticket price is Rs. {}".format(output))
        
        
        
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)