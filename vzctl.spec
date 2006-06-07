%define _initddir /etc/init.d
%define _crondir /etc/cron.d
%define _vzdir /vz
%define _lockdir %{_vzdir}/lock 
%define _dumpdir %{_vzdir}/dump 
%define _cachedir %{_vzdir}/template/cache 
%define _veipdir /var/lib/vzctl/veip 
%define _libdir /usr/lib/vzctl
%define _configdir /etc/vz
%define _scriptdir /usr/share/vzctl//scripts
%define _vpsconfdir /etc/sysconfig/vz-scripts
%define _netdir	/etc/sysconfig/network-scripts
%define _logrdir /etc/logrotate.d
%define _distconfdir %{_configdir}/dists
%define _distscriptdir %{_distconfdir}/scripts
# rh macros defines _mandir incrorrectly
%define _mandir %{_datadir}/man

Summary: Virtual Private Server control utility
Name: vzctl
Version: 3.0.10
Release: 1
License: GPL
Group: System Environment/Kernel
Source: vzctl-%{version}.tar.bz2
ExclusiveOS: Linux
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: vzkernel
# these reqs are for vz helper scripts
Requires: bash
Requires: gawk
Requires: sed
Requires: ed
Requires: grep
Requires: /sbin/chkconfig
Requires: vzquota >= 2.7.0-4
Requires: fileutils
Requires: vzctl-lib = %{version}-%{release}
Requires: tar

# requires for vzmigrate purposes
Requires: rsync
Requires: gawk
Requires: openssh

%description
This utility allows system administator to control VPS,
e.g. create, start, shutdown, set various options and limits etc.

%prep
%setup
%build
make CFLAGS="$RPM_OPT_FLAGS" ARCH=%{_arch}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir} ARCH=%{_arch} \
	VPSCONFDIR=%{_vpsconfdir}
