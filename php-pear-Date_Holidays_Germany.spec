%define		_class		Date
%define		_subclass	Holidays_Germany
%define		_status		alpha
%define		_pearname	Date_Holidays_Germany
Summary:	%{_pearname} - Driver based class to calculate holidays in Germany
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania świąt niemieckich
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a1bcfb1a6da9b56e9080a4ebca745dad
URL:		http://pear.php.net/package/Date_Holidays_Germany/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
Obsoletes:	php-pear-Date_Holidays_Germany-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating
holidays in Germany.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt niemieckich.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/Holidays/Driver/Germany.php
%{php_pear_dir}/Date/Holidays/Filter/Germany
%{php_pear_dir}/data/Date_Holidays_Germany
