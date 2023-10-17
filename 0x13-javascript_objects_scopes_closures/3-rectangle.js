#!/usr/bin/node
/**
 * Rectangle class and check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      let b = 0;
      while (b < this.width) {
        myVar += 'X';
        b++;
      }

      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
