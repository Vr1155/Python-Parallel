'''
    Simple hello world ...
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()
print(f"Hello world...From  {rank}")

# compile and run this program by going to anaconda environments, play button, open in terminal
# the type following commands in the cmd:
# $mpiexec -n 4 python hello_world_in_mpi.py