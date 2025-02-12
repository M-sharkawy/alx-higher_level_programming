#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const completedTasks = {};

  body.forEach(tasks => {
    if (tasks.completed) {
      if (completedTasks[tasks.userId]) {
        completedTasks[tasks.userId]++;
      } else {
        completedTasks[tasks.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
