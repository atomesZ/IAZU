#!/bin/bash

ENDPOINT_URI="https://iazu2.cognitiveservices.azure.com/"

MOUNT_DIR="$(pwd)/container_mount_point"


docker run --rm -it -p 5000:5000 \
--memory 4g \
--cpus 2 \
--mount type=bind,src="$MOUNT_DIR/input",target="/input" \
--mount type=bind,src="$MOUNT_DIR/output",target="/output" \
mcr.microsoft.com/azure-cognitive-services/language/luis \
Eula=accept \
Billing=$ENDPOINT_URI \
ApiKey=$API_KEY
