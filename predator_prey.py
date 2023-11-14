import logging
from pathlib import Path

from libmuscle.runner import run_simulation
import ymmsl


from muscle3playground.lotkavolterra import predator
from muscle3playground.lotkavolterra import prey

# Configure Python logging
logging.basicConfig()
logging.getLogger('yatiml').setLevel(logging.WARNING)

# Set this to logging.DEBUG to get some more information
logging.getLogger().setLevel(logging.INFO)

# Load configuration
configuration = ymmsl.load(Path('predator_prey.ymmsl'))
configuration.model.conduits = [
        ymmsl.Conduit('prey.prey_temp', 'predator.prey_temp'),
        ymmsl.Conduit('predator.predator_temp', 'prey.predator_temp')
        ] #TODO: use ymmsl file for this

# Connect the model functions to the configuration
implementations = {'predator': predator, 'prey': prey}

# And run the coupled simulation!
run_simulation(configuration, implementations)
