Name:           openfortivpn
Summary:        Client for PPP+SSL VPN tunnel services compatible with Fortinet
Version:        1.17.1
Release:        1
License:        GPLv3+
URL:            https://github.com/adrienverge/openfortivpn
Source0:        %{name}-%{version}.tar.bz2
Patch0:         0001-Add-trust-all-certs-option.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.
It is compatible with Fortinet VPNs.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%reconfigure
%make_build

%install
%make_install

# We don't need config template and man pages on device
rm -f %{buildroot}/%{_datadir}/openfortivpn/config.template
rm -f %{buildroot}/%{_mandir}/man1/openfortivpn.1*

%files
%defattr(-,root,root,-)
%license LICENSE LICENSE.OpenSSL
%{_bindir}/openfortivpn
%{_unitdir}/openfortivpn@.service
%dir %{_sysconfdir}/openfortivpn
%config(noreplace) %{_sysconfdir}/openfortivpn/config
