Summary:	X font encodings database
Summary(pl):	Baza kodowa� font�w X
Name:		xorg-font-encodings
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/encodings-%{version}.tar.bz2
# Source0-md5:	9275581cdcd7d74120a75680ed2aa1ca
#Patch0:		encodings-fontpath.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font encodings database.

%description -l pl
Baza kodowa� font�w X.

%prep
%setup -q -n encodings-%{version}
#%patch0 -p1

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
