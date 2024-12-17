#!/usr/bin/node

function factorial(num) {
    if (num <= 0 || isNaN(num))
        return 1;

    return num * factorial(num - 1);
}

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
console.log(factorial(num));
