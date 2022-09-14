import keras
import numpy as np
import joblib
import nltk
import os
import nltk
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 
from keras.preprocessing.sequence import pad_sequences
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

__model = None
__tokenizer = None
__embedding = None
__decode_label = {0:"Fake", 1:"Real"}

def load_artifacts():
    """
      The function loads the saved artifacts as global variables..

       Parameters: 
           None

       Returns:
           None
    """
        
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    
    # load trained keras model
    global __model
    if __model is None:
        print("Loading Keras model...")
        
        if os.getcwd() == '/':
            file_path = '/FlaskServer/artifacts/keras_artifacts'
        else:
            file_path = os.getcwd() + '/artifacts/keras_artifacts'
            
        print("Reading...", file_path)
        __model = keras.models.load_model(file_path)
    
    # loading tokenizer
    global __tokenizer
    print("Loading tokenizer...")
    
    if __tokenizer is None:
        
        if os.getcwd() == '/':
            file_path = '/FlaskServer/artifacts/tokenizer.pickle'
        else:
            file_path = os.getcwd() + '/artifacts/tokenizer.pickle'
            
        print("Reading...", file_path)
        with open(file_path, 'rb') as handle:
            __tokenizer = pickle.load(handle)
    
    print("Loading Complete!!!")
    
# Preprocessing
def pre_process_news(news):
    """
      The function applies the WordNetLemmatization , PotterStamming, stop word removal, and punctuation removal on the string for preprocessing.

       Parameters: 
           news: string that needs to be pre-processed

       Returns:
           processed string
    """
    print("Starting preprocessing")
    
    lemm = WordNetLemmatizer()
    ps = PorterStemmer() 
    stop_words = set(stopwords.words('english'))
    news = news.lower()                             # convert to lowercase letters
    news = re.sub("[^0-9a-z]", ' ' , news)          # removes punctuations
    tokenized = news.split(" ")                     # tokenize string
    news = [ ps.stem(word) for word in tokenized if word not in stop_words] # apply stemming and drop stopwords
    news = " ".join(news)                           # join the tokens into a string
    news = lemm.lemmatize(news)                     # apply lemmatization
    
    print("processing complete!!!")
    return news

def tokenize_pad_text(text):
    """
      The function converts text tokens to a sequence of numbers and pads it for acceptable input length for the model.

       Parameters: 
          text: string that needs tokenized nad padded

       Returns:
           padded sequence
    """
    text_tokenized = __tokenizer.texts_to_sequences(texts = [text])
    MAX_PAD_SEQUENCE_LENGTH = 3000
    data = pad_sequences(sequences= text_tokenized, maxlen = MAX_PAD_SEQUENCE_LENGTH)
    print("returning")
    return data

def pred_acc(x_test):
    """
      The function tests the trained model using test data and prints performance metrics.

      Parameters:
        model: the trained model to use for prediction making
        x_test: test data

      Returns:
        predicted value
    """
    
    print("Starting classification...")
    y_preds = __model.predict(x_test)
    print(x_test)
    y_pred = np.round(y_preds)
    
    print("Classification Complete!!!")
    return y_pred

def predict_pipeline(news):
    """
      The function runs the prediction pipeline steps such as pre-processing, tokenizing, and predicting.

       Parameters: 
          news: string that needs to be clasified

       Returns:
           prediction (Fake or Real)
    """
    processed = pre_process_news(news)
    processed = tokenize_pad_text(processed)
    y_pred = pred_acc(processed)
    prediction = __decode_label[int(y_pred[0][0])]
    return prediction
    
    