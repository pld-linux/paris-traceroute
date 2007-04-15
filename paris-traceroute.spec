Summary:	A new version of a well-known network diagnosis and measurement tool
Summary(pl.UTF-8):	Nowa wersja dobrze znanego narzędzia do diagnostyki i pomiarów sieci
Name:		paris-traceroute
Version:	0.92
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.paris-traceroute.net/downloads/%{name}-%{version}-dev.tar.gz
# Source0-md5:	43a23e4a0d4a877e81b7c330091adc75
URL:		http://www.paris-traceroute.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Paris traceroute is a new version of the well-known network diagnosis
and measurement tool. It addresses problems caused by load balancers
with the initial implementation of traceroute.

%description -l pl.UTF-8
Paris traceroute to nowa wersja dobrze znanego narzędzia do
diagnostyki i pomiarów sieci. Radzi sobie z problemami powodowanymi
przez load balancery ze wstępną implementacją traceroute.

%prep
%setup -q -n %{name}-%{version}-dev

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
