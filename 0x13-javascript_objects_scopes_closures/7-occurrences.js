#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;

  for (let x = 0; x < list.length; x++) {
    i = (list[x] === searchElement ? i + 1 : i);
  }
  return i;
};
