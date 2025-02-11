#!/usr/bin/node

const fs = require('fs');

const filearg = process.argv[2];
const TextToWrite = process.argv[3];

fs.writeFile(filearg, TextToWrite, (err) => {
  if (err) {
    console.error(err);
  }
});
