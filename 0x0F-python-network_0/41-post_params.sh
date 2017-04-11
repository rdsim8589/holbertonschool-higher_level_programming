#!/bin/bash
# sends a post request and sets variables. returns the body as response
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $1 
