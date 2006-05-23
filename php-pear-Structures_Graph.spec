%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	Graph
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - graph datastructure manipulation library
Summary(pl):	%{_pearname} - biblioteka do obr�bki struktur danych graf�w
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	5
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	97baf9bf892a6a54213d193767f97a09
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

%description -l pl
Za pomoc� Structures_Graph mo�liwe jest tworzenie i manipulacja
strukturami danych graf�w. Pakiet pozwala tworzy� grafy skierowane i
nieskierowane z danymi i metadanymi zapisanymi w wierzcho�kach.
Biblioteka dostarcza funkcje do przechodzenia graf�w, a tak�e
wyci�gania charakterystyki z topologii grafu.

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
