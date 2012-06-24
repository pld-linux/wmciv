Summary:	Freeciv launcher for Window Maker Dock
Summary(pl):	Odpalacz Freeciv dla Doku Window Makera
Name:		wmciv
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.chez.com/soap/wmciv/%{name}-%{version}.tar.gz
# Source0-md5:	df737598c616286d71e904a9f9c01f4b
URL:		http://www.chez.com/soap/wmciv/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmciv is a dock-application designed for Window Maker. It allows you
to easily launch a Freeciv game. Any relatively recent version of
Freeciv should be supported.

After installing this package you have to create a directory named
.wmciv in your home directory and copy in it the files contained in
%{_defaultdocdir}/%{name}-%{version}/scripts/.

%description -l pl
wmciv jest dokowalnym apletem zaprojektowanym dla Window Makera.
Pozwala Ci na �atwe uruchamianie gry Freeciv. Powinien wsp�pracowa� z
ka�d�, w miar� now�, wersj� Freeciv.

Po zainstalowaniu tego pakietu musisz stworzy� katalog .wmciv w swoim
katalogu domowym i skopiowa� do niego pliki znajduj�ce si� w
%{_defaultdocdir}/%{name}-%{version}/scripts/.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -Wall -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG scripts

%attr(755,root,root) %{_bindir}/wmciv
