/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let outer =[]
    for (let i=0;i<arr.length;i++){
        let s = arr[i];
        
        if(fn(s,i)){
         outer.push(s)
        }
        
    }
    return outer
};