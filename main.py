import sys
from credentials import cur

cur.execute("SELECT * from orders;")