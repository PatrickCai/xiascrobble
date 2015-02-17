class Count(object):
    def __init__(self, info):
        self.info = info
        self.count = 0

    def add_count(self):
        self.count += 1

    def report_count(self):
        count = self.count
        self.count = 0
        return count

err_count = Count("Xiami Connection error")
