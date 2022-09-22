#!/bin/bash
# takes in a URL as an argument, sends a GET request to URL displays the body of the response
curl -s -H "X-School-User-Id: 98" $1
