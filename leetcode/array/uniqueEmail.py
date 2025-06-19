def numUniqueEmails(self, emails: List[str]) -> int:
        #  add a plus '+' in the local name, everything after the first plus sign will be ignored. 
        # add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.


        # see . join together without .
        # see + remove after + sign
        # return count of mail ids
        # s= set()
        # for e in emails:
        #     local,domain = e.split("@")
        #     local = local.split("+")[0] # takes only 0 indexed element
        #     print(local)
        #     local = local.replace(".","")
        #     s.add((local,domain)) #{('testemail', 'leetcode.com')}
        #     print(s)

        # return len(s)
        s =set()

        for e in emails:
            i,local = 0,""
            while e[i] not in ["@","+"]:
                if e[i] != ".":
                    local+=e[i]
                i+=1
            while e[i] != "@":
                i+=1
            domain = e[i+1:]
            print(domain,i,i+1)
            s.add((local,domain))
        return len(s)
            