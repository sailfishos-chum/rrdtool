# This SPEC is based on repoforge implementation from
# https://github.com/repoforge/rpms/blob/master/specs/rrdtool/rrdtool.spec
#
# Here, selection of options was made to suit Sailfish package
#
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.7.2
Release: 3%{?dist}
License: GPL
Group: Applications/Databases
URL: http://www.rrdtool.org/

Source0: http://oss.oetiker.ch/rrdtool/pub/rrdtool-%{version}.tar.gz

BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: glib2-devel
# BuildRequires: gettext-devel
#BuildRequires: groff
#BuildRequires: intltool
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
# BuildRequires: lua-devel
# BuildRequires: openssl-devel
BuildRequires: pango-devel
# BuildRequires: python-devel >= 2.3
# BuildRequires: ruby
# BuildRequires: ruby-devel
# BuildRequires: tcl-devel
# BuildRequires: tk-devel
BuildRequires: zlib-devel
Requires: cairo
# Requires: gettext
Requires: glib2
Requires: libxml2
# Requires: lua
# Requires: openssl
# Requires: perl
Requires: pango
# Requires: python
# Requires: ruby
# Requires: xorg-x11-fonts-Type1
Requires: zlib

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

PackageName: RRDtool
Type: console-application
Custom:
  Repo: https://github.com/oetiker/rrdtool-1.x
Categories:
  - Utility
  - Graphics
  - Science
Icon: https://upload.wikimedia.org/wikipedia/commons/7/7b/Rrdtool-3dlogo.png
Screenshots:
  - https://oss.oetiker.ch/rrdtool/gallery/sma_inverter.png
  - https://upload.wikimedia.org/wikipedia/commons/7/76/Rrddemo.png

%package devel
Summary: RRDtool static libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to use directly this library.

PackageName: RRDtool Development
Type: console-application
Custom:
  Repo: https://github.com/oetiker/rrdtool-1.x
Categories:
  - Library
  - Graphics
  - Science
Icon: https://upload.wikimedia.org/wikipedia/commons/7/7b/Rrdtool-3dlogo.png

%prep
%setup -q -n %{name}-%{version}/rrdtool

%build
%configure \
    --disable-docs \
    --disable-perl \
    --disable-rrdcached \
    --disable-rrdcgi \
    --disable-examples \
    --disable-python \
    --disable-nls \
    --disable-ruby \
    --disable-lua \
    --disable-tcl

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

#%{__install} -Dp -m0755 ../rrd-sync %{buildroot}%{_bindir}/rrd-sync

find %{buildroot} -name .packlist -exec %{__rm} {} \;

# remove man pages
%{__rm} -f %{buildroot}%{_mandir}/man1/*.1*
%{__rm} -f %{buildroot}%{_mandir}/man3/librrd.3*

# remove docs
%{__rm} -rf %{buildroot}%{_datadir}/doc/rrdtool*

# remove services if installed
%{__rm} -f %{buildroot}%{_unitdir}/rrd*.socket || true
%{__rm} -f %{buildroot}%{_unitdir}/rrd*.service || true

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n rrdtool -p /sbin/ldconfig

%postun -n rrdtool -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
#%doc CHANGES CONTRIBUTORS COPYRIGHT LICENSE NEWS THREADS TODO VERSION
%{_bindir}/rrdtool
%{_bindir}/rrdupdate
%{_bindir}/rrdcreate
%{_bindir}/rrdinfo
%{_libdir}/librrd.so.*
#%{_bindir}/rrd-sync

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rrd.h
%{_includedir}/rrd_client.h
%{_includedir}/rrd_format.h
%{_libdir}/librrd.a
%{_libdir}/librrd.so
%{_libdir}/pkgconfig/librrd.pc
%exclude %{_libdir}/librrd.la

%changelog
