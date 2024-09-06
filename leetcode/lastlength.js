const lengthOfLastWord = (string)=> {
  
    let newArr = string.trim().split(" ")
    console.log(newArr,"newArr")
    let last = newArr[newArr.length-1]
    console.log(last,"last")
    console.log(last.length)
    return last.length
    };

    s ="   fly me   to   the moon  "
    lengthOfLastWord(s)