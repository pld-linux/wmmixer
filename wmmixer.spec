Summary:	A mixer designed for WindowMaker
Summary(pl):	Program do regulacji g³o¶no¶ci dzwiêku dla WindowMaker'a
Name:		wmmixer
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A mixer designed for WindowMaker.

%description -l pl
Program do regulacji g³o¶no¶ci dzwiêku dla WindowMaker'a

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
