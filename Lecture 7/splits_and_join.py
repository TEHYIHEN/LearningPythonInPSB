name_str = "bobo chacha dodo ah gogo"

names = name_str.split()
print(names)

current_date = "7/5/2026"
data_parts = current_date.split("/")
print(data_parts)

if len(data_parts[0]) == 1:   #当一组号码大过1， 例如 19/5/2026 , 结果会是 ["19","05","2026"], 不是“019”
    data_parts[0] = "0" + data_parts[0]
elif len(data_parts[1]) == 1:
    data_parts[1] = "0" + data_parts[1]

print(data_parts)

# 07-05-2026

updated_date = "-".join(data_parts)
print(updated_date)
