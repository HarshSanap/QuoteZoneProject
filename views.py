from django.shortcuts import render
import random

quotes_list = [
    "Push yourself, because no one else is going to do it for you.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
]

def home(request):
    quote = random.choice(quotes_list)
    return render(request, 'quotes/index.html', {'quote': quote})
