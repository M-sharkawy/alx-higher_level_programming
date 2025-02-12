#!/usr/bin/node

const request = require('request');

const charactersId = 18;
const url = process.argv[2];

request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  let count = 0;
  body.results.forEach(film => {
    if (film.characters && film.characters.some(url => url.includes(`/people/${charactersId}/`))) {
      count++;
    }
  });

  console.log(count);
});
