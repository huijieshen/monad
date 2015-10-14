"""
Copyright 2015 Ericsson AB

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the 
specific language governing permissions and limitations under the License.
"""
from dbConnection import DB
from fitness import Fitness
from deap import base, creator, tools

# Constant
INDIVIDUAL_SIZE = 24
POPULATION_SIZE = 100

# Initialize the classes
databaseClass = DB()
fitnessClass = Fitness()

# Creating a minimizing fitness class to minimize a single objective that 
# inherits from the base class "Fitness".
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# Creating an individual class that inherits a list property and has a fitness 
# attribute of type FitnessMin
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize the toolbox from the base class
toolbox = base.Toolbox()

# Register the operations to be used in the toolbox
toolbox.register("attribute", databaseClass.generateTripTimeTable, 2)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, INDIVIDUAL_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual,
                 POPULATION_SIZE)
toolbox.register("evaluate", fitnessClass.evalIndividual)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("select", tools.selTournament, tournsize=3)
