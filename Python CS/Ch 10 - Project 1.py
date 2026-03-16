class RollercoasterQueue:
    def __init__(self,seats,length):
        self.__queue_length = 0
        self.__ride_seats = seats
        self.__ride_length = length
        

    def board_ride(self):
        if self.__queue_length >= self.__ride_seats:
            self.__queue_length = self.__queue_length - self.__ride_seats
        else:
            self.__queue_length = 0


    def enqueue(self):
        self.__queue_length += 1

    def length(self):
        return self.__queue_length


a = int(input("How many people fit in one ride?"))
b = int(input("How long is the ride, in minutes?"))
print(a)
print(b)             
rc_queue = RollercoasterQueue(a,b)



for i in range(1,21):
            rc_queue.enqueue()
            #print('Board',rc_queue.length())

while rc_queue.length() > 0:
            rc_queue.board_ride()
            print(rc_queue.length())

        
