import copy
import random


class Hat:
    def __init__(self, **kwarg):
        contents = []
        for key in kwarg:
            for n in range(kwarg[key]):
                contents.append(key)
        self.contents = contents

    def draw(self, number):
        contents = self.contents
        draw_ball = []
        if number >= len(contents):
            return contents
        else:
            for n in range(number):
                len_contents = len(contents)
                i = random.randrange(len_contents)
                x = contents[i]
                draw_ball.append(x)
                contents = contents[0:i] + contents[i + 1:]
        self.contents = contents
        return draw_ball


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    bad = 0

    for n in range(num_experiments):
        exp_ = copy.deepcopy(hat)
        prova = exp_.draw(num_balls_drawn)
        # print(f'drawn:  {prova} expected: {expected_balls}')
        for v in expected_balls.keys():
            count = 0
            for x in range(len(prova)):
                if prova[x] == v:
                    count += 1
            if count < expected_balls[v]:
                bad += 1
                # print(f'bad experiment, prob:  {count}/{num_experiments}') // so use bad instead of count
                # count -= 1
                break
                # print(f'good experiment, prob:  {count}/{num_experiments}') // good exp - but not necessary

    return 1 - bad / num_experiments

