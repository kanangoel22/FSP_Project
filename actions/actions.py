from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random


class ActionMotivationQuote(Action):

    def name(self) -> Text:
        return "action_motivation_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = [
            "Believe you can and you're halfway there.",
            "Push yourself, because no one else will do it for you.",
            "Dream it. Wish it. Do it.",
            "Success doesn't just find you. You have to go out and get it.",
            "The harder you work for something, the greater you'll feel when you achieve it."
        ]

        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionInspirationQuote(Action):

    def name(self) -> Text:
        return "action_inspiration_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = [
            "The best way to predict the future is to create it.",
            "Do what you can, with what you have, where you are.",
            "Start where you are. Use what you have. Do what you can.",
            "Everything you’ve ever wanted is on the other side of fear.",
            "Your limitation—it’s only your imagination."
        ]

        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionFunnyQuote(Action):

    def name(self) -> Text:
        return "action_funny_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = [
            "I'm not lazy, I'm on energy saving mode.",
            "I put the 'pro' in procrastinate.",
            "Why work hard when you can nap harder?",
            "I’m on a seafood diet. I see food and I eat it.",
            "Life is short. Smile while you still have teeth."
        ]

        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionLoveQuote(Action):

    def name(self) -> Text:
        return "action_love_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = [
            "Love all, trust a few, do wrong to none.",
            "Where there is love there is life.",
            "Love is composed of a single soul inhabiting two bodies.",
            "You call it madness, but I call it love.",
            "The best thing to hold onto in life is each other."
        ]

        dispatcher.utter_message(text=random.choice(quotes))
        return []


class ActionSuccessQuote(Action):

    def name(self) -> Text:
        return "action_success_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quotes = [
            "Success usually comes to those who are too busy to be looking for it.",
            "Don't be afraid to give up the good to go for the great.",
            "Success is not in what you have, but who you are.",
            "The secret of success is to do the common thing uncommonly well.",
            "Opportunities don't happen. You create them."
        ]

        dispatcher.utter_message(text=random.choice(quotes))
        return []