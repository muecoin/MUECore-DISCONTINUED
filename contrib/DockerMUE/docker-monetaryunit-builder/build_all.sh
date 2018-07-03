#!/bin/bash

docker volume create --name monetaryunit_packages &&
for i in $(find -name 'Dockerfile')
do
  _DIRNAME=$(dirname ${i})
  _DISTRO=$(grep " DISTRO " ${i} | cut -f2 -d\")
  cd ${_DIRNAME}
  docker build -t mue:${_DISTRO} . &&
  docker run -v monetaryunit_packages:/packages mue:${_DISTRO}
  cd -
done

exit $?
