# -----------------------------------------------------------------------------
# Distributed Systems (TDDD25)
# -----------------------------------------------------------------------------
# Author: Sergiu Rafiliu (sergiu.rafiliu@liu.se)
# Modified: 24 July 2013
#
# Copyright 2012 Linkoping University
# -----------------------------------------------------------------------------

"""Implementation of a simple database class."""

import random


class Database(object):

    """Class containing a database implementation."""

    def __init__(self, db_file):
        self.db_file = db_file
        self.rand = random.Random()
        self.rand.seed()
        self.db_array = []
        temp_fortune = ""
        f = open(self.db_file,'r')
        for line in f:
            if(line != "%\n"):
                temp_fortune+=line
            else:
                self.db_array.append(temp_fortune)
                temp_fortune = ""
        f.close()

    def read(self):
        """Read a random location in the database."""
        return self.db_array[self.rand.randint(0,len(self.db_array))]
        
        

    def write(self, fortune):
        """Write a new fortune to the database."""
        self.db_array.append(fortune)
        f = open(self.db_file,'a')
        f.write(fortune+'\n')
        f.write("%\n")
        f.close()
