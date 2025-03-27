@app.route('/result', methods=['POST'])
def result():
    try:
        # Extract form data
        form_data = {key: request.form.get(key, "").strip() for key in request.form.keys()}

        # Convert to float, validate input
        data = {}
        for key, value in form_data.items():
            if not value.replace(".", "", 1).isdigit():  # Allow decimals
                return render_template('result.html', error=f"Invalid input for {key}: {value}")
            data[key] = float(value)

        # Dummy clustering logic (replace with actual model)
        cluster = "Cluster 1"  # Replace with model.predict(data)

        return render_template('result.html', **data, cluster=cluster)
    except Exception as e:
        return render_template('result.html', error=f"Unexpected error: {e}")
