%define name nethserver-dokuwiki
%define version 0.0.7
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
Requires: dokuwiki
Requires: nethserver-httpd
Requires: nethserver-directory
AutoReqProv: no

%description
Nethserver integration of dokuwiki
DokuWiki is a simple to use Wiki aimed at the documentation needs of a small company


%prep
%setup

%build
perl ./createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%clean
rm -rf $RPM_BUILD_ROOT


%postun

%changelog
* Sun May 13 2018 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.7-1
- Typo on the apache URL path

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.6-1
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5-1
- Template expansion on trusted-network

* Thu Mar 16 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4-2
- Changed DocumentRoot to DomainName property

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3-1
- GPL license

* Sat Mar 11 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- Certificates for virtualhost added

* Sat Apr 9 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- set a document root is an option accessible by a property

* Tue Mar 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release to Nethserver
