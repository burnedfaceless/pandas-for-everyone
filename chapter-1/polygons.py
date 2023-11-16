import mariadb
import math
import matplotlib.patches as patches
import pylab

# Connect to MariaDB Server
conn = mariadb.connect(
    user='brian',
    password='brian',
    host='localhost',
    port=3306,
    database='service_territory'
)

# Get Cursor
cur = conn.cursor()

# Execute Query
cur.execute('SELECT lat, lng FROM addresses WHERE system_id = 4')

# Get Results as Tuples
result = cur.fetchall()

# convert the list of rows to a list of tuples
tuples_list = [row for row in result]

cent = (sum p[0] for p in tuples_list) / len(tuples_list), (sum p[1] for p in tuples_list) / len(tuples_list)
tuples_list.sort(key = lambda p: math.atan2(p[1] - cent[1], p[0] - cent[0]))
pylab.scatter((p[0] for p in tuples_list), (p[1] for p in tuples_list))
pylab.gca().add_patch(patches.Polygon(tuples_list, closed=False, fill=False))
pylab.grid()
pylab.show()


print(cur)


