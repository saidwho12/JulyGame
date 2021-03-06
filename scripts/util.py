# todo: comment

import random
import math


def mode_to_directory(mode):
    if mode == 0:
        return 'levels/normal'
    elif mode == 1:
        return 'levels/survival'
    elif mode == 2:
        return 'levels/maze'


def get_filename(mode, level_name, extention=''):
    return '{}/{}{}'.format(mode_to_directory(mode), level_name, extention)


def random_value(f):
    return (random.random() * 2 - 1) * f


def animate_int(n, j, rate):
    if n != j:
        d = j - n
        if abs(d) > rate:
            return n - rate * cmp(d, 0)
        else:
            return j
    return j


def vector_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)


def lerp_int(i, j, lerp):
    return i + (j - i) * lerp


def get_rect(w, h):
    return [(i, j) for i in (-w * .5, w * .5) for j in (-h * .5, h * .5)]


def get_dist_sqrd(a, b, y_offset=0):
    return (b.x - a.x) ** 2 + (b.y + y_offset - a.y) ** 2 + (b.z - a.z) ** 2


def sqr_distance_between(v1, v2):
    return sum([(i - j) ** 2 for i, j in zip(v1, v2)])


def distance_between(v1, v2):
    return sum([(i - j) ** 2 for i, j in zip(v1, v2)]) ** .5


def loop_time(time, secs, negative=True):
    percent = abs(((time % secs) / (secs * .5)) - 1)

    if negative:
        return percent * 2 - 1
    else:
        return percent


def angle_diff(a, b, rads=False):
    if rads:
        return ((b - a) + 3.14) % 6.28 - 3.14
    else:
        return ((b - a) + 180) % 360 - 180


def format_time(secs):
    if secs < 0:
        return '--:--.---'
    else:
        mins, secs = divmod(secs, 60)
        secs, ms = divmod(secs, 1)

        return '{mins:02d}:{secs:02d}.{ms:03d}'.format(mins=int(mins),
                                                       secs=int(secs),
                                                       ms=int(ms * 1000))


def get_time_str(seconds):
    if seconds is None:
        return 'N/A'
    else:
        mins, secs = divmod(round(float(seconds), 2), 60)

        if mins == 0:
            return '{} seconds'.format(secs)
        elif mins == 1.0:
            return '1 min {} secs'.format(secs)
        else:
            return '{} mins {} secs'.format(int(mins), secs)
