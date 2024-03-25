#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	General-purpose library for the WPE-flavored port of WebKit
Summary(pl.UTF-8):	Ogólna biblioteka do portu WPE biblioteki WebKit
Name:		libwpe
Version:	1.16.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/WebPlatformForEmbedded/libwpe/releases
Source0:	https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9779115aaa7e67abe642777394e7bfa2
Patch0:		%{name}-libdir.patch
URL:		https://wpewebkit.org/
BuildRequires:	EGL-devel
BuildRequires:	cmake >= 3.0
%{?with_apidocs:BuildRequires:	hotdoc}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General-purpose library developed for the WPE-flavored port of WebKit.

%description -l pl.UTF-8
Ogólna biblioteka do portu WPE biblioteki WebKit.

%package devel
Summary:	Header files for WPE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WPE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	EGL-devel
Requires:	xorg-lib-libxkbcommon-devel

%description devel
Header files for WPE library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WPE.

%package apidocs
Summary:	API documentation for WPE library
Summary(pl.UTF-8):	Dokumentacja API biblioteki WPE
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for WPE library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki WPE.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_apidocs:-DBUILD_DOCS=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_libdir}/libwpe-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpe-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpe-1.0.so
%{_includedir}/wpe-1.0
%{_pkgconfigdir}/wpe-1.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/Documentation/html/*
%endif
