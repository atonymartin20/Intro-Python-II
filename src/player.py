# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, name, cur_rm):
        self.name = name
        self.cur_rm = cur_rm