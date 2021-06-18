#!/bin/bash

docker build -t iazu2.azurecr.io/src_iazu_server . && docker push iazu2.azurecr.io/src_iazu_server
