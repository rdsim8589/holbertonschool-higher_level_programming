#!/bin/bash
# sends post request that contains the post request
curl -s "$1" -X POST -H "Content-Type: application/json" -d @$2
