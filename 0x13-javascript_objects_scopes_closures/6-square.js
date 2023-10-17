#!/usr/bin/node
/**
 * Square class inherits from Square
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myCh = c === undefined ? 'X' : c;
    for (let x = 0; x < this.height; x++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myCh;
        y++;
      }
      console.log(myVar);
    }
  }
}
module.exports = Square;
