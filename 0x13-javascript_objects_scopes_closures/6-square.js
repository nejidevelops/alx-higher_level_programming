#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    for (let i = 1; i <= this.height; i++) {
      let row = '';
      for (let j = 1; j <= this.width; j++) row += c || 'X';
      console.log(row);
    }
  }
}

module.exports = Square;
