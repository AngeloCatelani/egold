/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    carry=0
    while(b!==0){
        carry = a & b
        console.log(carry,"carry")
        a = a ^ b
        console.log(a,"a")
        b = carry << 1
        console.log(b,"b")
    }
    return a
 };
 // Time = O(1)
 // space = O(1)
 a = 1, b = 2
 console.log(getSum(a,b))