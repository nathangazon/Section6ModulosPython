'''
datetime
'''

from datetime import datetime
from pytz import timezone

# data_str_data = '2023/03/22 18-22-00'
# data_str_fmt = '%Y/%m/%d %H-%M-%S'

# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)

data = datetime.now(timezone('Asia/Tokyo'))
print(data)
print(data.timestamp())
print(datetime.fromtimestamp(1679540891.029234))
