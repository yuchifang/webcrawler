print("moduleX.py")

# https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3
# https://pavolkutaj.medium.com/why-import-of-sibling-packages-does-not-always-work-in-python-16b87d2134a


# todo ---------------------
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3

# 測試 下面的 方法看看
# https://www.geeksforgeeks.org/python-import-from-parent-directory/
# https://stackoverflow.com/questions/7505988/importing-from-a-relative-path-in-python

# Absolute Import google 

# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3

# 測試 下面的 方法看看
# https://www.geeksforgeeks.org/python-import-from-parent-directory/

# todo new
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
import sys
print(sys.version)
print(sys.version_info)
print(sys.path)

# from .moduleY import sample
# python3 -m importSample.subpackage1.moduleX
# 這種情況 
# python3 -m subpackage1.moduleX
# 可以成功


# from moduleA import sample
# 這種方法可以 是因為把
from importSample.subpackage1.moduleY import sample