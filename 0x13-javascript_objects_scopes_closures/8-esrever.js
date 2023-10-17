#!/usr/bin/node

exports.esrever = function (list) {
  const rList = [];
  for (let x = list.length - 1; x >= 0; x--) {
    rList.push(list[x]);
  }
  return (rList);
};
