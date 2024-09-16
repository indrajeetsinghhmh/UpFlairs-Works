from flask import Flask, render_template, request
import joblib, sqlite3

model = joblib.load("./oldbike/models/linear_model.lb")

app = Flask(__name__) 


@app.route('/') 
def home(): 
    return render_template('home.html') 


@app.route("/predict", methods=['GET','POST']) 
def predict():
    if request.method == "POST":
        brand_name = int(request.form["brand_name"]) 
        Kms_Driven = int(request.form["Kms_Driven"]) 
        owner = int(request.form["owner"]) 
        age = int(request.form["age"]) 
        power = int(request.form["power"]) 
        
        brand_dict = {'Bajaj': 1,'Royal Enfield': 2,'Hero': 3,'Honda': 4,'Yamaha': 5,'TVS': 6,
                        'KTM': 7,'Suzuki': 8,'Harley-Davidson': 9,'Kawasaki': 10,'Hyosung': 11,
                        'Mahindra': 12,'Benelli': 13,'Triumph': 14,'Ducati': 15,'BMW': 16}
        
        brand_dict2 = {value:key for key, value in brand_dict.items()}
        print(brand_dict2)

        unseen_data = [[Kms_Driven, owner, age, power, brand_name]] #user input data
        prediction = model.predict(unseen_data)[0][0]

        # inserting data into database 
        
        query_to_insert = '''
        Insert into BikeDetails values(?,?,?,?,?,?)
        '''

        conn = sqlite3.connect('bikedata.db')
        cur = conn.cursor()
        data = (owner, brand_dict2[brand_name], Kms_Driven, power, age, int(round(prediction,2)))
        cur.execute(query_to_insert, data)
        conn.commit()
        print("your record is dumped into database")
        cur.close()
        conn.close()



        return render_template("home.html", prediction_text = str(round(prediction, 2)))

if __name__ == "__main__": 
    app.run(debug=True)