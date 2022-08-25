# Probability Calculator
# Instructions found at:
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

# Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 
# green balls. What is the probability that a random draw of 4 balls will 
# contain at least 1 red ball and 2 green balls? While it would be possible to 
# calculate the probability using advanced mathematics, an easier way is to 
# write a program to perform a large number of experiments to 
# estimate an approximate probability.

# For this project, you will write a program to determine the approximate 
# probability of drawing certain balls randomly from a hat.

# First, create a Hat class in prob_calculator.py. The class should take a 
# variable number of arguments that specify the number of balls of each color 
# that are in the hat. For example, a class object could be created 
# in any of these ways:

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

# A hat will always be created with at least one ball. The arguments 
# passed into the hat object upon creation should be converted to a contents 
# instance variable. contents should be a list of strings containing one item
# for each ball in the hat. Each item in the list should be a color name 
# representing a single ball of that color. 
# For example, if your hat is {"red": 2, "blue": 1}, 
# contents should be ["red", "red", "blue"].

# The Hat class should have a draw method that accepts an argument 
# indicating the number of balls to draw from the hat. This method should 
# remove balls at random from contents and return those balls as a list of 
# strings. The balls should not go back into the hat during the draw, 
# similar to an urn experiment without replacement. If the number of balls
# to draw exceeds the available quantity, return all the balls.

# Next, create an experiment function in prob_calculator.py (not inside 
# the Hat class). This function should accept the following arguments:

#     hat: A hat object containing balls that should be copied 
#          inside the function.
#     expected_balls: An object indicating the exact group of balls to 
#          attempt to draw from the hat for the experiment. For example, 
#          to determine the probability of drawing 2 blue balls and 1 red 
#          ball from the hat, set expected_balls to {"blue":2, "red":1}.
#     num_balls_drawn: The number of balls to draw out of the hat in each experiment.
#     num_experiments: The number of experiments to perform. (The more 
#          experiments performed, the more accurate the approximate 
#          probability will be.)

# The experiment function should return a probability.

# For example, if you want to determine the probability of getting at least 
# two red balls and one green ball when you draw five balls from a hat 
# containing six black, four red, and three green. To do this, you will 
# perform N experiments, count how many times M you get at least two red 
# balls and one green ball, and estimate the probability as M/N. Each 
# experiment consists of starting with a hat containing the specified 
# balls, drawing several balls, and checking if you got the balls you 
# were attempting to draw.

# Here is how you would call the experiment function based on the 
# example above with 2000 experiments:

# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)

# Since this is based on random draws, the probability will be 
# slightly different each time the code is run.

import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball_color, count in balls.items():
            i = 0
            while i != count:
                self.contents.append(ball_color)
                i += 1

    def draw(self, draw_count):
        drawn_balls = []
        i = 0
        
        # If too many balls are drawn, return all drawn balls
        if draw_count > len(self.contents):
            for ball in drawn_balls:
                self.contents.append(ball)
            drawn_balls = []
    
        # Else proceed to draw balls until given number
        else:
            while i != draw_count:
                drawn = random.choice(self.contents)
                self.contents.remove(drawn)
                drawn_balls.append(drawn)
                i += 1
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # Create success sample template
    template = {}
    for ball_color, count in expected_balls.items():
        template[ball_color] = template.get(ball_color, 0) + count
    positives = 0

    # Start experiments
    for x in range(0, num_experiments):
        hat_balls = hat.contents.copy()

        # Draw balls
        sample = {}
        for y in range(0, num_balls_drawn):
            if len(hat_balls) > 0:
                drawn = random.choice(hat_balls)
                sample[drawn] = sample.get(drawn, 0) + 1
                hat_balls.remove(drawn)

            # Skip if no available balls in hat
            elif len(hat_balls) == 0:
                pass
        
    # Determine success
        i = 0 
        for ball_color, count in template.items():
            # Create key:value pair in sample if needed
            sample[ball_color] = sample.get(ball_color, 0)
            # Compare key:value pairs in sample vs template
            if sample[ball_color] >= template[ball_color]:
                i += 1
            else:
                break

        # If all colored balls were checked, add 1 to positive result
        if i >= len(template):
            positives += 1

    probability = positives / num_experiments
    return probability

