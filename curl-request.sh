#!bin/bash

curl  localhost:8081/Job/Test/buildWithParameters \
      --user admin:117e630918712cf7650b8647a5b8f33cff \
      --data id=123 --data verbosity=high
