#!/usr/bin/node
exports.esrever = function (list) {
  const listLength = list.length;
  const list2 = [];
  let list2Length = listLength;
  for (let i = 0; i < listLength; i++) {
    list2[list2Length - 1] = list[i];
    list2Length--;
  }
  return (list2);
};
