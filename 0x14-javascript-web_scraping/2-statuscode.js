#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
