# scheduled-tweet
This code uses ibm cloud as functions platform.

## create virtualenv folder
`docker run --rm -v "$PWD:/tmp" ibmfunctions/action-python-v3.7 bash -c "cd /tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
`

## setup ibmcloud info
```
ibmcloud login
ibmcloud target -g <resource name> -r <region name>
ibmcloud fn namespace create <your namespace>
ibmcloud fn namespace target <your namespace>
```

## zipping
`zip -r scheduled-tweet.zip virtualenv __main__.py`

## deployment

`ibmcloud fn action create scheduled-tweet scheduled-tweet.zip --kind python:3.7`
