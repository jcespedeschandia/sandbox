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

// Level 3
//1.
var x = [1,3,5];
x[0] = x[2];
x[1] = x[0];
console.log(x);

//2.
var x = [1,3,5];
var y = [0,5,7];
x[0] = x[1] + y[2];
y[1] = y[2] - x[0]; 
console.log(x);

//3.
var x = [1,3,5,8];
x[0] = x[x.length - 1]; 
console.log(x); 

//4.
var x = [1,3,5,8]; 
var temp = x[x.length -1]; 
x[x.length - 1] = x[0]; 
console.log(x); 

//5.
var x = [1,3,5,8]; 
var temp = x[x.length - 1]; 
x[x.length -1] = x[0]; 
x[0] = temp; 
console.log(x);

//6.
var x = [1,3,5,8]; 
x.pop(); 
x.push(7); 
console.log(x); 

//7.
var x = [1,3,5];
x[0] = 15;
x[3] = 77;
console.log(x);

//8.
var x = [1,3,5,8,2,-5,-8]; 
x[0] = x[x.length - 1]; 
x[x.length -1] = x[0]; 
console.log(x); 

//9.
var x = [1,3,5,8,2,-5,-8]; 
var temp = x[0]; 
x[0] = x[x.length -1];
x[x.length-1] = temp; 
console.log(x);

//10.
var x = [1,3,5]; 
x.push(7); 
console.log(x);

//11.
var x = [2,4,6]; 
x.push(3); 
console.log(x);

//12.
var x = [1,3,5]; 
var y = x[0] + x[1]; 
x.push(y); 
console.log(x); 

//13.
var x = [2,3,5]; 
x.push(x[0] + x[1]); 
console.log(x);

//14.
var x = [1,3,5];
x.pop(); 
console.log(x);

//15.
var x = [1,3,5]; 
x.push(2);
x.pop();
console.log(x);

// Level 4
//1.
var counter = 1;
    if (counter == 1){
        console.log("hello");
    }

//2.
var counter = 1;
if (counter == 1){
    console.log("hello");
}
else if (counter == 2){
    console.log("world");
}

//3.
var counter = 2;
if (counter < 10){
    console.log("less than 10");
}
else {
    console.log("greater or equal to 10"); 
}

//4.
var counter = 1; 
if (counter == 5){
    console.log("coding");
}
else {
    console.log("dojo");
}

//5.
var x = [2,4,5]; 
var counter = 0;
if (x[counter] < 5){
    console.log("coding");
}
else{
    console.log("dojo");
}

//6.
var x = [2,4,5]; 
var counter = 2;

if (x[counter] > 10){
    console.log("coding");
}
else{
    console.log("dojo");
}

//7.
var x = [2,4,5];
var counter = 0;

if (x[counter] > 0){
    console.log("coding");
    counter = counter + 1;
}
console.log(x[counter]); 


//8.
var x = [2,4,5];
var counter = 0; 

if (x[counter] > 0){
    console.log("coding");
    counter = counter + 1;
}

if (x[counter] > 0){
    console.log("coding");
    counter = counter + 1;
}

if (x[counter] > 0){
    console.log("coding");
    counter = counter + 1;
}

console.log(x);
console.log(counter);

// Level 5
//1.
for (var i=0; i<10; i++){
    console.log(i);
}

//2.
var x = 1;

for (var i=0; i<3; i++){
    x = x+1;
}
console.log(x);

//3.
var x = 1;
for (var i=0; i<3; i++){
    x = x + 1; 
}
console.log(x);
console.log(i);

//4.
var x = 1; 
var i = 0; 

for (var i=0; i<-1; i++){
    x = x + 1;
}
console.log(x);

//5.
var x = [];

for (var i=0; i<10; i++){
    x.push(i*2);
}
console.log(x);

//6.
var x = [1,3,5,8]; 

for (var i=0; i < x.length; i++){
    if (x[i] > 4){
        x[i] = 0;
    }
}
console.log(x);

//7.
var x = [-1,3,2,7]; 

for (var i=0; i<x.length; i++){
    if (x[i] < i){
        x[i] = -10
    }
}
console.log(x);

//8.
for (var i=20; i!=10; i--){

    console.log(i);
}

//9.
var x = 0;

for (var i=1; i<4; i++){
    x += i
    console.log(x);
    console.log(i);
}

//10.
var x = 0; 

for (var i=1; i<4; i=i+2){
    x += i; 
    console.log(x);
    console.log(i);
}
