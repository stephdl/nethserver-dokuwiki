%define name nethserver-dokuwiki
%define version 1.3.1
%define release 1
Summary: Nethserver integration of dokuwiki
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL
URL: http://www.splitbrain.org/projects/dokuwiki
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRequires: nethserver-devtools
BuildRoot: /var/tmp/%{name}-%{version}
Requires: dokuwiki >= 20180422
Requires: nethserver-httpd
Requires: nethserver-rh-php73-php-fpm
AutoReqProv: no

%description
Nethserver integration of dokuwiki
DokuWiki is a simple to use Wiki aimed at the documentation needs of a small company


%prep
%setup

%build
perl ./createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_dokuwiki

%clean
rm -rf $RPM_BUILD_ROOT

%post
# ensure the local.php is writable by apache
/bin/chown apache:apache /etc/dokuwiki/local.php

%postun
/usr/bin/rm -f /etc/httpd/conf.d/zzz_dokuwiki.conf
/usr/bin/systemctl reload httpd

%changelog
* Sat Jul 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 1.3.1
- Remove http templates after rpm removal

* Sun May 03 2020  stephane de Labrusse  <stephdl@de-labrusse.fr> 1.3.0-1.ns7
- Move to rh-php73

* Thu Mar 05 2020  stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.14-1.ns7
- Fix bad sudoers permission

* Tue Nov 3 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.13-1.NS7
- Changed name of runtime directory fragment for rh-php71 

* Tue Oct 15 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.12-1.ns7
- cockpit. added to legacy apps

* Sun Jun 30 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.11-1.ns7
- local.php must be writable by apache and cannot be a template

* Fri Jun 28 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.10-1.ns7
- Allow the email address login with openLdap

* Wed Jun 26 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.9-1.ns7
- Find startTls from NethServer::SSSD for openLdap remote authenticator

* Sat Jun 22 2019 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.8-1.ns7
- Use a dedicated rh-php71-php service for dokuwiki

* Fri Jun 21 2019 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.7-1.ns7
- MaxExecutionTime and MaxInputTime implemented in apache settings

* Wed Jun 20 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.6-1.ns7
- Comment dokuwiki.conf, do not remove it

* Tue Jun 19 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.5-1.ns7
- Probe starttls for remote samba AD authentication

* Mon Jun 04 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.4-1.ns7
- Avoid apache vhost collision
- better definition of ssl certificate

* Sun May 13 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.3-1.ns7
- Typo on the apache URL path

* Tue May 8 2018  stephane de labrusse <stephdl@de-labrusse.fr> 1.2.2-1.ns7
- Subscribe to nethserver-sssd-save event 

* Sat May 5 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.1-1.ns7
- SambaAD uses self bind
- Users cannot change their password with openldap

* Tue May 1 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1.ns7
- use nethserver-rh-php71-php-fpm for dokuwiki-20180422

* Mon Oct 02 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.5-1.ns7
- corrected typo in local.protected.php
 
* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.4-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.3-1.ns7
- Template expansion on trusted-network

* Thu Mar 16 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-2.ns7
- Changed DocumentRoot to DomainName property

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-2.ns7
- GPL license

* Sat Mar 11 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-1.ns7
- Certificates for virtualhost added

* Thu Dec 1 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-1.ns7
- First release to NS7

* Sat Apr 9 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- set a document root is an option accessible by a property

* Tue Mar 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release to Nethserver
