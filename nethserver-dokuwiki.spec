%define name nethserver-dokuwiki
%define version 0.1.2
%define release 2
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
%{genfilelist} $RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%clean
rm -rf $RPM_BUILD_ROOT


%postun

%changelog
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
