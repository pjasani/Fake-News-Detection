from flask import Flask, request, jsonify
import utils
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def classify():
    """
    The function responsds to GET and POST requests to the server.

    Parameters: 
       For GET request -> None
       For POST request -> news: string that needs to be pre-processed

    Returns:
       For GET request it returns 'Successful connection to server.'
       For POST request it makes the prediction and returns output (Fake or Real)
    """
    
    if request.method == 'POST':
        response = request.form.get('news')
        prediction = utils.predict_pipeline(response)
        return { 'prediction': prediction }
    return {'label': 'Successful connection to server.'}

if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # set the flag for tensorflow
    utils.load_artifacts()
    app.run(port=5001)
