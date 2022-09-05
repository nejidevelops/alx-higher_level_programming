#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 1; i <= size; i++) {
  let row = '';
  for (let j = 1; j <= size; j++) row += 'X';
  console.log(row);
}
