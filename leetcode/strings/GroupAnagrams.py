class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #defaultdict(<class 'list'>, {}) res []
        # print(res,"res")
        
        for s in strs:
            count = [0]*26 #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] count
            # print(count,"count") creating list with 26 zeros

            for c in s:
                # print(c,"c") each letter eg:e,a,t,a,t,e
                count[ord(c) - ord("a")]+=1 # to have index within 25 80-80=0
                # print(count,"count")
            # print( res[tuple(count)],"red")first res will be [] then whole strs will be added
            # print(tuple(count),"tuple")(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) tuple for "eat"
            res[tuple(count)].append(s)
        return res.values()
              # time complesity - O(m*n) where m is the total length strs and n is the length of each string