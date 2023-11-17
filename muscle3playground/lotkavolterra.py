import numpy as np
import copy

from libmuscle import Instance, Message
from ymmsl import Operator

def predator():
    """Predator dynamics"""
    instance = Instance({
        Operator.O_I: ['predator_temp'], # Has to send predator information
        Operator.S: ['prey_temp'], # Has to receive prey information
    })

    while instance.reuse_instance():
        # begin F_INIT
        a = instance.get_setting('a', 'float')
        b = instance.get_setting('b', 'float')
        dx = lambda x, y : a*x - b*x*y

        t_max = instance.get_setting('t_max', 'float')
        dt = instance.get_setting('dt', 'float')
        t_cur = 0.0

        predator_temp = 1.0
        # end F_INIT

        while t_cur + dt < t_max:
            # begin O_I
            msg = Message(t_cur, None, predator_temp)
            instance.send('predator_temp', msg)
            # end O_I

            # begin S
            msg = instance.receive('prey_temp')
            prey_temp = copy.copy(msg.data)
            predator_temp += dx(predator_temp, prey_temp)
            t_cur += dt
            # end S


def prey():
    """Prey dynamics"""
    instance = Instance({
        Operator.O_I: ['prey_temp'], # Has to send prey information
        Operator.S: ['predator_temp'], # Has to receive predator information
    })

    while instance.reuse_instance():
        # begin F_INIT
        c = instance.get_setting('c', 'float')
        d = instance.get_setting('d', 'float')
        dy = lambda x, y : c*x*y - d*y

        t_max = instance.get_setting('t_max', 'float')
        dt = instance.get_setting('dt', 'float')
        t_cur = 0.0

        prey_temp = 2.0
        # end F_INIT
        while t_cur + dt < t_max:
            # begin O_I
            msg = Message(t_cur, None, prey_temp)
            instance.send('prey_temp', msg)
            # end O_I

            # begin S
            msg = instance.receive('predator_temp')
            predator_temp = copy.copy(msg.data)
            prey_temp += dy(predator_temp, prey_temp)
            t_cur += dt
            # end S
