# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, value):
        self.stack_enqueue.append(value)

    def dequeue(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def peek(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]

if __name__ == '__main__':
    q = int(input().strip())
    queue = QueueUsingTwoStacks()

    for _ in range(q):
        query = input().strip().split()
        command = int(query[0])

        if command == 1:  # Enqueue
            queue.enqueue(int(query[1]))
        elif command == 2:  # Dequeue
            queue.dequeue()
        elif command == 3:  # Print front
            print(queue.peek())
