Summary:	DirectFB - Hardware graphics accelration.
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.0
Release:	1
Copyright:	GPL
Group:		X11	
Group(pl):	X11
Source:		http://directfb.org/download/%{name}-%{version}.tar.gz
URL:		htt://directfs.org/
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%package devel
Group:		X11
Group(pl):	X11
Summary:	DirectFB - development package.
Summary(pl):	DirectFB - pliki naglowkowe.
%description devel
%description -l pl devel

%package doc
Group:		X11
Group(pl):	X11
Summary:	DirectFB - documentation.
Summary(pl):	DirectFB - dokumantacja.
%description doc
%description -l pl doc

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%defattr(644,root,root,755)
#%doc
#%attr(,,)

%files devel
%files doc
