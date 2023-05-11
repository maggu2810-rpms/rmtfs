%global commit 695d0668ffa6e2a4bf6e676f3c58a444a5d67690

Name:           rmtfs
Version:        20220718
Release:        1%{?dist}
Summary:        Qualcomm Remote Filesystem Service Implementation
License:        BSD-3-Clause
URL:            https://github.com/andersson/rmtfs
Source0:        https://github.com/andersson/rmtfs/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  qrtr
BuildRequires:  systemd-devel

%description
%summary.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
%make_install prefix=/usr

%files
%{_bindir}/rmtfs
/usr/lib/systemd/system/rmtfs.service

%changelog
* Thu May 11 2023 Justin Zobel <justin@1707.io> -
- Initial Package
