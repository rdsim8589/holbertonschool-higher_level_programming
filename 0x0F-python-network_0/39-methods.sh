#!/bin/bash
# Display all the allowed HTTP methods
curl -sI $1 | grep Allow: | cut -d':' -f2 | sed -e 's/^[[:space:]]*//'
