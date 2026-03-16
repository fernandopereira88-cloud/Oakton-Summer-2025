class RollercoasterQueue:
    def __init__(self, ride_seats, ride_length):
        self.__ride_seats = ride_seats
        self.__ride_length = ride_length
        self.__queue_length = 0

    def board_ride(self):
        if self.__queue_length >= self.__ride_seats:
            self.__queue_length -= self.__ride_seats
        else:
            self.__queue_length = 0

    def enqueue(self):
        self.__queue_length += 1

    def length(self):
        return self.__queue_length


# --- Main Program ---
# Prompt user for input
ride_seats = int(input("Enter the number of seats on the ride: "))
ride_length = int(input("Enter the ride duration in minutes: "))

# Store the instance in rc_queue
rc_queue = RollercoasterQueue(ride_seats, ride_length)

# Simulate 20 people joining the queue
for _ in range(20):
    rc_queue.enqueue()

# Board the ride repeatedly until the queue is empty
while rc_queue.length() > 0:
    rc_queue.board_ride()
    print(f"{rc_queue.length()} people still waiting in the queue.")
