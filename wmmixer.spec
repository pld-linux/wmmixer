Summary:	A mixer designed for WindowMaker
Summary(pl.UTF-8):	Program do regulacji głośności dźwięku dla WindowMakera
Name:		wmmixer
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://freakzone.net/gordon/src/%{name}-%{version}.tar.gz
# Source0-md5:	bfb1ded801910dd39e1bb0b273c4e1c3
URL:		http://freakzone.net/gordon/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A mixer designed for WindowMaker.

%description -l pl.UTF-8
Program do regulacji głośności dźwięku dla WindowMakera.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D wmmixer $RPM_BUILD_ROOT%{_bindir}/wmmixer
install -D wmmixer.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmmixer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES home.wmmixer
%attr(755,root,root) %{_bindir}/wmmixer
%{_mandir}/man1/*
