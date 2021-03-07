#!bin/bash

curl  localhost:8081/Job/Test/buildWithParameters \
      --user USER:TOKEN \
      --data id=123 --data verbosity=high
