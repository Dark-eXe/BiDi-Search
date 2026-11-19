from bidisearch import Queue

def test_queue():
    testQueue = Queue()
    assert testQueue.isEmpty()

    for i in range(5):
        testQueue.enqueue(i)
    assert not testQueue.isEmpty()
    for i in range(5):
        assert i == testQueue.dequeue()

    assert testQueue.isEmpty()