import time

class LeakyBucket:
    def __init__(self, capacity, leakRate):
        """
        Initializes the Leaky Bucket
        :param capacity: Maximum number of requests the bucket can hold
        :param leakRate: Number or requests processed (leaked) per second
        """
        self.capacity = capacity #
        self.leakRate = leakRate #Requests per second
        self.currentLoad = 0 #Current number of requests in the bucket
        self.lastChecked = time.time()

    def leak(self):
        """
        Updates the current load by leaking requests based on the elapsed time
        """
        now = time.time()
        elapsedTime = now - self.lastChecked
        leaked = elapsedTime * self.leakRate
        self.currentLoad = max(0, self.currentLoad - leaked)
        self.lastChecked = now
    
    def allowRequest(self):
        """
        Checks if a new request can be processed. If so, it return True, False otherwise
        :return: return True if so, False otherwise 
        """
        self.leak()
        if self.currentLoad < self.capacity:
            self.currentLoad += 1 #Add the new request to the bucket
            return True
        return  False

if __name__ == "__main__":
    bucket = LeakyBucket(capacity = 5, leakRate = 1)
    for i in range(10):
        if bucket.allowRequest():
            print(f"Request {i+1} allowed")
        else:
            print(f"Request {i+1} not allowed")


