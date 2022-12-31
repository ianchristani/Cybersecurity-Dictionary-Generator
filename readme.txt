The Dictionay Generator was builded using FastAPI and it builds an password list based in informations provided (from 1 up to 3) to use in PENTESTS.
Please remember:

1. special characters are already included as options
2. social engineering is very welcomed to provide the infos

the Body request should be:
{
  "info1": "informationProvided1-MANDATORY",
  "info2": "informationProvided2-Optional",
  "info3": "informationProvided3-Optional"
}


It is deployed on AWS
API: http://52.90.75.139/
endpoint: http://52.90.75.139/dictgen
doc: http://52.90.75.139/docs
