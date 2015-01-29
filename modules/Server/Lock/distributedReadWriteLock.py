# -----------------------------------------------------------------------------
# Distributed Systems (TDDD25)
# -----------------------------------------------------------------------------
# Author: Sergiu Rafiliu (sergiu.rafiliu@liu.se)
# Modified: 31 July 2013
#
# Copyright 2012 Linkoping University
# -----------------------------------------------------------------------------

"""Class implementing a distributed version of ReadWriteLock."""

import threading
from . import readWriteLock


class DistributedReadWriteLock(readWriteLock.ReadWriteLock):

    """Distributed version of ReadWriteLock."""

    def __init__(self, distributed_lock):
        readWriteLock.ReadWriteLock.__init__(self)
        # Create a distributed lock
        self.distributed_lock = distributed_lock
        #
        # Your code here.
        #
        pass

    # Public methods

    def write_acquire(self):
        """Acquire the rights to write into the database.

        Override the write_acquire method to include obtaining access
        to the rest of the peers.

        """

        #
        # Your code here.
        #
        pass

    def write_release(self):
        """Release the rights to write into the database.

        Override the write_release method to include releasing access
        to the rest of the peers.

        """

        #
        # Your code here.
        #
        pass
