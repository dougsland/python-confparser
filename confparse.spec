%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           confparse
Version:        1.0.0
Release:        1%{?dist}
Summary:        confparse - A KISS parse to *nix config files

Group:          Development/Libraries
License:        GPLv2
URL:            https://github.com/dougsland/confparse
Source0:        https://github.com/dougsland/confparse/raw/master/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch

%if 0%{?fedora}
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif      

%description
Parser for *nix config files

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*

%changelog
* Sat Jul 25 2011 Douglas Schilling Landgraf <dougsland@redhat.com> 1.0.0
- Initial Commit
