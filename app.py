from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        birth_rate = float(request.form.get('birth_rate', 0))  # Default to 0 if missing
        business_tax_rate = float(request.form.get('business_tax_rate', 0))
        co2_emissions = float(request.form.get('co2_emissions', 0))
        days_start_business = float(request.form.get('days_start_business', 0))
        ease_business = float(request.form.get('ease_business', 0))
        energy_usage = float(request.form.get('energy_usage', 0))
        gdp = float(request.form.get('gdp', 0))
        health_exp_gdp = float(request.form.get('health_exp_gdp', 0))
        health_exp_capita = float(request.form.get('health_exp_capita', 0))
        life_expectancy_female = float(request.form.get('life_expectancy_female', 0))

        # Your clustering logic here
        cluster = "Cluster 1"  # Replace with actual model prediction

        return render_template('result.html', birth_rate=birth_rate, business_tax_rate=business_tax_rate, 
                               co2_emissions=co2_emissions, days_start_business=days_start_business,
                               ease_business=ease_business, energy_usage=energy_usage, gdp=gdp, 
                               health_exp_gdp=health_exp_gdp, health_exp_capita=health_exp_capita, 
                               life_expectancy_female=life_expectancy_female, cluster=cluster)
    except ValueError as e:
        return render_template('result.html', error=f"Invalid input: {e}")

if __name__ == '__main__':
    app.run(debug=True)
