#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const len = args.lenght;

if (len <= 1) {
    console.log(0);
} else {
    const sortedArgs = args.sort((a,b) => b - a);
    console.log(sortedArgs[1]);
}
