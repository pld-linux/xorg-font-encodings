Summary:	X font encodings database
Summary(pl.UTF-8):	Baza kodowań fontów X
Name:		xorg-font-encodings
Version:	1.0.6
Release:	1
License:	Public Domain
Group:		X11
Source0:	https://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.xz
# Source0-md5:	c2bcfdc52b8b6462228342cedae2fed9
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font encodings database.

%description -l pl.UTF-8
Baza kodowań fontów X.

%prep
%setup -q -n encodings-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-encodingsdir=%{_fontsdir}/encodings

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/encodings
