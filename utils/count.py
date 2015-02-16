class Count(object):
    def __init__(self, info):
        self.info = info
        self.count = 0

    def add_count(self):
        print("the count is %s " % (self.count))
        self.count += 1

    def report_count(self):
        self.count = 0
        return self.count

err_count = Count("Xiami Connection error")
