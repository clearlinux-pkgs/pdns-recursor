#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0x6FFC33439B0D04DF (erik.winkels@open-xchange.com)
#
Name     : pdns-recursor
Version  : 5.2.2
Release  : 45
URL      : https://downloads.powerdns.com/releases/pdns-recursor-5.2.2.tar.bz2
Source0  : https://downloads.powerdns.com/releases/pdns-recursor-5.2.2.tar.bz2
Source1  : http://localhost/cgit/vendor/pdns-recursor/snapshot/pdns-recursor-2024-10-03-14-24-15.tar.xz
Source2  : http://localhost/cgit/vendor/pdns-recursor/snapshot/pdns-recursor-2025-04-09-13-19-25.tar.gz
Source3  : https://downloads.powerdns.com/releases/pdns-recursor-5.2.2.tar.bz2.asc
Source4  : 6FFC33439B0D04DF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSL-1.0 GPL-2.0 MIT Unicode-DFS-2016 Unlicense
Requires: pdns-recursor-bin = %{version}-%{release}
Requires: pdns-recursor-license = %{version}-%{release}
Requires: pdns-recursor-man = %{version}-%{release}
Requires: pdns-recursor-services = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : boost-dev
BuildRequires : curl-dev
BuildRequires : file
BuildRequires : gnupg
BuildRequires : libcap-dev
BuildRequires : openssl-dev
BuildRequires : pypi-virtualenv
BuildRequires : ragel
BuildRequires : rustc
BuildRequires : systemd-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PowerDNS Recursor
=================
For full details on building PowerDNS Recursor, please read https://docs.powerdns.com/recursor/appendices/compiling.html

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
Requires: systemd

