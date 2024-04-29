'''
    Simple scatter an array to multiple processes and sub-arrays
'''

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()
size = comm.Get_size() # gives total number of processes (-n 4)

# had to use numpy arrays because simple string data type was not working.
# 

sendingData = None
dataPerRank = 10

if rank == 0:
    sendingData = np.linspace(1, size*dataPerRank, size*dataPerRank)
    # when -n 4, here size = 4 ---> sendingData --> {1, 0:40, 0} 
    # i.e. 0th index to 40th index is filled with 1s, rest with 0s.

recvData = np.empty(dataPerRank, dtype='d')
comm.Scatter(sendingData, recvData, root = 0)
print(f"Rank: {rank} data: {recvData}")

# Scatter means it takes a range of data and sends to everyone 
# (i.e. it can send different data to everyone).
# broadcast means it will send it to everyone.

# if you want to run a large number of processors
# use this command:
# $mpiexec -20 python mpFour.py -core 4

# note that here, 20 is the number of processors
# and 4 is the number of processors.