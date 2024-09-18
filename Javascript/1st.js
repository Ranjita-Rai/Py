// console.log("Hello World");

// arithmetic operation
// let a=10;
// let b=20;
// let c=a+b;
// console.log(c);

// console.log("Hello");
// console.loggg("Hello");



// // Avoid
// const code = 'console.log("Hello, world!")';
// eval(code); // "Hello, world!"
// // Use safer alternatives
// const func = new Function('console.log("Hello, world!")');
// func(); // "Hello, world!"


// function createUser(name, role) {
//     return {
//     name,
//     role,
//     sayHello() {
//     console.log(`Hello, my name is ${this.name} and I am a ${this.role}`);
//     },  //Using this keyword for calling the value (call by value)
//     };
//     }
//     const admin = createUser('Alice', 'admin');
//     const user = createUser('Bob', 'user');
//     admin.sayHello(); // "Hello, my name is Alice and I am an admin"
//     user.sayHello(); // "Hello, my name is Bob and I am a user"