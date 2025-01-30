def getSpamEmails(subjects, spam_words):
    # Write your code here
    arr=[]
    count=0
    for i in range(len(subjects)):
        for j in range(len(subjects[i])):
            splitArr = subjects[i].split()
        # check = any(item in splitArr for item in spam_words)
        # if check is True:
        #     arr.append("spam")
        # else:
        #     arr.append("not_spam")
        if j <= len(spam_words):
            if splitArr[j] in spam_words:
              count+=1
            elif splitArr[j] not in spam_words:
               continue
            elif count >=2:
              arr.append("spam")
              count = 0
              break
            else:
              arr.append("not_spam")
              print(arr,"arr")
    return arr
        
subjects = ["I paid him paid", "Summertime Sadness"]
spam_words = ["I", "Sadness", "paid"]
print(getSpamEmails(subjects,spam_words))