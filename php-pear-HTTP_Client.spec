%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Client
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - easy way to perform multiple HTTP requests
Summary(pl):	%{_pearname} - ³atwe zarz±dzanie wieloma zapytaniami HTTP
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4ae6973a6a3663abd9cdbe28ccaacdb4
URL:		http://pear.php.net/package/HTTP_Client/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.2
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
  events to listeners that do the response processing

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿na w ³atwy sposób wykonaæ wiele zapytañ HTTP i
przetworzyæ otrzymane wyniki.
Mo¿liwo¶ci:
- zarz±dzanie ciasteczkami (cookies) i ¼ród³ami odwo³añ (referrers)
  pomiêdzy zapytaniami
- obs³uga przekierowañ HTTP
- metody do ustawiania domy¶lnych parametrów nag³ówków i zapytañ
- implementacja idei projektowej Subject-Observer - klasa bazowa
  wysy³a zdarzenia do nas³uchuj±cych, które przetwarzaj± te dane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
