#!/usr/bin/node

const fs = require('fs');
const request = require(`request`)

const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, { json: true }, (err, res, body) => {
    if (err) {
        console.error(err);
        return;
    }

    fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
        console.error(err);
    }
    });
});
