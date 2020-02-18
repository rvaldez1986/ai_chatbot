# ai_chatbot

Python Chatbot connected with [Chatra’s API](https://chatra.io/help/api/).

![Chatbot Flowchart](https://user-images.githubusercontent.com/19597283/69583327-a37caa00-0fa8-11ea-8f59-c7ce9a85b7d7.png)

### About

Deployed on [Actuaria](https://actuaria.com.ec/). Interacts with Chatra.io using a web server, a REST API and webhooks. Uses a flow chart for handling the user - bot interaction. Decisions on most nodes are based on a probabilistic model using a Neural Network. Connects with Azure LUIS for some nodes.

This program contains:

* Chatra's Webhook at [pro_app](pro_app.py).
* Chatbot flowchart handling at [text_processer](text_processer.py).
* Natural language processing, API connections, etc. at [nlp_functions](nlp_functions.py).
* Dictionary of replys at [textos](textos.py).
* Dictionary of URLs at [urls](urls.py).
* Data for fitting machine learning models at [preguntas](/Data/preguntas.csv). 







