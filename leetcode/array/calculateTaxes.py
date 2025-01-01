def calculateTax( brackets, income) :
    ans = 0
    prev = 0

    for upper, percent in brackets:
      if income < upper:
        return ans + (income - prev) * percent / 100.0
      ans += (upper - prev) * percent / 100.0
      prev = upper

    return ans
print(calculateTax([[3,50],[7,10],[12,25]],10))
print(calculateTax([[1,0],[4,25],[5,50]],2))
# time -O(n) space-O(1)