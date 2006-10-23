Summary:	X font encodings database
Summary(pl):	Baza kodowañ fontów X
Name:		xorg-font-encodings
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
# Source0-md5:	902246a9ebc11a16a9726bf3f33f4b00
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

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%doc COPYING ChangeLog
%{_fontsdir}/encodings
