Summary:	This is the ASN.1 library used in GNUTLS.                                                                                             
Name:		libtasn1
Version:	0.2.6
Release:	0.fdr.1.rh90
Epoch:		0
License:	LGPL
Group:		System Environment/Libraries
URL:		http://www.gnu.org/software/gnutls/download.html
Source0:	ftp://ftp.gnutls.org/pub/gnutls/libtasn1/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
BuildRequires:	bison


%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
%{__make} DESTDIR="$RPM_BUILD_ROOT" install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%check
%{__make} check


%clean
rm -rf "$RPM_BUILD_ROOT"


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc doc/TODO doc/*.ps
%doc AUTHORS COPYING* ChangeLog NEWS README THANKS
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so*


%changelog
* Tue Nov 18 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.2.6-0.fdr.1
- updated to 0.2.6

* Mon Aug  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.5-0.fdr.1
- updated to 0.2.5
- changed license to LGPL
- rearranged %%check to reflect execution order
- minor cosmetical changes

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.4-0.fdr.1
- Initial build.

### Local Variables:
### compile-command: "cd .. && ./buildpkg libtasn1"
### End:
