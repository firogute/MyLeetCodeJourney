/**
 * @param {number} x
 * @return {boolean}
 */

var isPalindrome = function (x) {
  let bool = true;
  const text1 = `${x}`;
  const text = [...text1];
  console.log(text);
  for (let i = 0; i < text.length; i++) {
    if (text[i] !== text[text.length - (i + 1)]) {
      bool = false;
      return bool;
    }
  }
  return bool;
};
