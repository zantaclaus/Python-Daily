import math

minute = float(input("Enter minute: "))
net = float(input("Enter net: "))

net_price_1 = 0
minute_price_1 = 0
net_price_2 = 0
minute_price_2 = 0
net_price_3 = 0
minute_price_3 = 0

# Case 299
if net > 1.5:
    net_over = net - 1.5
    if net_over % 5 > 0 and net_over % 5 <= 1:
        x = 1
        y = int(net_over / 5)
    else:
        x = 0
        y = math.ceil(net_over / 5)
    net_price_1 = x*99 + y*150
if minute > 100:
    minute_price_1 = (minute - 100) * 1.59

# Case 399
if net > 5:
    net_over = net - 5
    if net_over % 5 > 0 and net_over % 5 <= 1:
        x = 1
        y = int(net_over / 5)
    else:
        x = 0
        y = math.ceil(net_over / 5)
    net_price_2 = x*99 + y*150
if minute > 150:
    minute_price_2 = (minute - 150) * 1.59

# Case 599
if net > 16:
    net_over = net - 16
    if net_over % 5 > 0 and net_over % 5 <= 1:
        x = 1
        y = int(net_over / 5)
    else:
        x = 0
        y = math.ceil(net_over / 5)
    net_price_3 = x*99 + y*150
if minute > 300:
    minute_price_3 = (minute - 300) * 1.59

print(f"net: {net_price_1}, minute: {minute_price_1}")
print(f"net: {net_price_2}, minute: {minute_price_2}")
print(f"net: {net_price_3}, minute: {minute_price_3}")

package1 = 299 + net_price_1 + minute_price_1
package2 = 399 + net_price_2 + minute_price_2
package3 = 599 + net_price_3 + minute_price_3

if package1 < package3 and package2 < package3:
    if package1 < package2:
        print("package1", package1)
    else:
        print("package2", package2)

if package1 < package2 and package3 < package2:
    if package1 < package3:
        print("package1", package1)
    else:
        print("package3", package3)

if package2 < package1 and package3 < package1:
    if package2 < package3:
        print("package2", package2)
    else:
        print("package3", package3)
