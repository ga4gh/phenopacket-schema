#!/usr/bin/env bash

# Build and Deploy Python Package
# We assume the script is ran from the top-level repository folder as ./deploy-python.sh

DIRECTORY=./python
echo "Building phenopacket distribution files in directory at $DIRECTORY"

# Ensure we generated the protobuf Python files.
./mvnw clean compile

cd $DIRECTORY || { echo "Deployment FAILED. Couldn't find directory" ; exit 1; }
createVirtualEnvironment(){
  echo "Creating Python virtual environment at ${1}"
  python3 -m venv "${1}" &> /dev/null
  if [ $? -ne 0 ]; then
    echo "Setup of Python virtual environment using 'python3 -m venv' failed. Trying 'virtualenv'"
    virtualenv "${1}" &> /dev/null
    if [ $? -ne 0 ]; then
      echo "Deployment FAILED. Could not create Python virtual environment"
      exit 1;
    fi
  fi
  echo "Virtual environment created successfully";
}

# Create Python venv in virtual directory
TEMP_DIRECTORY_VIRTUAL_ENV="phenopackets-venv"
createVirtualEnvironment $TEMP_DIRECTORY_VIRTUAL_ENV
# shellcheck disable=SC1090
source "$TEMP_DIRECTORY_VIRTUAL_ENV/bin/activate"

# Test
python3 -m pip install ".[test]"
pytest || { echo "Deployment FAILED. Unittest Failure" ; exit 1; }

# Install dependencies for building/deploying
python3 -m pip install build twine || { echo "Deployment FAILED. Failed to install python dependencies" ; exit 1; }
# Build
python3 -m build || { echo "Deployment FAILED. Building python package" ; exit 1; }
# Deploy - Remove --repository testpypi flag for production.
if [ "$1" = "release-prod" ]; then
  python3 -m twine upload dist/* || { echo "Deployment FAILED. Could not upload."; exit 1; }
elif [ "$1" = "release-test" ]; then
  python3 -m twine upload --repository testpypi dist/* || { echo "Deployment FAILED. Could not upload."; exit 1; }
else
  echo "Python Release was prepared successfully. No release argument provided, use one of [release-prod, release-test] to make the production/test release."
fi

# Clean up
echo "Cleaning up the build environment and the build files"
deactivate
rm -rf build dist ${TEMP_DIRECTORY_VIRTUAL_ENV}
cd ..
./mvnw clean