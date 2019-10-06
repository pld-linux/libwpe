Summary:	General-purpose library for the WPE-flavored port of WebKit
Name:		libwpe
Version:	1.4.0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	1d4d38413ee0d0043f74d0445cab906f
URL:		https://wpewebkit.org/
BuildRequires:	cmake
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	Mesa-libEGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
%cmake . \
  -DCMAKE_BUILD_TYPE=Release

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_libdir}/%{name}-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}-1.0.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/wpe-1.0/
%attr(755,root,root) %{_libdir}/%{name}-1.0.so
%{_pkgconfigdir}/wpe-1.0.pc

