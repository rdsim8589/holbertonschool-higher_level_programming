#!/bin/bash
#script size of a body response
curl -Is $1 | grep Content-Length |cut -d' ' -f2
