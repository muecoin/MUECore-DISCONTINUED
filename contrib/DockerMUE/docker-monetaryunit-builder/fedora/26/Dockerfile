FROM fedora:26

ENV DISTRO "fedora26"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"

# update dnf, install EPEL repo and the packages required to build the wallet
RUN dnf -y update && \
    dnf -y upgrade && \
    dnf -y install autoconf \
										automake \
										binutils \
										bison \
										boost-devel \
										flex \
										gcc \
										gcc-c++ \
										gettext \
										libdb4-cxx-devel \
										libdb4-devel \
										libevent-devel \
										libtool \
										make \
										miniupnpc-devel \
										openssl-devel \
										patch \
										pkgconfig \
										protobuf-devel \
										qrencode-devel \
										qt5-qtbase-devel \
										qt5-qttools-devel \
										redhat-rpm-config \
										rpm-build \
										rpm-sign \
										rpmdevtools \
										zeromq-devel

# create build user and set up the package build environment
RUN mkdir $TOP_DIR && \
    groupadd -g 1000 build && \
    useradd -g build -m -d $DISTRO_DIR -s /bin/bash -c "Build user" build && \
    su -c 'rpmdev-setuptree' - build && \
    # run one job less than the number of available CPUs concurrently
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    echo "%__make     /usr/bin/make -j${BUILDJOBS}" >> /etc/rpm/macros

# copy the spec file to the Docker image
COPY monetaryunit-wallet.spec $DISTRO_DIR/rpmbuild/SPECS/

# build MUE packages from .spec file
RUN su -c "rpmbuild -ba $DISTRO_DIR/rpmbuild/SPECS/monetaryunit-wallet.spec" - build

# move monetaryunit-wallet-*.rpm to $DISTRO_DIR where they can be picked up by /copy_packages.sh
RUN find $DISTRO_DIR/rpmbuild/ -name 'monetaryunit-wallet-*.rpm' -exec mv {} $DISTRO_DIR \;

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh" ]
