
### Simple Flask Application

import tensorflow_datasets as tfds
import tensorflow as tf
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
padding_size = 1000

### Load Models at first iteself. 
model = tf.keras.models.load_model('sentiment_analysis.hdf5')
## All the words which we trained our model on 
text_encoder = tfds.features.text.TokenTextEncoder.load_from_file("sa_encoder.vocab")

print('Model and Vocabalory loaded.......')


def pad_to_size(vec, size):
    zeros = [0] * (size - len(vec))
    vec.extend(zeros)
    return vec


def predict_fn(predict_text, pad_size):
    encoded_text = text_encoder.encode(predict_text)
    encoded_text = pad_to_size(encoded_text, pad_size)
    encoded_text = tf.cast(encoded_text, tf.int64)
    predictions = model.predict(tf.expand_dims(encoded_text, 0))

    return (predictions.tolist())


@app.route('/seclassifier', methods=['POST'])
def predict_sentiment():
    text = request.get_json()['text']
    print(text)
    predictions = predict_fn(text, padding_size)
    sentiment = 'positive' if float(''.join(map(str,predictions[0]))) > 0 else 'Negative'
    return jsonify({'predictions ':predictions, 'sentiment ': sentiment})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
