#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request
import joblib  # Load ML model
import numpy as np  # Data processing

app = Flask(__name__)

# Load pre-trained ML model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        # Get user input from form
        user_input = float(request.form.get("user_input"))

        # Make prediction
        prediction = model.predict(np.array([[user_input]]))[0]

        return render_template("result.html", user_input=user_input, prediction=prediction)
    
    except Exception as e:
        return render_template("result.html", error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


# In[ ]:




