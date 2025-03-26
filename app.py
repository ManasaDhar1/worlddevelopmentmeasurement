from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Hierarchical Clustering model
model = joblib.load("model.pkl")

# Dummy dataset (use the same dataset used for training)
X = np.array([[1], [2], [5], [6], [8], [10]])  # Example dataset

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        # Get user input
        user_input = float(request.form.get("user_input"))

        # Add user input to dataset
        X_new = np.vstack([X, [user_input]])

        # Recompute clusters
        clusters = model.fit_predict(X_new)

        # Get the cluster for the last (user-input) value
        cluster = clusters[-1]

        return render_template("result.html", user_input=user_input, cluster=cluster)

    except Exception as e:
        return render_template("result.html", error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
