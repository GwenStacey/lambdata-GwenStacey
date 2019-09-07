'''A simple class example'''


class Monster:
    '''A base monster class'''
    
    def __init__(self, name, height, num_arms):
        self.name = name
        self.height = height
        self.num_arms = num_arms
    
    def print_monster(self):
        '''Print the monster and its stats'''
        print('{} is {} feet tall, has {} arms'.format(self.name, 
                                                       self.height,
                                                       self.num_arms))

    
class Godzilla(Monster):
    
    def __init__(self, name = 'Godzilla', height = 164, num_arms = 2):
        self.name = name
        self.height = height
        self.num_arms = num_arms 

    def print_monster(self):
        '''Print the monster and its stats'''
        print('{} is {} feet tall, has {} arms'.format(self.name,
                                                       self.height,
                                                       self.num_arms))