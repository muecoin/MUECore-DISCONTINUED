FROM ubuntu:16.04

ENV DISTRO "ubuntu1604"
ENV DISTROCODE "ubuntu_xenial"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"
ENV BDB_SRCDIR "$DISTRO_DIR/bdb/src"
ENV BDB_TGTDIR "$DISTRO_DIR/bdb/build"
ENV BDB_VERSION "4.8.30"
ENV BDB_URL "http://download.oracle.com/berkeley-db/db-$BDB_VERSION.tar.gz"
ENV MUE_SRCDIR "$DISTRO_DIR/mue/src"
ENV MUE_CLI_TGTDIR "$DISTRO_DIR/mue/build"
ENV MUE_GUI_TGTDIR "$DISTRO_DIR/mue/build-gui"
ENV MUE_URL "https://github.com/muecoin/MUECore.git"
ENV MUE_VERSION "1.0.3.2"

COPY mue_cli_control /tmp
COPY mue_qt5_control /tmp

# update apt
RUN apt -q update && \
# install dependencies
    apt -qy install autoconf \
                   	bsdmainutils \
                    build-essential \
                    gawk \
                    gettext \
                    git \
                    libboost-all-dev \
                    libdb-dev \
                    libevent-dev \
                    libminiupnpc-dev \
                    libprotobuf-dev \
                    libqrencode-dev \
                    libssl-dev \
                    libtool \
                    libzmq3-dev \
                    libzmq5 \
                    lcov \
                    pkg-config \
                    protobuf-compiler \
                    qtbase5-dev \
                    qttools5-dev-tools \
                    wget

# create all the dirs
RUN for i in $DISTRO_DIR $BDB_SRCDIR $BDB_TGTDIR $MUE_SRCDIR $MUE_CLI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/usr/bin; do mkdir -p ${i}; done

# build libdb-dev v4.8 from source and install it in /tmp/db-$BDB_VERSION-build
RUN wget -qO $BDB_SRCDIR/db.tar.gz $BDB_URL && \
    cd $BDB_SRCDIR && \
    tar xzf db.tar.gz && \
    cd $BDB_SRCDIR/db-$BDB_VERSION/build_unix && \
    mkdir -p $BDB_TGTDIR && \
    ../dist/configure --disable-shared --enable-cxx --with-pic --prefix=$BDB_TGTDIR && \
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    make -j${BUILDJOBS} && \
    make install

# clone the git repo
RUN git clone $MUE_URL $MUE_SRCDIR

# build MUECore with QT5 GUI from Github sources
RUN cd $MUE_SRCDIR && \
    sh ./autogen.sh && \
    ./configure --prefix=/usr --with-gui=qt5 CPPFLAGS="-I$BDB_TGTDIR/include -O2" LDFLAGS="-L$BDB_TGTDIR/lib" && \
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    make -j${BUILDJOBS} && \
    make DESTDIR=$MUE_CLI_TGTDIR install && \
    strip $MUE_CLI_TGTDIR/usr/bin/* && \
    # move gui files to separate dir
    mv $MUE_CLI_TGTDIR/usr/bin/*qt $MUE_GUI_TGTDIR/usr/bin/

# create .deb from newly compiled MUE wallet files
RUN mv /tmp/mue_cli_control $MUE_CLI_TGTDIR/DEBIAN/control && \
    mv /tmp/mue_qt5_control $MUE_GUI_TGTDIR/DEBIAN/control && \
    cd $DISTRO_DIR && \
    dpkg-deb --build $MUE_CLI_TGTDIR monetaryunit-wallet-$MUE_VERSION-$DISTROCODE-amd64.deb && \
    dpkg-deb --build $MUE_GUI_TGTDIR monetaryunit-wallet-qt5-$MUE_VERSION-$DISTROCODE-amd64.deb

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh" ]
