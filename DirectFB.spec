Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.21
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB/%{name}-%{version}.tar.gz
# Source0-md5:	22699a04f2f618b287aa0ae1b06045b5
Source1:	http://www.directfb.org/download/DirectFB-extra/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-fix.patch
# missing files taken from DirectFB CVS
Patch3:		%{name}-missing-files.patch
URL:		http://www.directfb.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	sysfsutils-devel
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-%{version}

%description
DirectFB hardware graphics acceleration - libraries.

%description -l pl
Wspomaganie grafiki DirectFB - biblioteki.

%package devel
Summary:	DirectFB - development package
Summary(pl):	DirectFB - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel >= 1.1.3

%description devel
DirectFB header files.

%description devel -l pl
Pliki nag��wkowe dla DirectFB.

%package static
Summary:	DirectFB static libraries
Summary(pl):	Statyczne biblioteki DirectFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
DirectFB static libraries.

%description static -l pl
Statyczne biblioteki DirectFB.

%package doc
Summary:	DirectFB - documentation
Summary(pl):	DirectFB - dokumentacja
Group:		Development/Libraries

%description doc
DirectFB documentation and tutorials.

%description doc -l pl
Dokumentacja dla systemu DirectFB wraz z wprowadzeniem.

%package core-sdl
Summary:	SDL core system for DirectFB
Summary(pl):	System SDL dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-sdl
This package contains SDL core system module for DirectFB.

%description core-sdl -l pl
Ten pakiet zawiera modu� systemu SDL dla DirectFB.

%package font-ft2
Summary:	FreeType2 font provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca fonty poprzez FreeType2
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description font-ft2
This package contains FreeType2 font provider for DirectFB.

%description font-ft2 -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� fonty poprzez
bibliotek� FreeType2.

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca grafik� JPEG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� grafik� JPEG.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca grafik� PNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� grafik� PNG.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e 's@sysfs/libsysfs.h@libsysfs.h@' \
	configure.in gfxdrivers/{nvidia/nvidia.c,matrox/matrox_maven.c}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	%{!?debug:--disable-debug} \
	--disable-maintainer-mode \
	--enable-elo-input \
	--enable-fast-install \
	--enable-linux-input \
	--enable-mutouch \
	--enable-sdl \
	--enable-shared \
	--enable-static \
	--enable-unique \
	--enable-video4linux2 \
	--enable-voodoo \
	--enable-zlib \
%ifarch %{ix86}
%ifnarch i386 i486
	--enable-mmx \
%endif
%ifnarch i386 i486 i586
	--enable-sse
%endif
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf DFBTutorials* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# dbfdump and dfbg require multi-application core - useless now
rm -f $RPM_BUILD_ROOT{%{_bindir}/{dfbdump,dfbg},%{_mandir}/man1/dfbg.1}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dfbinfo
%attr(755,root,root) %{_bindir}/dfblayer
%attr(755,root,root) %{_bindir}/dfbproxy
%attr(755,root,root) %{_bindir}/dfbscreen
%attr(755,root,root) %{_bindir}/dfbsummon
%attr(755,root,root) %{_bindir}/uwmdump
%attr(755,root,root) %{_libdir}/libdirect-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libdirectfb-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libfusion-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libuniquewm-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libvoodoo-*.so.*.*.*
%dir %{dfbdir}
%dir %{dfbdir}/gfxdrivers
%attr(755,root,root) %{dfbdir}/gfxdrivers/*.so
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_elo.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_joystick.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_keyboard.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_linux_input.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_lirc.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_mutouch.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ps2mouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_serialmouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sonypi.so
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/IDirectFB
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFB/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDataBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDataBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDisplayLayer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDisplayLayer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBEventBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBEventBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBInputDevice
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBInputDevice/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBPalette
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBPalette/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBScreen
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBScreen/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBSurface
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBSurface/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.so
%dir %{dfbdir}/interfaces/IDirectFBWindow
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBWindow/lib*.so
%dir %{dfbdir}/systems
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_fbdev.so
%dir %{dfbdir}/wm
%attr(755,root,root) %{dfbdir}/wm/*.so
%{_datadir}/directfb-%{version}
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/directfb-config
%attr(755,root,root) %{_bindir}/directfb-csource
%attr(755,root,root) %{_libdir}/libdirect.so
%attr(755,root,root) %{_libdir}/libdirectfb.so
%attr(755,root,root) %{_libdir}/libfusion.so
%attr(755,root,root) %{_libdir}/libuniquewm.so
%attr(755,root,root) %{_libdir}/libvoodoo.so
%{_libdir}/libdirect.la
%{_libdir}/libdirectfb.la
%{_libdir}/libfusion.la
%{_libdir}/libuniquewm.la
%{_libdir}/libvoodoo.la
%{_includedir}/directfb
%{_includedir}/directfb-internal
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/directfb-csource.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{dfbdir}/gfxdrivers/*.*[ao]
%{dfbdir}/inputdrivers/*.*[ao]
%{dfbdir}/interfaces/*/*.*[ao]
%{dfbdir}/systems/*.*[ao]
%{dfbdir}/wm/*.*[ao]

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%{_examplesdir}/%{name}-%{version}

%files core-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sdlinput.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_sdl.so

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.so

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.so

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.so
