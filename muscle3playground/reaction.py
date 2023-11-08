import numpy as np

from libmuscle import Instance, Grid, Message
from ymmsl import Operator

def reaction():
    """A simple exponential reaction model on a 1D grid.
    """
    instance = Instance({
            Operator.F_INIT: ['initial_state'],       # np.array
            Operator.O_F: ['final_state']})           # np.array

    while instance.reuse_instance():
        # begin F_INIT
        t_max = instance.get_setting('t_max', 'float')
        dt = instance.get_setting('dt', 'float')
        k = instance.get_setting('k', 'float')

        msg = instance.receive('initial_state')
        U = msg.data.array.copy()

        t_cur = msg.timestamp
        t_max = msg.timestamp + t_max
        # end F_INIT

        # begin state_update_loop
        while t_cur + dt < t_max:
            # begin O_I
            # end O_I

            # begin S
            U += k * U * dt
            t_cur += dt
            # end S
        # end state_update_loop

        # begin O_F
        final_message = Message(t_cur, None, Grid(U, ['x']))
        instance.send('final_state', final_message)
        # end O_F