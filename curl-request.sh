#!bin/bash

curl  localhost:8080/Job/Test1/buildWithParameters \
      --user USER:TOKEN \
      --data id=123 --data verbosity=high
