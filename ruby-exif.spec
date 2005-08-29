%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	EXIF module for Ruby
Summary(pl):	Modu³ EXIF dla Ruby
Name:		ruby-exif
Version:	0.1
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://www.asobitari.nu/program/exif.zip
# Source0-md5:	53b7ad45772bbf4bdb638dfc14682a0c
URL:		http://www.asobitari.nu/program/exif.html
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
BuildRequires:	unzip
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EXIF module for Ruby.

%description -l pl
Modu³ EXIF dla Ruby.

%prep
%setup -c -q

%build
mkdir lib
mv *exif*.rb lib/
cp /usr/share/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_examplesdir}/%{name}-%{version}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/ruby-exif.rb
