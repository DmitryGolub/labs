# 1 задание
import math
from datetime import datetime


print(math.sqrt(4))
print(datetime.now())

# 2 задание
from pack.my_module import get_ip

print(get_ip())

# 3 задание
from pack.my_module import *

print(get_ip())

from pack import my_module, my_module2

print(my_module.get_ip())
print(my_module2.test(1, 2))

from pack import *

print(my_module.get_ip())
print(my_module2.test(2, 8))
