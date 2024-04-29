'''
    Sending data from one process to another
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

# similarly we can send various other data types in python like,
# numpy arrays or python lists, sets, dictionaries and tuples.

if rank == 0:
    data = ["Hello", 32352, 5324.234532, True, (234, "grofea", 432.234)]
    print(f"First Processor sending")
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print(f"Received data from the first processor: {data}")

