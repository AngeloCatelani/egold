/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let diff = 0;
    let map = {};
    let arr = [];
    for(let i =0; i<nums.length; i++){
        diff = target - nums[i];
        if(map.hasOwnProperty(diff)){
         return [map[diff],i]

        }
        else{
            map[nums[i]] = i;
            };
    }
    return [];
};