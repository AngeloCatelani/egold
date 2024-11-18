def minFlips( target: str) -> int:
        flips = 0
        status = '0'
        for c in target:
            if c != status:
                flips += 1
                # status = '0' if status == '1' else '1'
                if status =="1": status ="0"
                else: status = "1"
        return flips
print(minFlips("10111"))
