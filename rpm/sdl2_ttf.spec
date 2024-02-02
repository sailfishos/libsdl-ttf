%undefine __cmake_in_source_build

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL2_ttf
Version: 2.22.0
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libsdl-org/SDL_net
License: zlib
BuildRequires: cmake
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
%cmake
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*
