#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}

for (let i = 1; i <= arg; i++) {
  console.log('C is fun');
}
