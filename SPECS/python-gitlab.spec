%define	module	gitlab

Name:		python-%{module}
Version:	0.16
Release:	1
Summary:	Interact with GitLab API
%define __urlhelper_localopts -O
Source0:	https://github.com/gpocentek/%{name}/archive/%{version}.tar.gz
License:	LGPLv3
Group:		Development/Python
Url:		https://github.com/gpocentek/python-gitlab
BuildArch:	noarch
BuildRequires:	pythonegg(3)(setuptools)

%description
Interact with GitLab API.

%prep
%setup -q

%build
%__python3 setup.py build

%install
%__python3 setup.py install --root=%{buildroot}

%files
%doc AUTHORS
%license ChangeLog
%doc README.rst
%doc requirements.txt
%doc test-requirements.txt
%doc docs/gl_objects/projects.py
%doc docs/gl_objects/projects.rst
%doc docs/gl_objects/todos.py
%doc docs/gl_objects/todos.rst
%{_bindir}/gitlab 
%{python3_sitelib}/gitlab/
%{python3_sitelib}/python_gitlab*.egg-info
