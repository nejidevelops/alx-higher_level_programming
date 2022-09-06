#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);
const concat = fileA.toString() + fileB.toString();

fs.writeFileSync(process.argv[4], concat);
