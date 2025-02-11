#!/usr/bin/node

const fs = require('fs');

const filearg = process.argv[2];

fs.readFile(filearg, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
