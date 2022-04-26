import time


class Producer:
    """Define the resource intensive obj to instatiate"""

    def produce(self):
        print('Producer is working hard')

    def meet(self):
        print('Producers has time to meet you now')


class Proxy:
    """Define the relatively less resource intensive proxy to instantiate"""

    def __init__(self) -> None:
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print('Artist checking if producer is available...')

        if self.occupied == 'No':
            self.produce = Producer()
            time.sleep(2)
            # Make producer meet guest
            self.produce.meet()

        else:
            print('here')
            # Otherwise, dont instatntiate a producer
            time.sleep(2)
            print('Producer is busy!')


# Instantiate a proxy
p = Proxy()


p.occupied = 'yes'

p.produce()