ln -s ../sysconfig/vz-scripts $RPM_BUILD_ROOT/etc/vz/conf
ln -s ../vz/vz.conf $RPM_BUILD_ROOT/etc/sysconfig/vz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_initddir}/vz
%attr(644,root,root) %config(noreplace) %{_crondir}/vpsreboot
%attr(644,root,root) %{_crondir}/vpsnetclean
%dir %attr(755,root,root) %{_lockdir}
%dir %attr(755,root,root) %{_dumpdir}
%dir %attr(755,root,root) %{_cachedir}
%dir %attr(755,root,root) %{_veipdir}
%dir %attr(755,root,root) %{_configdir}
%dir %attr(755,root,root) %{_vpsconfdir}
%dir %attr(755,root,root) %{_distconfdir}
%dir %attr(755,root,root) %{_distscriptdir}
%dir %attr(755,root,root) %{_vzdir}
%attr(755,root,root) %{_sbindir}/vzctl
%attr(755,root,root) %{_sbindir}/arpsend
%attr(755,root,root) %{_sbindir}/vzsplit
%attr(755,root,root) %{_sbindir}/vzlist
%attr(755,root,root) %{_sbindir}/vzmemcheck
%attr(755,root,root) %{_sbindir}/vzcpucheck
%attr(755,root,root) %{_sbindir}/vzcalc
%attr(755,root,root) %{_sbindir}/vzpid
%attr(755,root,root) %{_sbindir}/vzcfgvalidate
%attr(755,root,root) %{_sbindir}/vzmigrate
%attr(755,root,root) %{_scriptdir}/vpsreboot
%attr(755,root,root) %{_scriptdir}/vpsnetclean
%attr(644,root,root) %{_logrdir}/vzctl
%attr(644,root,root) %{_distconfdir}/distribution.conf-template
%attr(644,root,root) %{_distconfdir}/default
%attr(755,root,root) %{_distscriptdir}/*.sh
%attr(644,root,root) %{_distscriptdir}/functions
%attr(755,root,root) %{_netdir}/ifup-venet
%attr(755,root,root) %{_netdir}/ifdown-venet
%attr(644,root,root) %{_netdir}/ifcfg-venet0
%attr(644, root, root) %{_mandir}/man8/vzctl.8.*
%attr(644, root, root) %{_mandir}/man8/vzmigrate.8.*
%attr(644, root, root) %{_mandir}/man8/arpsend.8.*
%attr(644, root, root) %{_mandir}/man8/vzsplit.8.*
%attr(644, root, root) %{_mandir}/man8/vzcfgvalidate.8.*
%attr(644, root, root) %{_mandir}/man8/vzmemcheck.8.*
%attr(644, root, root) %{_mandir}/man8/vzcalc.8.*
%attr(644, root, root) %{_mandir}/man8/vzpid.8.*
%attr(644, root, root) %{_mandir}/man8/vzcpucheck.8.*
#%attr(644, root, root) %{_mandir}/man8/vzcheckovr.8.*
%attr(644, root, root) %{_mandir}/man8/vzlist.8.*
%attr(644, root, root) %{_mandir}/man5/vps.conf.5.*
%attr(644, root, root) %{_mandir}/man5/vz.conf.5.*

%config(noreplace) %{_configdir}/vz.conf
%config(noreplace) %{_distconfdir}/*.conf
%config %{_vpsconfdir}/ve-vps.basic.conf-sample
%config %{_vpsconfdir}/ve-light.conf-sample
%config %{_vpsconfdir}/0.conf

%attr(777, root, root) /etc/vz/conf
%config /etc/sysconfig/vz

%post
/bin/rm -rf /dev/vzctl
/bin/mknod -m 600 /dev/vzctl c 126 0
if [ -f %{_configdir}/vz.conf ]; then
	if ! grep "IPTABLES=" %{_configdir}/vz.conf >/dev/null 2>&1; then
		echo 'IPTABLES="ipt_REJECT ipt_tos ipt_limit ipt_multiport iptable_filter iptable_mangle ipt_TCPMSS ipt_tcpmss ipt_ttl ipt_length"' >> %{_configdir}/vz.conf
	fi
fi
/sbin/chkconfig --add vz > /dev/null 2>&1

if [ -f /etc/SuSE-release ]; then
	NET_CFG='ifdown-venet ifup-venet'
	if ! grep -q -E "^alias venet0" /etc/modprobe.conf; then 
		echo "alias venet0 vznet" >> /etc/modprobe.conf
	fi
	ln -f /etc/sysconfig/network-scripts/ifcfg-venet0 /etc/sysconfig/network/ifcfg-venet0
	for file in ${NET_CFG}; do
		ln -sf /etc/sysconfig/network-scripts/${file} /etc/sysconfig/network/scripts/${file}
	done
fi

%preun
if [ $1 = 0 ]; then 
	/sbin/chkconfig --del vz >/dev/null 2>&1
fi

%package lib
Summary: Virtual Private Servers control API library
Group: System Environment/Kernel
%ifarch x86_64 ia64
Provides: libvzctl-fs.so()(64bit)
%else
Provides: libvzctl-fs.so
%endif

%description lib
Virtual Private Servers control API library

%files lib
%defattr(-,root,root)
%dir %{_libdir}/lib
%attr(755,root,root) %{_libdir}/lib/libvzctl.so.*
%attr(755,root,root) %{_libdir}/lib/libvzctl-fs.so
%attr(755,root,root) %{_libdir}/lib/libvzctl-simfs.so.0.0.2
%attr(755,root,root) %{_libdir}/scripts/vps-stop
%attr(755,root,root) %{_libdir}/scripts/vps-functions
%attr(755,root,root) %{_libdir}/scripts/vps-net_add
%attr(755,root,root) %{_libdir}/scripts/vps-net_del
%attr(755,root,root) %{_libdir}/scripts/vps-create
%attr(755,root,root) %{_libdir}/scripts/vps-postcreate

