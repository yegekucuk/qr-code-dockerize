import generator
from time import sleep
import sys

print("Parameters in python: ", sys.argv)

if len(sys.argv) != 3:
    print("Usage: ./run.sh <filename> <data>\nExiting python program")
    sys.exit(1)

filename = sys.argv[1]
data = sys.argv[2]

generator.generate_qr(name=filename,data=data)
generator.show_qr_code(name=filename)
print("successfully generated")

# For Docker container to not shut down automaticly, we need to make program wait forever. The program will be shutted down when we manually shut down with:
# docker stop {container_name}
# The container gets removed after the usage when the application ran with run.sh file.
while True:
    sleep(1)
