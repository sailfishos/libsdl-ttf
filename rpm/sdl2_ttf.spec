Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL2_ttf
Version: 2.0.15
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_ttf/
License: zlib
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(freetype2)

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Simple DirectMedia Layer - Sample TrueType Font Library (Development)
Requires: %{name}

%description devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
