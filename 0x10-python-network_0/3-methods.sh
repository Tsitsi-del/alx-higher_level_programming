#!/bin/bash
#display HTTP methods the server of given URL
CURL -Si "$1" | grep "Allow" | cut -d " " -f 2-
