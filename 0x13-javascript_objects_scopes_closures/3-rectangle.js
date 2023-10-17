#!/usr/bin/node
/*
 * Rectangle class and checking parameters
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    for (let x = 0 < this.height; x++) {
      let myVar = '';
      let b = 0;
      while (b < this.width) {
        myVar += 'X';
	b++
      }
      console.log(myVar);
    }
  }
}	
module.exports = Rectangle;
