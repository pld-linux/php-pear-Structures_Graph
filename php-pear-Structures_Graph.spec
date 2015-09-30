%define		status		stable
%define		pearname	Structures_Graph
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - graph datastructure manipulation library
Summary(pl.UTF-8):	%{pearname} - biblioteka do obróbki struktur danych grafów
Name:		php-pear-%{pearname}
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ee63a3d24c94338af90334f3dd42c518
URL:		http://pear.php.net/package/Structures_Graph/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.2
Obsoletes:	php-pear-Structures_Graph-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Structures_Graph is a package for creating and manipulating graph
datastructures. It allows building of directed and undirected graphs,
with data and metadata stored in nodes. The library provides functions
for graph traversing as well as for characteristic extraction from the
graph topology.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Za pomocą Structures_Graph możliwe jest tworzenie i manipulacja
strukturami danych grafów. Pakiet pozwala tworzyć grafy skierowane i
nieskierowane z danymi i metadanymi zapisanymi w wierzchołkach.
Biblioteka dostarcza funkcje do przechodzenia grafów, a także
wyciągania charakterystyki z topologii grafu.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv docs/%{pearname}/docs/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install
cp -a tutorials/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/*.php
%{php_pear_dir}/Structures/Graph
%{_examplesdir}/%{name}-%{version}
