import gevent

from gevent.queue import Queue
from gevent import monkey
monkey.patch_socket()

from utils.log import logger


class Worker(object):
    def __init__(self, workers_number):
        self.workers_number = workers_number
        self.tasks = Queue()

    def put_tasks(self, all_tasks):
        '''
        The boss put all tasks into queue
        '''
        for one_task in all_tasks:
            self.tasks.put_nowait(one_task)

    def generate_boss(self, all_tasks):
        '''
        '''
        self.all_tasks_number = len(all_tasks)
        boss = [gevent.spawn(self.put_tasks, all_tasks)]
        return boss

    def get_tasks(self, worker_id, func, *args, **kwargs):
        '''
        The worker get all tasks from queue, and run the
        corresponding function
        '''
        while not self.tasks.empty():
            task = self.tasks.get()
            progress = self.show_progress()
            func(task, progress, *args, **kwargs)
            # logger.info("The worker %s has got task %s " % (worker_id, task))

    def generate_workers(self, func, *args, **kwargs):
        '''
        Generate workers array
        '''
        workers = [gevent.spawn(self.get_tasks, worker_id,
                   func, *args, **kwargs)
                   for worker_id in xrange(1, self.workers_number + 1)]
        return workers

    def joinall(self, boss, workers):
        all_spawns = boss + workers
        gevent.joinall(all_spawns)

    def show_progress(self):
        '''
        Show the progress in two ways
        1. current_task / all_task
        2. the percentage
        '''
        self.current_tasks_id = self.tasks.qsize()
        progress_one = '%s/%s' % (self.current_tasks_id, self.all_tasks_number)

        progress_percentage = 1 - float(self.current_tasks_id)\
            / float(self.all_tasks_number)
        progress_two = "%s" % (progress_percentage * 100)
        progress = [progress_one, progress_two]
        return progress
