#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = Object.entries(dict).reduce((item, [k, v]) => {
  item[v] = item[v] ? [...item[v], k] : [k];
  return item;
}, {});

console.log(newDict);
