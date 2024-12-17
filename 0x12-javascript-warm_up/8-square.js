#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0],10);
let ind = 0;

if (isNaN(num)){
    console.log("Missing size");
} else {
for (ind; ind < args[0]; ind++)
{
    console.log("X".repeat(args[0]));
}
}
