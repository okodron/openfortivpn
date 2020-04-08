Name:           openfortivpn
Version:        1.11.0
Release:        1
Summary:        Client for PPP+SSL VPN tunnel services compatible with Fortinet
License:        GPLv3+
URL:            https://github.com/adrienverge/openfortivpn
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  openssl-devel
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.
It is compatible with Fortinet VPNs.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install
rm -f %{buildroot}/%{_datadir}/openfortivpn/config.template

%files
%defattr(-,root,root,-)
%{_bindir}/openfortivpn
%{_mandir}/man1/openfortivpn.1*
%dir %{_sysconfdir}/openfortivpn
%config(noreplace) %{_sysconfdir}/openfortivpn/config
%doc README.md
%license LICENSE LICENSE.OpenSSL
