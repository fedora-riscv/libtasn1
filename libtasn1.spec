## $Id$

%{!?release_func:%global release_func() %1%{?dist}}

Summary:	This is the ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	0.3.0
Release: 	%release_func 1

License:	LGPL
Group:		System Environment/Libraries
URL:		http://www.gnu.org/software/gnutls/download.html
Source0:	ftp://ftp.gnutls.org/pub/gnutls/libtasn1/%name-%version.tar.gz
Source1:	ftp://ftp.gnutls.org/pub/gnutls/libtasn1/%name-%version.tar.gz.sig
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	bison


%package devel
Summary:	Files for development of applications which will use libtasn1
Group:		Development/Libraries
Requires:	%name = %version-%release
Requires(pre):		automake pkgconfig
Requires(postun):	automake pkgconfig
Requires(post):		/sbin/install-info
Requires(postun):	/sbin/install-info


%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

%description devel
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This packages contains files for development of applications which
will use libtasn1.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT{%_libdir/*.la,%_infodir/dir}


%check
make check


%clean
rm -rf "$RPM_BUILD_ROOT"


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%post devel
/sbin/install-info --info-dir=%_infodir %_infodir/%name.info || :

%preun devel
test "$1" != 0 ||
	/sbin/install-info --info-dir=%_infodir --delete %_infodir/%name.info || :


%files
%defattr(-,root,root,-)
%doc doc/TODO doc/*.pdf
%doc AUTHORS COPYING* ChangeLog NEWS README THANKS
%_libdir/*.so.*


%files devel
%defattr(-,root,root,-)
%_bindir/*-config
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
%_datadir/aclocal/libtasn1.m4
%_infodir/*.info.*
%_mandir/man3/*asn1*


%changelog
* Mon Mar  6 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.0-1
- updated to 0.3.0
- removed unneeded curlies
- created -devel subpackage

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.2.6-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 18 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.2.6-0.fdr.1
- updated to 0.2.6

* Mon Aug  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.5-0.fdr.1
- updated to 0.2.5
- changed license to LGPL
- rearranged %%check to reflect execution order
- minor cosmetical changes

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.4-0.fdr.1
- Initial build.