from count import err_count

for i in xrange(3):
    err_count.add_count()
    print(id(err_count))

from count import err_count

print(id(err_count))
