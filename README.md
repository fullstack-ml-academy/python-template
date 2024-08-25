# Auto MPG Predictor

## Part 1: Model Training and Testing

This project is a machine learning application that predicts the miles per gallon (MPG) for automobiles based on various features. It's developed as a learning exercise and currently consists of two main parts: model training and model testing.

### Features

- Data loading and preprocessing
- Model training using Linear Regression
- Model serialization and deserialization
- Comprehensive unit tests for the prediction functionality

### How to Run

1. Ensure you have Python 3.x installed along with the required libraries (pandas, scikit-learn).
2. To train the model:
   ```
   python src/train.py
   ```
3. To run the tests:
   ```
   python src/test_predict.py
   ```

## Part 2: Flask API Development

This project is a continuation of the Auto MPG Predictor, focusing on creating a RESTful Flask API to serve predictions and other data. This part of the project includes the implementation of several endpoints to interact with the model and retrieve relevant data.

### Features

- **RESTful API Endpoints**:

  - `GET /`: Returns a JSON response with a simple greeting.
  - `GET /hello_world`: Returns a simple HTML page with "Hello, World!".
  - `GET /training_data`: Returns an array of training data in JSON format.

- **Frameworks and Tools**:
  - Flask: A lightweight WSGI web application framework.
  - Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS), making it easier to build a front-end that interacts with the API.

### How to Run

1. **Install Dependencies**:
   Make sure you have Python 3.x installed. Install the required packages using pip:

   ```bash
   pip install flask flask-cors
   ```

2. **Run the Flask Application**:

   ```bash
   python wsgi.py
   ```

   The application will start on `http://127.0.0.1:5000/`.

3. **Test the Endpoints**:
   - Visit `http://127.0.0.1:5000/` to see the JSON response: `{"hello": "world"}`.
   - Visit `http://127.0.0.1:5000/hello_world` to see the HTML response: `<p>Hello, World!</p>`.
   - Visit `http://127.0.0.1:5000/training_data` to see the array of training data in JSON format.

### Next Steps

The next steps in the project include:

1. **Prediction Endpoint**: Implementing a new endpoint to handle predictions based on user input.
2. **Model Integration**: Integrating the trained machine learning model into the API to provide real-time predictions.
3. **Frontend Development**: Developing a web interface to interact with the API, allowing users to make predictions directly from the browser.

### Contributing

Suggestions and improvements are always welcome. If you have any ideas to enhance this project, feel free to open an issue or submit a pull request.

### License

[MIT License](https://opensource.org/licenses/MIT)
