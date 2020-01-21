from __future__ import unicode_literals, print_function

import pytesseract as tess
from spacy.lang.en import English
import spacy
import pymunk

# nlp = English()
nlp = spacy.load("en_core_web_sm")
test = "test.jpg"
kine_question1 = "A ball thrown vertically upwards with a speed of 9.6m/s from the top of a tower returns to the " \
                 "earth in 6sec. Find height of the tower."
kine_question2 = "An airplane accelerates down a runway at 3.20 m/s2 for 32.8 s until is finally lifts off " \
                 "the ground. Determine the distance traveled before takeoff."
kine_question3 = "A car starts from rest and accelerates uniformly over a time of 5.21 seconds for " \
                 "a distance of 110 m. Determine the acceleration of the car."
kine_question4 = "Upton Chuck is riding the Giant Drop at Great America. If Upton free falls for 2.60 seconds," \
                 " what will be his final velocity and how far will he fall?"
s = tess.image_to_string(test)
# print(s)

doc = nlp(kine_question1)
# spacy.displacy.serve(doc)

nlp2 = English()
nlp2.add_pipe(nlp2.create_pipe('sentencizer'))  # updated
doc2 = nlp2(kine_question1)
sentences = [sent.string.strip() for sent in doc2.sents]
for tok in doc2:
    if not tok.is_stop:
        print(tok)
print(sentences)
# Read about how displacy makes its syntactic dependencies or whatever


class PhysicalObject:
    def __init__(self):
        self.initial_velocity_vector = (0, 0)
        self.initial_position_vector = (0, 0)  # assume all bodies to start above "EARTH" / "GROUND" / "FLOOR"
        self.shape = None


space = pymunk.Space()      # Create a Space which contain the simulation
space.gravity = 0,-1000     # Set its gravity

body = pymunk.Body(1,1666)  # Create a Body with mass and moment
body.position = 50,100      # Set the position of the body

poly = pymunk.Poly.create_box(body) # Create a box shape and attach to body
space.add(body, poly)       # Add both body and shape to the simulation

while True:                 # Infinite loop simulation
    space.step(0.02)        # Step the simulation one step forward

