%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	Graph
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - graph datastructure manipulation library
Summary(pl):	%{_pearname} - biblioteka do obróbki struktur danych grafów
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2e3030da0b0996702a1ea86b73941acb
URL:		http://pear.php.net/package/Structures_Graph/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Structures_Graph is a package for creating and manipulating graph
datastructures. It allows building of directed and undirected graphs,
with data and metadata stored in nodes. The library provides functions
for graph traversing as well as for characteristic extraction from the
graph topology.

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc± Structures_Graph mo¿liwe jest tworzenie i manipulacja
strukturami danych grafów. Pakiet pozwala tworzyæ grafy skierowane i
nieskierowane z danymi i metadanymi zapisanymi w wierzcho³kach.
Biblioteka dostarcza funkcje do przechodzenia grafów, a tak¿e
wyci±gania charakterystyki z topologii grafu.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Manipulator

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Manipulator/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Manipulator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
