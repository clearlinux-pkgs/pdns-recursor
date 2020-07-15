#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6FFC33439B0D04DF (erik.winkels@open-xchange.com)
#
Name     : pdns-recursor
Version  : 4.1.17
Release  : 14
URL      : https://downloads.powerdns.com/releases/pdns-recursor-4.1.17.tar.bz2
Source0  : https://downloads.powerdns.com/releases/pdns-recursor-4.1.17.tar.bz2
Source1  : https://downloads.powerdns.com/releases/pdns-recursor-4.1.17.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: pdns-recursor-bin = %{version}-%{release}
Requires: pdns-recursor-license = %{version}-%{release}
Requires: pdns-recursor-man = %{version}-%{release}
Requires: pdns-recursor-services = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : boost-dev
BuildRequires : curl-dev
BuildRequires : openssl-dev
BuildRequires : protobuf-dev
BuildRequires : ragel
BuildRequires : systemd-dev
BuildRequires : valgrind
BuildRequires : virtualenv
Patch1: 0001-Replace-boost-s-placeholders-with-the-ones-from-the-.patch
Patch2: 0002-Update-boost.m4.patch

%description
PowerDNS Recursor
-----------------
For full details, please read https://doc.powerdns.com/md/recursor/

%package bin
Summary: bin components for the pdns-recursor package.
Group: Binaries
Requires: pdns-recursor-license = %{version}-%{release}
Requires: pdns-recursor-services = %{version}-%{release}

%description bin
bin components for the pdns-recursor package.


%package license
Summary: license components for the pdns-recursor package.
Group: Default

%description license
license components for the pdns-recursor package.


%package man
Summary: man components for the pdns-recursor package.
Group: Default

%description man
man components for the pdns-recursor package.


%package services
Summary: services components for the pdns-recursor package.
Group: Systemd services

%description services
services components for the pdns-recursor package.


%prep
%setup -q -n pdns-recursor-4.1.17
cd %{_builddir}/pdns-recursor-4.1.17
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594774673
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static --with-luajit \
--enable-reproducible \
--enable-unit-tests \
--enable-valgrind \
--enable-systemd \
--with-socketdir=/run
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1594774673
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pdns-recursor
cp %{_builddir}/pdns-recursor-4.1.17/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/pdns-recursor-4.1.17/NOTICE %{buildroot}/usr/share/package-licenses/pdns-recursor/b0546213f9970e01098f0ec919c828d83790eb9a
cp %{_builddir}/pdns-recursor-4.1.17/ext/json11/LICENSE.txt %{buildroot}/usr/share/package-licenses/pdns-recursor/d40d61b8fa8ecae46da12bd1fce4162af02cff8c
cp %{_builddir}/pdns-recursor-4.1.17/ext/yahttp/LICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/cd4a6679c43eb8c0331ebc91648b27b6fd747252
cp %{_builddir}/pdns-recursor-4.1.17/html/LICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/23a1f87d806ce0330b3d85485e399a5f9f553409
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pdns_recursor
/usr/bin/rec_control

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pdns-recursor/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/pdns-recursor/23a1f87d806ce0330b3d85485e399a5f9f553409
/usr/share/package-licenses/pdns-recursor/b0546213f9970e01098f0ec919c828d83790eb9a
/usr/share/package-licenses/pdns-recursor/cd4a6679c43eb8c0331ebc91648b27b6fd747252
/usr/share/package-licenses/pdns-recursor/d40d61b8fa8ecae46da12bd1fce4162af02cff8c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pdns_recursor.1
/usr/share/man/man1/rec_control.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/pdns-recursor.service
/usr/lib/systemd/system/pdns-recursor@.service
