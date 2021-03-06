#
# Orig: spec file for package lxc (Version 0.6.5)
# brian@aljex.com
#
# Modified: 2010-03-14 llange

Name:           lxc-management-tools
Version:        1.0.0
Release:        4
Summary:        Lxc Management Tools
Group:          System/Management
AutoReqProv:    on
License:        LGPL v2.1 only
URL:		http://github.com/llange/LXC-Management-Tools/
Packager:	Ludovic LANGE
Vendor:		eTour
Distribution:	Fedora / Redhat
Source0:        lxc
Source1:        lxc-shutdown-agent
Source3:        lxc-shutdown-all
Source4:        lxc-status-all
Source5:	lxc.conf
Source6:	lxc-start-vm
Source7:	lxc-stop-vm
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       lxc >= 0.6.3

%description
This particular build/package contains init scripts so that the host
system can gracefully start and stop container systems when the host
system boots up and shuts down.


Authors:
--------
    (init scripts: Brian K. White <brian@aljex.com>)
    (Fedora packaging: llange)

%prep
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}
exit 0

%build
exit 0

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}
install -m 755 %{SOURCE4} %{buildroot}%{_bindir}
install -m 755 %{SOURCE6} %{buildroot}%{_bindir}
install -m 755 %{SOURCE7} %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_sysconfdir}
install -m 755 %{SOURCE5} %{buildroot}%{_sysconfdir}
mkdir -p -m 755 %{buildroot}%{_initddir}
install -m 755 %{SOURCE0} %{buildroot}%{_initddir}

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post

%postun

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/lxc.conf
%{_bindir}/lxc-*
%{_initddir}/lxc

%changelog
* Sat Mar 27 2010 llange
- 1.0.0-4 new commands for managing one VM only
* Sun Mar 14 2010 llange
- 1.0.0-3 Fix for lxc 0.6.3, need to restart your containers from the host with restart
* Sun Mar 14 2010 llange
- 1.0.0-1 Packaging for Fedora
* Sat Feb 13 2010 brian@aljex.com
- init scripts to start/stop/status all containers
- lxc-shutdown-agent container monitor daemon script
