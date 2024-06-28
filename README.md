# LSTM Quote Generator

## Demo [link](https://quote-generator-lstm-kunal.onrender.com)

## Overview

This project implements a Long Short-Term Memory (LSTM) model using TensorFlow's Keras API. The primary functionality of the model is to predict the next word in a given input word or sentence. By utilizing a loop, users can generate quotes by providing a starting word or sentence and specifying the desired length of the generated quote.

The key concepts covered in this project include:

- Text preprocessing: Preparing and cleaning the text data for training.
- Tokenization: Converting words into numerical tokens for model input.
- Padding: Ensuring uniform input length by padding sequences.
- Embedding: Mapping words to vectors for input to the LSTM model.
- LSTM: Training the model using Long Short-Term Memory architecture for sequence prediction.

The model has been trained on a dataset comprising 5000 quotes, enabling it to generate quotes that are related to the input data.

## Google Colab Link for Model Training

To explore and experiment with the model training code, you can use the provided [Google Colab notebook](https://colab.research.google.com/drive/1W9kgorcb39qiOHYCOiIIA7z-tav6aqbN). Simply follow the instructions and run the code cells in the notebook to understand the training process and make modifications as needed.

## Requirements

To run this project, you will need the following:

- Python (version 3.10)
- TensorFlow (version 2.15.0)
- Flask 
- Docker (if deploying with Docker)

## Dataset Information

The LSTM model has been trained on a diverse dataset of 5000 quotes. The dataset source, size, and any preprocessing steps applied are detailed in the `dataset/README.md` file.

## Model Architecture

The LSTM model in this project follows a specific architecture. The layers, units, and any custom configurations are described in the `model_architecture.md` file.

## Usage

To generate a quote, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/deep-learning-kunal/quote_generator_lstm.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

5. Enter a starting word or sentence and specify the desired length for the generated quote.

6. Click the "Generate Quote" button to receive your generated quote.

## Deployment with Docker
To deploy the application using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t lstm-quote-generator .
3. Run the Docker container:
   ```bash
   docker run -p 5000:5000 lstm-quote-generator
4. Open your web browser and navigate to http://localhost:5000.

5. Follow steps 5 and 6 from the Usage section to generate quotes.

## Acknowledgments
This project was developed by Kunal Thakare. If you find it helpful or have any suggestions for improvement, feel free to contribute or reach out.
