/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  var len = nums.length;
  var last = NaN;
  var count = 0;
  for (var i = 0; i < len; i++) {
    if (nums[i] !== last) {
      nums[count] = nums[i];
      last = nums[i];
      count++;
    }
  }
  return count;
};
