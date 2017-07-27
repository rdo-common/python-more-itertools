# spec file for package python-more-itertools
# https://fedoraproject.org/wiki/Packaging:Python#Example_common_spec
%global srcname more-itertools
%global _description \
Opensource python library wrapping around itertools. Package also includes \
implementations of the recipes from the itertools documentation.\
\
See https://pythonhosted.org/more-itertools/index.html for documentation.\
%global sum Python library for efficient use of itertools utility

Name:           python-%{srcname}
Version:        2.3
Release:        4%{?dist}
Summary:        %{sum} 
License:        MIT
URL:            https://github.com/erikrose/more-itertools
Source0:        https://pypi.python.org/packages/3d/4d/5900efaab46680e3c6c7a2fd87e4531f87e101ec35f6941621dc7f097e82/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  python2-six
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-six

%description %_description

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}} 

%description -n python2-%{srcname} %_description

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -a0

%build
%py2_build
(cd more-itertools-%{version}/ && %py3_build)

%install
%py2_install
(cd more-itertools-%{version}/ && %py3_install)

%check
%{__python2} -m nose build/lib/ -v
%{__python3} -m nose more-itertools-%{version}/build/lib/ -v

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python2_sitelib}/more_itertools/
%{python2_sitelib}/more_itertools-%{version}-py%{python2_version}.egg-info

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/more_itertools/
%{python3_sitelib}/more_itertools-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 aarem AT fedoraproject DOT org - 2.3-1
- update to 2.3
* Fri Oct 14 2016 aarem AT fedoraproject DOT org - 2.2-4
- fixed missing sum in line 9 of spec file, per BZ #138195
* Sat Oct 8 2016 aarem AT fedoraproject DOT org - 2.2-3
- renamed spec file to match package as per BZ #1381029
-fixed bug (incorrect python3_provides) as per BZ #1381029
- use common macro for description as per suggestion in BZ #1381029

* Wed Oct 05 2016 aarem AT fedoraproject DOT org - 2.2-2
- separated python and python3 cases as per BZ #1381029

* Sun Oct 02 2016 aarem AT fedoraproject DOT org - 2.2-1
- initial packaging of 2.2 version
