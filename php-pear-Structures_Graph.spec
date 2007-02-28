%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	Graph
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - graph datastructure manipulation library
Summary(pl.UTF-8):	%{_pearname} - biblioteka do obróbki struktur danych grafów
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2664e2d024048f982e12fad4d1bfbb87
URL:		http://pear.php.net/package/Structures_Graph/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Structures_Graph is a package for creating and manipulating graph
datastructures. It allows building of directed and undirected graphs,
with data and metadata stored in nodes. The library provides functions
for graph traversing as well as for characteristic extraction from the
graph topology.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą Structures_Graph możliwe jest tworzenie i manipulacja
strukturami danych grafów. Pakiet pozwala tworzyć grafy skierowane i
nieskierowane z danymi i metadanymi zapisanymi w wierzchołkach.
Biblioteka dostarcza funkcje do przechodzenia grafów, a także
wyciągania charakterystyki z topologii grafu.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
