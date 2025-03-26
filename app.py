from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("model.pkl")

# Use the same dataset from training
X_train = np.array([[1], [2], [3], [5], [6], [8], [9], [10], [15], [20], [25]])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        user_input = float(request.form.get("user_input"))

        # Find the closest cluster to user input
        distances = np.abs(X_train - user_input)
        closest_point_index = np.argmin(distances)
        cluster = model.fit_predict(X_train)[closest_point_index]  # Assign cluster based on closest point

        return render_template("result.html", user_input=user_input, cluster=cluster)

    except Exception as e:
        return render_template("result.html", error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
