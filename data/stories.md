## story1
* greet
  - utter_greet

## story2
* mood_happy
  - utter_happy

## story3
* mood_unhappy
  - utter_cheer_up

## story4
* ask_mood
  - utter_happy_mood

## story5
* goodbye
  - utter_goodbye

## story5
* ask_recipy{"cake": "carrot cake"}
  - slot{"cake": "carrot cake"}
  - action_recipy
  - slot{"cake": "carrot cake"}

## happy_path
* greet
  - utter_greet
* mood_happy
  - utter_happy
* goodbye
  - utter_goodbye

## sad_path
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
* goodbye
  - utter_goodbye


## Generated Story 7641940660552289253
* greet
    - utter_greet
* ask_mood
    - utter_happy_mood
* ask_recipy{"cake": "carrot cake"}
    - slot{"cake": "carrot cake"}
    - action_recipy
    - slot{"cake": "carrot cake"}
* goodbye
    - utter_goodbye


