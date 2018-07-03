Name: monetaryunit-wallet
Version: 1.0.3.2
Release: 1
%undefine _disable_source_fetch
Source: https://github.com/muecoin/MUECore/archive/v%{version}.tar.gz
%define     SHA256SUM0 b1b392688e9036f7bd5be935f386311af6131738a2a52a2681db943ad889ba7c
License: MIT
Summary: Monetary Unit (MUE) wallet
Group: Applications/System
BuildRequires: boost-devel
BuildRequires: libdb4-devel
BuildRequires: libdb4-cxx-devel
BuildRequires: libevent-devel
BuildRequires: miniupnpc-devel
BuildRequires: openssl-devel
BuildRequires: protobuf-devel
BuildRequires: qrencode-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: zeromq-devel

%description
This package provides the Monetary Unit (MUE) wallet with CLI.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.


# subpackage monetaryunit-wallet-qt5
%package qt5
Group: Applications/System
Summary: QT5 GUI for the Monetary Unit (MUE) wallet
%description qt5
This package provides the QT5 GUI to the Monetary Unit (MUE) wallet.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.

# verify checksum of downloaded source
%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -

%setup -n MUECore-%{version}

%build
./autogen.sh
./configure --prefix=/usr --with-gui=qt5
make

%install
%make_install
rm %{buildroot}/usr/lib/libbitcoinconsensus.a
rm %{buildroot}/usr/lib/libbitcoinconsensus.la

%files
/usr/bin/bench_mue
/usr/bin/mue-cli
/usr/bin/mue-tx
/usr/bin/mued
/usr/bin/test_mue
/usr/include/bitcoinconsensus.h
/usr/lib/libbitcoinconsensus.so
/usr/lib/libbitcoinconsensus.so.0
/usr/lib/libbitcoinconsensus.so.0.0.0
/usr/lib/pkgconfig/libbitcoinconsensus.pc

%files qt5
/usr/bin/mue-qt
/usr/bin/test_mue-qt
