# Chatbot in python 

### DATA SOURCE : 
The provided dataset consists of multiple short conversations between two participants, primarily focusing on casual and friendly exchanges. The conversations cover topics like greetings, well-being, attending school at PCC (a specific institution), and some small talk about the weather. Each conversation is structured as a back-and-forth dialogue between the participants, featuring natural language and informal communication
### Dataset Link :( https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot)
In dataset we have provided is an example of a conversational dataset. Conversational datasets are typically used to train chatbot models. The dataset contains a dialogue between two people, where each person takes a turn speaking. The dataset also includes the context of the conversation, which is important for training chatbot models to generate natural and informative responses.

### Repository Contents
The repository contains the following files and directories:

1.static/: This directory contains static assets such as CSS files, images, and JavaScript files that can be used in the web application.

2.templates/: This directory holds HTML templates used to render web pages in your Flask application.

3.Application.py: The main entry point of the Flask application. Running this file will start the application.

4.dataclass.py: This file likely contains custom data classes or structures used in your application.

5.dialogs.txt: This is a dataset file that the application might use for specific purposes.

6.model.py: This file is used to define and load a machine learning model.

7.model_state.pt: This file contains the pre-trained state of the machine learning model.

## Prerequisites
Before you can run the Flask application, you need to ensure that you have the required Python packages installed. 
### You can use the following command to install them:
     pip install flask transformers pandas torch
1.This command will install the necessary packages: Flask for web application development, transformers for working with transformer-based models, pandas for data manipulation, and torch for PyTorch, which is often used for machine learning tasks.
2.Running the Application
To run the Flask application, follow these steps:

Navigate to the root directory of the application in your terminal.

Make sure you have the required packages installed, as mentioned in the "Prerequisites" section.

### Run the application by executing the following command:
       python Application.py
### /or:
       python3 Application.py
  
1.After running the command, you should see output indicating that the Flask application is running.

2.It will typically provide a URL where you can access the application, often something like http://127.0.0.1:5000/.

3.train the model we need cuda for training the model.

4.we can 

Open a web browser and navigate to the provided URL to interact with the application.

### Phase1 document: https://sakthivelgokul2004.github.io/Chatbot-in-python/AI_Phase1.pdf

### Phase2 document: https://sakthivelgokul2004.github.io/Chatbot-in-python/AI_PHASE2.pdf

### Phase3 document: https://sakthivelgokul2004.github.io/Chatbot-in-python/AI_PHASE3.pdf

### Phase4 document: https://sakthivelgokul2004.github.io/Chatbot-in-python/AI_Phase4.pdf

### Phase5 document: https://sakthivelgokul2004.github.io/Chatbot-in-python/AI_Phase5.pdf
