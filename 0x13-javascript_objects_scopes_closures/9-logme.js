#!/usr/bin/node

let printed = 0;

exports.logMe = function (item) {
  console.log(`${printed}: ${item}`);
  printed += 1;
};
