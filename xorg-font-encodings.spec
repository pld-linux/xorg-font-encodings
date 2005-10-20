Summary:	X font encodings database
Summary(pl):	Baza kodowañ fontów X
Name:		xorg-font-encodings
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/font/encodings-%{version}.tar.bz2
# Source0-md5:	94a6c7af7516c05b66827121bafd6b70
Patch0:		xorg-encodings-fontpath.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font encodings database.

%description -l pl
Baza kodowañ fontów X.

%prep
%setup -q -n encodings-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_fontsdir}/encodings
