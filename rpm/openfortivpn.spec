Name:           openfortivpn
Version:        1.11.0
Release:        1%{?dist}
Summary:        Client for PPP+SSL VPN tunnel services

Group:          Applications/Internet
License:        GPLv3+
URL:            https://github.com/adrienverge/openfortivpn
Source0:        https://github.com/adrienverge/openfortivpn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  openssl-devel
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%{_bindir}/openfortivpn
%{_mandir}/man1/openfortivpn.1*
%{_datadir}/openfortivpn
%dir %{_sysconfdir}/openfortivpn
%config(noreplace) %{_sysconfdir}/openfortivpn/config
%doc README.md
%license LICENSE

