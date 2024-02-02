from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

essay_on_global_warming = "Global warming, driven by human activities, poses a critical threat to the Earth's climate equilibrium. The combustion of fossil fuels and deforestation release greenhouse gases, including carbon dioxide and methane, intensifying the natural greenhouse effect. As a result, the planet experiences a steady rise in average temperatures, leading to a cascade of adverse effects. Rising temperatures contribute to the melting of polar ice caps and glaciers, elevating sea levels and endangering coastal regions. Extreme weather events, such as hurricanes and wildfires, become more frequent and severe, disrupting ecosystems and communities. The delicate balance of biodiversity is under threat as species struggle to adapt to changing environments. Addressing global warming necessitates a comprehensive approach. Transitioning to renewable energy sources, enhancing energy efficiency, and promoting afforestation are crucial steps. International cooperation, exemplified by agreements like the Paris Agreement, underscores the shared responsibility in tackling this global challenge. Mitigating the impacts of global warming is not only an environmental imperative but also essential for ensuring the well-being of current and future generations. Urgent action to reduce emissions, protect ecosystems, and foster sustainable practices is vital to secure a resilient and sustainable future for our planet. It is a collective responsibility to safeguard the Earth from the repercussions of our own actions."
essay_on_birds = "Birds, with their diverse and captivating characteristics, play an integral role in the tapestry of our natural world. Spanning a vast array of species, from the majestic eagles soaring through the skies to the tiny hummingbirds flitting among flowers, birds exhibit remarkable adaptations and behaviors. Their ability to fly distinguishes them from most other animals, allowing for migration, foraging, and avoiding predators. Birds contribute significantly to ecosystems through pollination, seed dispersal, and controlling insect populations. Their intricate songs and vibrant plumage add aesthetic beauty to landscapes, making them a source of inspiration for art and culture. Despite their resilience, many bird species face threats such as habitat loss and climate change, underscoring the importance of conservation efforts to preserve the rich biodiversity they bring to our planet. Observing birds in their natural habitats provides a glimpse into the intricacies of nature and fosters a deeper appreciation for these feathered wonders."
def simple_chatbot(user_input):
    user_input = user_input.lower()

    # Define rules and responses
    rules_responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "Hello": ["Hi there!", "Hello!", "Hey!"],
        "hi": ["Hi there!", "Hello!", "Hey!"],
        "Hi": ["Hi there!", "Hello!", "Hey! How may I help you"],
        "how are you": ["I'm good, thanks!", "Doing well, how about you?", "I'm a chatbot, so I don't have feelings, but I'm here to help!"],
        "Write an essay on Global Warming": ["Global warming, driven by human activities, poses a critical threat to the Earth's climate equilibrium. The combustion of fossil fuels and deforestation release greenhouse gases, including carbon dioxide and methane, intensifying the natural greenhouse effect. As a result, the planet experiences a steady rise in average temperatures, leading to a cascade of adverse effects. Rising temperatures contribute to the melting of polar ice caps and glaciers, elevating sea levels and endangering coastal regions. Extreme weather events, such as hurricanes and wildfires, become more frequent and severe, disrupting ecosystems and communities. The delicate balance of biodiversity is under threat as species struggle to adapt to changing environments. Addressing global warming necessitates a comprehensive approach. Transitioning to renewable energy sources, enhancing energy efficiency, and promoting afforestation are crucial steps. International cooperation, exemplified by agreements like the Paris Agreement, underscores the shared responsibility in tackling this global challenge. Mitigating the impacts of global warming is not only an environmental imperative but also essential for ensuring the well-being of current and future generations. Urgent action to reduce emissions, protect ecosystems, and foster sustainable practices is vital to secure a resilient and sustainable future for our planet. It is a collective responsibility to safeguard the Earth from the repercussions of our own actions."],
        "Write an essay on Birds": ["Birds, with their diverse and captivating characteristics, play an integral role in the tapestry of our natural world. Spanning a vast array of species, from the majestic eagles soaring through the skies to the tiny hummingbirds flitting among flowers, birds exhibit remarkable adaptations and behaviors. Their ability to fly distinguishes them from most other animals, allowing for migration, foraging, and avoiding predators. Birds contribute significantly to ecosystems through pollination, seed dispersal, and controlling insect populations. Their intricate songs and vibrant plumage add aesthetic beauty to landscapes, making them a source of inspiration for art and culture. Despite their resilience, many bird species face threats such as habitat loss and climate change, underscoring the importance of conservation efforts to preserve the rich biodiversity they bring to our planet. Observing birds in their natural habitats provides a glimpse into the intricacies of nature and fosters a deeper appreciation for these feathered wonders."],
        "bye": ["Goodbye!", "See you later!", "Bye!"],
        "what is the formula of speed": ["Distance/Time"],
        "formula for distance": ["Time x Speed"],
        "why am i here": ["You have joined us for Ira Profusion 2023-24"],
        "where is the fun zone": ["There is one in the New Bouilding on Grond Floor at right side, and one at this floor at the very other end"],
        "give me names of different zone": ["Fun zone, Pottery, Science Squad, Steminist, Time Travellers, Robotics, Cafeteria, Byte the Bug, Zip-line"],
        "where is the pottery": ["Outside the new building"],
        "where is the science squad": ["New Building, first floor on left side"],
        "where is the steminist": ["New Building, first floor on right side"],
        "where is the time travellers": ["Old Building, first floor on left side"],
        "where is the robotics": ["Old Building, second floor on right side"],
        "where is the cafeteria": ["Old Building, ground floor on left side and New building in the Garden"],
        "where is the byte the bug": ["Old Building, first floor on right side"],
        "where is the zip-line": ["Old Building, on the terrace"],
        # Add more rules and responses as needed
    }

    # Check if user input matches any rule
    for rule, responses in rules_responses.items():
        if rule in user_input:
            return random.choice(responses)

    # If no matching rule is found, provide a default response
    return "I'm not sure how to respond to that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = simple_chatbot(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
