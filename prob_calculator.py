import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents

        balls_drawn = random.sample(self.contents, num_balls_drawn)
        for ball in balls_drawn:
            self.contents.remove(ball)

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True

        for ball, count in expected_balls.items():
            if drawn_balls.count(ball) < count:
                success = False
                break

        if success:
            num_successful_experiments += 1

    return num_successful_experiments / num_experiments
