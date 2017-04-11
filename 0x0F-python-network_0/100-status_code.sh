#!/bin/bash
# get the status code with curl
curl -s -o /dev/null -w %{http_code} $1
