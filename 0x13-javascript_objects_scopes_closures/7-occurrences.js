#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const listLenght = list.length;
  for (let i = 0; i < listLenght; i++) {
    if (list[i] === searchElement) {
      count = count + 1;
    }
  }
  return (count);
};
