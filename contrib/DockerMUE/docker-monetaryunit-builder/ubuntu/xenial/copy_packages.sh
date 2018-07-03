#!/bin/bash

DISTRO="ubuntu1604"
PKGEXT="deb"

mkdir -p /packages/${DISTRO} && echo "created /packages/${DISTRO}" || echo "failed to create created /packages/${DISTRO}"

if [ -d /packages/${DISTRO} ]
then
  mv $DISTRO_DIR/*.${PKGEXT} /packages/${DISTRO} && echo "moved *.${PKGEXT} to /packages/${DISTRO}" || echo "failed to move *.${PKGEXT} to /packages/${DISTRO}"
fi

ls -l /packages/${DISTRO}/*.${PKGEXT} 2>/dev/null

exit $?
