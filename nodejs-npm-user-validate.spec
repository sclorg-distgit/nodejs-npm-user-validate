%{?scl:%scl_package nodejs-npm-user-validate}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-npm-user-validate
Version:        0.1.1
Release:        2%{?dist}
Summary:        Username, password, and e-mail validation for the npm registry
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/robertkowalski/npm-user-validate
Source0:        http://registry.npmjs.org/npm-user-validate/-/npm-user-validate-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  %{?scl_prefix}npm(tap)

%description
This library validates usernames, passwords, and e-mail addresses to the
standards required by the npm registry.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/npm-user-validate
cp -pr npm-user-validate.js package.json %{buildroot}%{nodejs_sitelib}/npm-user-validate

%nodejs_symlink_deps

%check
#nodejs_symlink_deps --check
#tap test/*.js

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/npm-user-validate
%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-2
- rebuilt

* Thu Jan 08 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-1
- New upstream release 0.1.1

* Fri Nov 08 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.3-2.1
- Software collections support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- new upstream release 0.0.3

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-3
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-2
- fix License tag

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package
