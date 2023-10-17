#!/usr/bin/node
/**
 * Square class inherits from Square
 */
const Psquare = require('./5-square');

class Square extends Psquare {
  charPrint (x) {
    const myCh = c === undefined ? 'X' : c;
    for (let x = 0; x < this.height; x++) {
      let my Var = '';
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
