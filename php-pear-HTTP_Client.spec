# ToDo:
# - fix pl description (last feature)
%include	/usr/lib/rpm/macros.php
%define         _class          HTTP
%define         _subclass       Client
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Easy way to perform multiple HTTP requests
Summary(pl):	%{_pearname} - £atwe zarz±dzanie wieloma zapytaniami HTTP
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4c7743632dd13cd9c5086bf25345a590
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an easy way to perform multiple HTTP requests and
process their resulsts.
Features:
- manage cookies and referrers between requests
- handles HTTP redirection
- has methods to set default headers and request parameters
- implements the Subject-Observer design pattern: the base class sends
  events to listeners that do the respons processing

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿na w ³atwy sposób wykonaæ wiele zapytañ HTTP i
przetworzyæ otrzymane wyniki.
Mo¿liwo¶ci:
- zarz±dzanie cookies i referrers pomiêdzy zapytaniami
- obs³uguje przekierowania HTTP
- posiada metody do ustawiania domy¶lnych parametrów nag³ówków i zapytañ

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
