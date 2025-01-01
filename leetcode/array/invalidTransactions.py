import collections
def invalidTransactions(transactions)  :
        ans = []
        nameToTranses = collections.defaultdict(list) #defaultdict(<class 'list'>, {}) bif you give empty{}will throw key error so give defaultdict(list)

        for t in transactions:
          name, time, amount, city = t.split(',')
          time, amount = int(time), int(amount)
          nameToTranses[name].append({'time': time, 'city': city}) #{'alice': [{'time': 20, 'city': 'mtv'}, {'time': 50, 'city': 'beijing'}]}

        for t in transactions:
          name, time, amount, city = t.split(',')
          time, amount = int(time), int(amount)
          if amount > 1000:
            ans.append(t)
          elif name in nameToTranses:
            for sameName in nameToTranses[name]:
              if abs(sameName['time'] - time) <= 60 and sameName['city'] != city:
                ans.append(t)
                break

        return ans
print(invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print(invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))