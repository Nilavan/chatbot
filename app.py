from flask import Flask

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Chloe',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I\'m sorry, I don\'t understand. I\'m still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    "./training_data/finance.yml"
)

app = Flask(__name__)


@app.route("/get/<msg>")
def bot_respose(msg):
    return str(chatbot.get_response(msg))


if __name__ == "__main__":
    app.run()
