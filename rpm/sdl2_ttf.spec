Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL2_ttf
Version: 2.20.1
Release: 1
Source: %{name}-%{version}.tar.gz
Patch0: 0001-cmake-use-execute_process-for-CMake-3.14-compatibili.patch
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
mkdir -p build
pushd build
%cmake ..
%make_build
popd

%install
pushd build
%make_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
