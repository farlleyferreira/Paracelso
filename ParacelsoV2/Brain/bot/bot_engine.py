# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance


class bot_brain_engine:
    def __init__(self):

        self.bot = ChatBot(
                    "Paracelso",
                    statement_comparison_function=levenshtein_distance,
                    storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    logic_adapters=[
                                {
                                        "import_path": "chatterbot.logic.BestMatch",
                                        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                                        "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"
                                },
                                {
                                        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                        'threshold': 0.35,
                                        'default_response': 'Não consegui te entender'
                                },
                                {
                                        'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                                        'input_text': 'Olá!',
                                        'output_text': 'Olá, meu nome é paracelso, em que posso ajudar hoje ?'
                                }],
                    output_adapter="chatterbot.output.TerminalAdapter",
                    database="databases/database.db",
                 )

    def Train(self):
        self.bot.set_trainer(ListTrainer)
        self.bot.train()

    def Conversation(self, text):
        try:
            response = self.bot.get_response(text)
            return response
        except (KeyboardInterrupt, EOFError, SystemExit):
            return "erro ao processar sua solicitação"
