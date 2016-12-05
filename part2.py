
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

labal = [("ป้อนชื่อ : "),("ชื่อคุณคือ : ")]

s= (raw_input(labal[0]))
print ((labal[1])+ (s))

s= (input(labal[0]))#python 2.7 input object
print ((labal[1])+ s)
