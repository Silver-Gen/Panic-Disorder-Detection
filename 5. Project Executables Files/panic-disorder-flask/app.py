from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the features used for prediction
features = ['Lifestyle Factors', 'Current Stressors', 'Impact on Life', 'Symptoms', 'Severity', 'Personal History', 'Family History', 'Age', 'Medical History', 'Coping Mechanisms']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    input_data = []
    for feature in features:
        try:
            input_data.append(float(request.form[feature]))
        except KeyError:
            # Handle missing or invalid input
            return "Error: Missing or invalid input for feature: {}".format(feature)
        except ValueError:
            # Handle invalid data type
            return "Error: Invalid data type for feature: {}".format(feature)

    # Make prediction
    prediction = model.predict([input_data])

    # Process prediction and return result
    if prediction >= 0.5:
        result = "Panic Disorder"
    else:
        result = "No Panic Disorder"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

