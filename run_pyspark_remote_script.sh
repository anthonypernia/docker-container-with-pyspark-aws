#!/bin/bash

## validate if the script name is provided as an argument
if [[ -z "$1" ]]; then
  echo "Use: $0 <script_name>"
  echo "Please provide the name of the Python file you want to run."
  exit 1
fi

SCRIPT_NAME="$1"
LOCAL_PATH="$(pwd)/$SCRIPT_NAME"
CONTAINER_NAME="glue_jupyter_lab"  # container name
CONTAINER_PATH="/home/glue_user/workspace/$SCRIPT_NAME"

# validate if the file exists in the shared volume
if [[ ! -f "$LOCAL_PATH" ]]; then
  echo "Error: The file '$LOCAL_PATH' does not exist in the current directory ($(pwd))."
  exit 1
fi


# verifies if the container is running
if ! docker ps --format '{{.Names}}' | grep -q "^$CONTAINER_NAME$"; then
  echo "Error: The container '$CONTAINER_NAME' is not running."
  echo "Be sure to start the container before running this script."
  exit 1
fi

# execute the script in the container
echo "Executing the file '$SCRIPT_NAME' in the container '$CONTAINER_NAME'..."
if docker exec -it "$CONTAINER_NAME" python3 "$CONTAINER_PATH"; then
  echo "The script '$SCRIPT_NAME' was executed successfully in the container."
else
  echo "Error: The script '$SCRIPT_NAME' failed to execute in the container."
  exit 1
fi
