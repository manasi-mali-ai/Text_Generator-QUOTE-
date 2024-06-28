from flask import Flask, render_template, request

app = Flask(__name__)

# Load your pre-trained LSTM model here
# model = ...

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences

model = tf.keras.models.load_model("model/best_model.h5")

tokenizer_json_path = "model/tokenizer.json"
with open(tokenizer_json_path, 'r') as json_file:
    loaded_tokenizer_json = json_file.read()
    loaded_tokenizer = tokenizer_from_json(loaded_tokenizer_json)

def generator(seed, model, length = 15):
  for i in range(length):
    # tokenize
    token_text = loaded_tokenizer.texts_to_sequences([seed])[0]
    # padding
    padded_token_text = pad_sequences([token_text], maxlen=100, padding='pre')
    # predict
    pos = np.argmax(model.predict(padded_token_text, verbose=False))

    for word,index in loaded_tokenizer.word_index.items():
      if index == pos:
        seed = seed + " " + word
  return seed

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_quote = ""
    if request.method == 'POST':
        start_sentence = request.form['start_sentence']
        quote_length = int(request.form['quote_length'])
        # generated_quote = start_sentence + " " + str(quote_length)

        generated_quote = generator(start_sentence, model, quote_length)
    return render_template('index.html', generated_quote=generated_quote)

if __name__ == '__main__':
    app.run(debug=True)