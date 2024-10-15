wmt_stock_price_queue = []

#always inserting at 0 position
#when new value inserted the rest are pushed
#FIFO first iin first out
wmt_stock_price_queue.insert(0, 131.0)
wmt_stock_price_queue.insert(0, 132.12)
wmt_stock_price_queue.insert(0, 135)
print(wmt_stock_price_queue)

#FIFO
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())

#issues with dynamic array.
# If location run out ,
#   1.py)need to allocate new space and
#   2)the  copy all info to new location

