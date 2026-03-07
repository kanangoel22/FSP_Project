from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import json
import os

# Load quotes from the JSON file once when the action server starts
QUOTES_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "quotes.json")

def load_quotes():
    """Load quotes from quotes.json file."""
    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {QUOTES_FILE} not found. Using fallback quotes.")
        return {}
    except json.JSONDecodeError:
        print(f"Warning: {QUOTES_FILE} is not valid JSON. Using fallback quotes.")
        return {}

ALL_QUOTES = load_quotes()


class ActionMotivationQuote(Action):

    def name(self) -> Text:
        return "action_motivation_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = ALL_QUOTES.get("motivation", [
            "Believe you can and you're halfway there.",
            "Push yourself, because no one else will do it for you.",
            "Dream it. Wish it. Do it."
        ])
        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionInspirationQuote(Action):

    def name(self) -> Text:
        return "action_inspiration_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = ALL_QUOTES.get("inspiration", [
            "The best way to predict the future is to create it.",
            "Do what you can, with what you have, where you are.",
            "Everything you've ever wanted is on the other side of fear."
        ])
        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionFunnyQuote(Action):

    def name(self) -> Text:
        return "action_funny_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = ALL_QUOTES.get("funny", [
            "I'm not lazy, I'm on energy saving mode.",
            "I put the 'pro' in procrastinate.",
            "Life is short. Smile while you still have teeth."
        ])
        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionLoveQuote(Action):

    def name(self) -> Text:
        return "action_love_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = ALL_QUOTES.get("love", [
            "Love all, trust a few, do wrong to none.",
            "Where there is love there is life.",
            "The best thing to hold onto in life is each other."
        ])
        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionSuccessQuote(Action):

    def name(self) -> Text:
        return "action_success_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = ALL_QUOTES.get("success", [
            "Success usually comes to those who are too busy to be looking for it.",
            "Opportunities don't happen. You create them.",
            "The secret of success is to do the common thing uncommonly well."
        ])
        dispatcher.utter_message(text=random.choice(quotes))
        return []