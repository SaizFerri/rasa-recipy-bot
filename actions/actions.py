import requests
import json
import variables
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionRecipy(Action):
  def name(self):
    return "action_recipy"

  def run(self, dispatcher, tracker, domain):
    cake = tracker.get_slot('cake')
    response = ""
    url = 'https://www.food2fork.com/api/search?key={}&q={}&top=true'.format(variables.API_KEY, cake)
    
    request = requests.get(url).json()

    if (request['count'] > 10):
      response = "I found this 10 recipes:\n"
      for index, recipe in enumerate(request['recipes']):
        if (index < 10):
          response = response + " - {}: {}\n".format(recipe['title'], recipe['source_url'])
    elif (request['count'] == 0):
      response = "I didn't find any recipes"
    else:
      response = "I found this {} recipes:\n".format(request['count'])
      for index, recipe in enumerate(request['recipes']):
        response = response + " - {}: {}\n".format(recipe['title'], recipe['source_url'])


    dispatcher.utter_message(response)
    return [SlotSet('cake', cake)]