'''
There is a queue for the self-checkout tills at the supermarket. Your task is 
write a function to calculate the total time required for all the customers to 
check out!

input
customers: an array of positive integers representing the queue. Each integer 
represents a customer, and its value is the amount of time they require to 
check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand 
the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) 
proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified 
above.

P.S. The situation in this kata can be likened to the 
more-computer-science-related idea of a thread pool, with relation to running 
multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
'''
import heapq

# 1st Method


def queue_time_1(customers, n):
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)


# TODO -
# add second method from saved in Code\python-snippets\supermarket.py

# 2nd Method
def queue_time_2(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)


# 3nd Method
class MarketQueue():

    def __init__(self, customers, n):
        self.customers = customers
        self.n = n
        self.timer = 0
        self.active_checkouts = []

    def calculate_total_time(self):
        while self.customers:
            self.process_queue()
        return self.timer

    def process_queue(self):
        if len(self.active_checkouts) < self.n:
            queue_index = self.n - len(self.active_checkouts)
            self.active_checkouts.extend(self.customers[:queue_index])
            self.customers[:queue_index] = []
        while self.active_checkouts and (len(self.active_checkouts) == self.n or not self.customers):
            self.timer += 1
            self.process_active_checkouts()

    def process_active_checkouts(self):
        finished_customers = []
        for index, customer in enumerate(self.active_checkouts):
            if customer > 1:
                self.active_checkouts[index] = int(customer-1)
            else:
                finished_customers.append(customer)

        for finished in finished_customers:
            self.active_checkouts.remove(finished)

# implementing requirements


def queue_time(customers, n):
    return MarketQueue(customers, n).calculate_total_time()


# Debug
print(queue_time_1([1, 2, 3, 4, 5], 1))
print(15)
