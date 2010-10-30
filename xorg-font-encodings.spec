Summary:	X font encodings database
Summary(pl.UTF-8):	Baza kodowań fontów X
Name:		xorg-font-encodings
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
# Source0-md5:	0f2d6546d514c5cc4ecf78a60657a5c1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.3
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
	--build=%{_host} \
	--host=%{_host} \
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
%doc COPYING ChangeLog README
%{_fontsdir}/encodings
