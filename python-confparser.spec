%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-confparser
Version:        1.0.0
Release:        3%{?dist}
Summary:        A KISS python module to parse *nix config files

Group:          Development/Libraries
License:        LGPLv2+
URL:            https://github.com/dougsland/python-confparser/wiki
Source0:        https://github.com/dougsland/python-confparser/raw/master/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires: python-devel, python-setuptools-devel

%description
Parser for *nix config files

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{python_sitelib}/python-confparser.py*
%{python_sitelib}/*.egg-info

%changelog
* Wed Jul 27 2011 Douglas Schilling Landgraf <dougsland@redhat.com> 1.0.0-3
- Renamed project to confparser
- Fixed the BuildArch space

* Tue Jul 26 2011 Douglas Schilling Landgraf <dougsland@redhat.com> 1.0.0-2
- Don't repeat the name in the summary.
- Fixed BuildArchitectures is practically always written short as BuildArch.
- Fixed License tag is incorrect, it should be LGPLv2+.
- Added python-devel, which is required for python packages.
- Fixed BuildRequires
- Added COPYING to doc.
- Fixed python_sitelib macro
- Added python macro to all python entries
- Improved Summary

* Mon Jul 25 2011 Douglas Schilling Landgraf <dougsland@redhat.com> 1.0.0
- Initial Commit
