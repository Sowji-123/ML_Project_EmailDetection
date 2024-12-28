from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model and TfidfVectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the message from the form
        message = request.form['message']
        
        # Transform the message using the vectorizer
        transformed_message = vectorizer.transform([message])
        
        # Make the prediction
        prediction = model.predict(transformed_message)
        
        # Interpret the result
        if prediction[0] == 1:
            result = "Ham"
        else:
            result = "Spam"
        
        return render_template('index.html', prediction=result, user_message=message)

if __name__ == "__main__":
    app.run(debug=True)
