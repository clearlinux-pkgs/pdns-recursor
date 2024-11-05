PKG_NAME := pdns-recursor
URL = https://downloads.powerdns.com/releases/pdns-recursor-5.1.3.tar.bz2
ARCHIVES = $(CGIT_BASE_URL)/vendor/pdns-recursor/snapshot/pdns-recursor-2024-10-03-14-24-15.tar.xz ./vendor $(CGIT_BASE_URL)/vendor/pdns-recursor/snapshot/pdns-recursor-2024-10-03-14-24-15.tar.gz ./vendor

include ../common/Makefile.common