%description services
services components for the pdns-recursor package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE4}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE3} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 6FFC33439B0D04DF' gpg.status
%setup -q -n pdns-recursor-5.2.2
cd %{_builddir}
tar xf %{_sourcedir}/pdns-recursor-2024-10-03-14-24-15.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/pdns-recursor-2025-04-09-13-19-25.tar.gz
cd %{_builddir}/pdns-recursor-5.2.2
mkdir -p ./vendor
cp -r %{_builddir}/pdns-recursor-2024-10-03-14-24-15/. %{_builddir}/pdns-recursor-5.2.2/./vendor
mkdir -p ./vendor
cp -r %{_builddir}/pdns-recursor-2025-04-09-13-19-25/. %{_builddir}/pdns-recursor-5.2.2/./vendor
mkdir -p .cargo
echo '
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
' >> .cargo/config.toml
pushd ..
cp -a pdns-recursor-5.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744205687
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --with-luajit \
--enable-reproducible \
--enable-unit-tests \
--enable-valgrind \
--enable-systemd \
--with-socketdir=/run
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static --with-luajit \
--enable-reproducible \
--enable-unit-tests \
--enable-valgrind \
--enable-systemd \
--with-socketdir=/run
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744205687
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pdns-recursor
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxx-build/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxx-build/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxx/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxx/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxxbridge-flags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxxbridge-flags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxxbridge-macro/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/cxxbridge-macro/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/equivalent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/equivalent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/c371f0a7cbb203643d88566665a452f96bf1ab86 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/hashbrown/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/hashbrown/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/c9c1c33aee599ebfdfb0bc2aed9ea082d9e3173a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/indexmap/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/indexmap/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/7e5936a6fa3cf3518c01cec41345adf27399fe12 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/ipnet/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/bb92c62835916e922667b4fe181beed0e6efca91 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/ipnet/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/4f8ab673f6e2ae6c7bb2910d7f38838c18c12178 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/itoa/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/itoa/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/link-cplusplus/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/link-cplusplus/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/ryu/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/ryu/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/pdns-recursor/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/scratch/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/scratch/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde_yaml/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/serde_yaml/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/termcolor/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/termcolor/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/termcolor/UNLICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pdns-recursor/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-width/COPYRIGHT %{buildroot}/usr/share/package-licenses/pdns-recursor/5ed53061419caf64f84d064f3641392a2a10fa7f || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-width/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unicode-width/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/unsafe-libyaml/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/winapi-util/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/winapi-util/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/winapi-util/UNLICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows-sys/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows-sys/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2024-10-03-14-24-15/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxx-build/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxx-build/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxx/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxx/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxxbridge-flags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxxbridge-flags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxxbridge-macro/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/cxxbridge-macro/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/equivalent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/equivalent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/c371f0a7cbb203643d88566665a452f96bf1ab86 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/hashbrown/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/hashbrown/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/c9c1c33aee599ebfdfb0bc2aed9ea082d9e3173a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/indexmap/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/indexmap/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/7e5936a6fa3cf3518c01cec41345adf27399fe12 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/ipnet/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/bb92c62835916e922667b4fe181beed0e6efca91 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/ipnet/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/4f8ab673f6e2ae6c7bb2910d7f38838c18c12178 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/itoa/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/itoa/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/link-cplusplus/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/link-cplusplus/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/ryu/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/ryu/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/pdns-recursor/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/scratch/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/scratch/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde_yaml/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/serde_yaml/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/shlex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/a97a2888bca904918b3b9ec008fde1d6e9905a6d || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/shlex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/termcolor/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/termcolor/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/termcolor/UNLICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pdns-recursor/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-width/COPYRIGHT %{buildroot}/usr/share/package-licenses/pdns-recursor/5ed53061419caf64f84d064f3641392a2a10fa7f || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-width/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unicode-width/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/unsafe-libyaml/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/winapi-util/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/winapi-util/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pdns-recursor/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/winapi-util/UNLICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows-sys/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows-sys/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pdns-recursor-2025-04-09-13-19-25/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pdns-recursor-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pdns-recursor/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/pdns-recursor-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/pdns-recursor/b0546213f9970e01098f0ec919c828d83790eb9a || :
cp %{_builddir}/pdns-recursor-%{version}/ext/json11/LICENSE.txt %{buildroot}/usr/share/package-licenses/pdns-recursor/d40d61b8fa8ecae46da12bd1fce4162af02cff8c || :
cp %{_builddir}/pdns-recursor-%{version}/ext/yahttp/LICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/cd4a6679c43eb8c0331ebc91648b27b6fd747252 || :
cp %{_builddir}/pdns-recursor-%{version}/html/LICENSE %{buildroot}/usr/share/package-licenses/pdns-recursor/23a1f87d806ce0330b3d85485e399a5f9f553409 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pdns_recursor
/V3/usr/bin/rec_control
/usr/bin/pdns_recursor
/usr/bin/rec_control

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pdns-recursor/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/pdns-recursor/23a1f87d806ce0330b3d85485e399a5f9f553409
/usr/share/package-licenses/pdns-recursor/2ad1215c12bd0a3492399dc438aa63084323c662
/usr/share/package-licenses/pdns-recursor/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pdns-recursor/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/pdns-recursor/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/pdns-recursor/4f8ab673f6e2ae6c7bb2910d7f38838c18c12178
/usr/share/package-licenses/pdns-recursor/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pdns-recursor/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pdns-recursor/5ed53061419caf64f84d064f3641392a2a10fa7f
/usr/share/package-licenses/pdns-recursor/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pdns-recursor/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6
/usr/share/package-licenses/pdns-recursor/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/pdns-recursor/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pdns-recursor/7e5936a6fa3cf3518c01cec41345adf27399fe12
/usr/share/package-licenses/pdns-recursor/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/pdns-recursor/a97a2888bca904918b3b9ec008fde1d6e9905a6d
/usr/share/package-licenses/pdns-recursor/b0546213f9970e01098f0ec919c828d83790eb9a
/usr/share/package-licenses/pdns-recursor/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/pdns-recursor/bb92c62835916e922667b4fe181beed0e6efca91
/usr/share/package-licenses/pdns-recursor/c371f0a7cbb203643d88566665a452f96bf1ab86
/usr/share/package-licenses/pdns-recursor/c9c1c33aee599ebfdfb0bc2aed9ea082d9e3173a
/usr/share/package-licenses/pdns-recursor/cd4a6679c43eb8c0331ebc91648b27b6fd747252
/usr/share/package-licenses/pdns-recursor/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pdns-recursor/d40d61b8fa8ecae46da12bd1fce4162af02cff8c
/usr/share/package-licenses/pdns-recursor/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/pdns-recursor/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pdns_recursor.1
/usr/share/man/man1/rec_control.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/pdns-recursor.service
/usr/lib/systemd/system/pdns-recursor@.service
