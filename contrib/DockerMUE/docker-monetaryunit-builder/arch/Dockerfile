FROM archlinux/base

ENV DISTRO "arch"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"
ENV MUE_URL "https://github.com/muecoin/MUECore.git"
ENV MUE_VERSION "1.0.3.2"

## update pacman and create normal user for package build
RUN pacman -Syu --noconfirm && \
## install dependencies
    pacman -S --noconfirm base-devel \
                    boost \
                    git \
                    libevent \
                    miniupnpc \
                    protobuf \
                    qrencode \
                    qt5-base \
                    qt5-tools \
                    tar \
                    wget \
                    zeromq

# create build user and set up the package build environment
RUN mkdir $TOP_DIR && \
    groupadd -g 1000 build && \
    useradd -g build -m -d $DISTRO_DIR -s /bin/bash -c "Build user" build && \
    echo 'build ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    # run one job less than the number of available CPUs concurrently
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    sed -i -e "s;#MAKEFLAGS=.*;MAKEFLAGS=\"-j${BUILDJOBS}\";" /etc/makepkg.conf && \
    # Set path for built packages
    sed -i -e "s;#PKGDEST=.*;PKGDEST=$TOP_DIR/$DISTRO;" /etc/makepkg.conf && \
    mkdir $DISTRO_DIR/pkgbuilds && \
    chown -R build:build $DISTRO_DIR

# Install Yaourt
RUN su -c "git clone https://aur.archlinux.org/package-query.git && \
          cd package-query && \
          makepkg -si --noconfirm && \
          cd .. && \
          git clone https://aur.archlinux.org/yaourt.git && \
          cd yaourt && \
          makepkg -si --noconfirm && \
          cd .." - build && \
# Set path for built packages
    sed -i -e "s;#EXPORT=0\(.*\);EXPORT=1\1;" /etc/yaourtrc

COPY PKGBUILD $DISTRO_DIR/pkgbuilds

# build libdb-dev v4.8 from source and install it
RUN su -c "yaourt -Sy --noconfirm db4.8" - build

# build the packages from PKGBUILD
RUN su -c "cd $DISTRO_DIR/pkgbuilds && \
          makepkg -si --noconfirm" - build

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh", "arch", "pkg.tar.xz" ]
