#1. init pre-test condition
#2. while 2. condition is True
# 3. statement(s)
# ...
# ...
# 4. update variable in condition (to eventually False)

count = 0                   #init
while count < 5:            #condition
    print(" *" * count)      #statement
    print("=" * count)
    count += 1              #update var

print("=== End of program ===")