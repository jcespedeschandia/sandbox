//Level 1
//1.
var x = 5; 
console.log(x);

//2.
var x = 3;
x = x + 1;
console.log(x);

//3.
var x = 3;
x = x + 2;
console.log(x+2);
console.log(x);

//4.
var x = 3;
x = x*x;
console.log(x);
console.log(x*2);

//5.
var x = 2;
var y = 5;
var z = x + y;
console.log(z);

// Level 2
//1.
var x = [1,2,4];
console.log(x);

//2.
var x = [1,3,5];
console.log(x[0]);

//3.
var x = [2,4,6];
console.log(x[1]);

//4.
var x = [1,3,5];
console.log(x[2]);

//5.
var x = [1.3];
console.log(x[0]);

//6.
var x = [1,2,4];
x[0] = x[1];
console.log(x);

//7.
var x = [1,3,5];
var y = x.length;
console.log(y);

//8.
var x = [2,4,6,3,7];
var y = x.length - 2;
console.log(y);

//9.
var x = [2,4,6,3,7];
var y = x.length;
console.log(x[y-1]);

//10.
var x = [1,3,5,7];
x[0] = x[x.length -2];
console.log(x);

//11.
var x = [1,3,5,7];
x[x.length - 3] = x[x.length /2 + x.length/4];
console.log(x);

//12.
var x = [1,3,5,7];
var y = [2,4,6];
x[2] = y[x.length - 3];
console.log(x);

//13.
var x = [1,3,5,7];
var y = [2,4,6];
x[2] = y[x.length-3] + x[x[0] + y[0]];
console.log(x);
