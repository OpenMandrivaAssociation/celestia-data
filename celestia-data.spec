%global git 20240101

# Disable debuginfo generation, no executable or library is built
%global debug_package %{nil}
%define ver 1.7.0

Name:           celestia-data
Version:        %{ver}~%{git}.0
Release:        1
Summary:        Data, models and textures for Celestia
License:        GPL-2.0-or-later AND CC-BY-SA-4.0 AND JPL-image
URL:            https://celestiaproject.space/
# data download from here: https://github.com/CelestiaProject/CelestiaContent/
Source0: CelestiaContent-20240101.tar.gz
 
BuildArch:      noarch
 
BuildRequires:  cmake
BuildRequires:  gettext
Requires:       celestia-common = %{ver}

%description
This package provides the required data files, spacecraft
models and planet textures for Celestia to work.

%prep
%autosetup -n CelestiaContent-%{git} -p1

%build
%cmake
%make_build

%install
%make_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README
%{_datadir}/celestia/data
%{_datadir}/celestia/extras-standard
%{_datadir}/celestia/models
%{_datadir}/celestia/textures
%{_datadir}/celestia/warp
