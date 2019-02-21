from rasa_nlu.model import Interpreter

def test_model(model_directory, text):
  interpreter = Interpreter.load(model_directory)
  print(interpreter.parse(text))

if __name__ == '__main__':
  test_model('../models/nlu/default/recipes', u'give me the recipy for an applepie?')