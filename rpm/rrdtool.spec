# This SPEC is based on repoforge implementation from
# https://github.com/repoforge/rpms/blob/master/specs/rrdtool/rrdtool.spec
#
# Here, selection of options was made to suit Sailfish package
#
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.5.6
Release: 3%{?dist}
License: GPL
Group: Applications/Databases
URL: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/

Source0: http://oss.oetiker.ch/rrdtool/pub/rrdtool-%{version}.tar.gz

BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: glib2-devel
# BuildRequires: gettext-devel
BuildRequires: groff
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
# %{!?_without_xulrunner:BuildRequires: xulrunner-devel}
BuildRequires: zlib-devel
BuildRequires: curl tar
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

%package devel
Summary: RRDtool static libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to use directly this library.

# %package -n perl-rrdtool
# Summary: Perl RRDtool bindings
# Group: Development/Languages
# Requires: %{name} = %{version}
# Obsoletes: rrdtool-perl <= %{version}-%{release}
# Provides: rrdtool-perl = %{version}-%{release}

# %description -n perl-rrdtool
# The Perl RRDtool bindings

# %package -n tcl-rrdtool
# Summary: TCL bindings
# Group: Development/Languages
# Requires: %{name} = %{version}
# Obsoletes: rrdtool-tcl <= %{version}-%{release}
# Provides: rrdtool-tcl = %{version}-%{release}

# %description -n tcl-rrdtool
# The TCL RRDtool bindings

# %package -n python-rrdtool
# Summary: Python RRDtool bindings
# Group: Development/Languages
# BuildRequires: python
# Requires: python >= %{python_version}
# Requires: %{name} = %{version}
# Obsoletes: rrdtool-python <= %{version}-%{release}
# Provides: rrdtool-python = %{version}-%{release}

# %description -n python-rrdtool
# Python RRDtool bindings.

# %package -n ruby-rrdtool
# Summary: RRDtool module for Ruby
# Group: Development/Languages
# Requires: %{name} = %{version}, ruby-devel
# Obsoletes: rrdtool-ruby <= %{version}-%{release}
# Provides: rrdtool-ruby = %{version}-%{release}

# %description -n ruby-rrdtool
# The ruby-%{name} package includes a library that implements RRDtool bindings
# for the Ruby language.

# %package -n lua-rrdtool
# Summary: RRDtool module for Lua
# Group: Development/Languages
# Requires: %{name} = %{version}, lua-devel
# Obsoletes: rrdtool-lua <= %{version}-%{release}
# Provides: rrdtool-lua = %{version}-%{release}

# %description -n lua-rrdtool
# The lua-%{name} package includes a library that implements RRDtool bindings
# for the Lua language.

%prep
%setup -q -n %{name}-%{version}/rrdtool

%build
%configure \
    --disable-perl \
    --disable-rrdcached \
    --disable-rrdcgi \
    --disable-examples \
    --disable-python \
    --disable-nls \
    --disable-ruby \
    --disable-lua \
    --disable-tcl

%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 ../rrd-sync %{buildroot}%{_bindir}/rrd-sync

find %{buildroot} -name .packlist -exec %{__rm} {} \;
#%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
#%{__rm} -f %{buildroot}%{perl_vendorarch}/ntmake.pl

# Init script/sysconfig for rrfdcached
#%{__mkdir} -p %{buildroot}%{_initrddir}
#%{__cp} %{SOURCE1} %{buildroot}%{_initrddir}/rrdcached
#%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
#%{__cp} %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/rrdcached

# Create dir for rrdcached data and unix socket
#%{__mkdir} -p %{buildroot}%{_localstatedir}/rrdtool/rrdcached

# remove man pages
%{__rm} -f %{buildroot}%{_mandir}/man1/*.1*
%{__rm} -f %{buildroot}%{_mandir}/man3/librrd.3*

# remove docs
%{__rm} -rf %{buildroot}%{_datadir}/doc/rrdtool*

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n rrdtool -p /sbin/ldconfig

%postun -n rrdtool -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYRIGHT LICENSE NEWS THREADS TODO VERSION
%{_bindir}/rrdtool
%{_bindir}/rrdupdate
%{_bindir}/rrdcreate
%{_bindir}/rrdinfo
%{_libdir}/librrd.so.*
%{_libdir}/librrd_th.so.*
%{_bindir}/rrd-sync

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rrd.h
%{_includedir}/rrd_client.h
%{_includedir}/rrd_format.h
%{_libdir}/librrd.a
%{_libdir}/librrd.so
%{_libdir}/librrd_th.a
%{_libdir}/librrd_th.so
%{_libdir}/pkgconfig/librrd.pc
%exclude %{_libdir}/librrd.la
%exclude %{_libdir}/librrd_th.la

# %files -n perl-rrdtool
# %defattr(-, root, root, 0755)
# %doc bindings/perl-shared/MANIFEST bindings/perl-shared/README
# %doc %{_mandir}/man3/RRDp.3*
# %doc %{_mandir}/man3/RRDs.3*
# %{perl_vendorarch}/RRDs.pm
# %{perl_vendorarch}/auto/RRDs/*
# %{perl_vendorlib}/RRDp.pm

# %files -n tcl-rrdtool
# %defattr(-, root, root, 0755)
# %doc bindings/tcl/README
# %{_libdir}/rrdtool/ifOctets.tcl
# %{_libdir}/rrdtool/pkgIndex.tcl
# %{_libdir}/tclrrd%{version}.so

# %files -n python-rrdtool
# %defattr(-, root, root, 0755)
# %doc bindings/python/ACKNOWLEDGEMENT bindings/python/AUTHORS bindings/python/COPYING bindings/python/README
# %{!?_without_egg_info:%{python_sitearch}/*.egg-info}
# %{python_sitearch}/rrdtoolmodule.so

# %files -n ruby-rrdtool
# %defattr(-, root, root, 0755)
# %doc bindings/ruby/CHANGES bindings/ruby/README
# %{ruby_sitearch}/RRD.so

# %files -n lua-rrdtool
# %defattr(-, root, root, 0755)
# %{_libdir}/lua/

%changelog
