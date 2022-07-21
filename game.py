class Menu(object):
    questions = [
        {'question': 'HTML é uma linguagem de...?',
            'answer': 'marcação de hipertexto'},
        {'question': 'Que linguagem você deve estudar para programar com React?',
         'answer': 'javascript'},
        {'question': 'Que linguagem usa ".py" como extensão de arquivo?',
            'answer': 'python'},
        {'question': 'Qual o paradigma da linguagem Java?',
         'answer': 'orientação a objetos'},
        {'question': 'Com que protocolo fazemos a conexão do front-end com back-end?',
         'answer': 'protocolo http'}
    ]
    rightAnswers, wrongAnswers = 0, 0

    def __init__(self, quizTheme):
        self.quizTheme = quizTheme

    def start(self):
        self.quiz(self.quizTheme)

    @classmethod
    def quiz(cls, theme):
        if(theme != 'programação'):
            print('Tema não existente!')
            return
        print(f'Tema escolhido {theme}\n')
        for question in cls.questions:
            userAnswer = input(question['question'] + ' ').lower()
            if userAnswer != question['answer']:
                cls.wrongAnswers += 1
            else:
                cls.rightAnswers += 1
        print(f'Questões acertadas: {cls.rightAnswers}')
        print(f'Questões erradas: {cls.wrongAnswers}')

        tryAgain = input('Jogar de novo?(s/n): ')
        cls.rightAnswers, cls.wrongAnswers = 0

        if tryAgain == "n":
            quit()


while True:
    theme = input('''
    Escolha um tema:
      - Programação 
  ''').lower()
    game = Menu(theme)
    game.start()
