from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Chloe',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
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

#trainer_corpus = ChatterBotCorpusTrainer(chatbot)
# trainer_corpus.train("./training_data/finance.txt")

training_fin = open('training_data/finance.txt').read().splitlines()
training_greet = open('training_data/greet.txt').read().splitlines()
training_bye = open('training_data/bye.txt').read().splitlines()

training_data = training_greet + training_fin + training_bye
trainer = ListTrainer(chatbot)
trainer.train(training_data)

app = Flask(__name__)


@app.route("/get/<msg>")
def bot_respose(msg):
    return str(chatbot.get_response(msg))


if __name__ == "__main__":
    app.run()
