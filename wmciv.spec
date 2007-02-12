Summary:	Freeciv launcher for Window Maker Dock
Summary(pl.UTF-8):	Odpalacz Freeciva dla Doku Window Makera
Name:		wmciv
Version:	0.2
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.chez.com/soap/wmciv/%{name}-%{version}.tar.gz
# Source0-md5:	df737598c616286d71e904a9f9c01f4b
Source1:	%{name}.desktop
URL:		http://www.chez.com/soap/wmciv/wmciv.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmciv is a dock-application designed for Window Maker. It allows you
to easily launch a Freeciv game. Any relatively recent version of
Freeciv should be supported.

After installing this package you have to create a directory named
.wmciv in your home directory and copy in it the files contained in
%{_docdir}/%{name}-%{version}/scripts/.

%description -l pl.UTF-8
wmciv jest dokowalnym apletem zaprojektowanym dla Window Makera.
Pozwala Ci na łatwe uruchamianie gry Freeciv. Powinien współpracować z
każdą, w miarę nową, wersją Freeciv.

Po zainstalowaniu tego pakietu musisz stworzyć katalog .wmciv w swoim
katalogu domowym i skopiować do niego pliki znajdujące się w
%{_docdir}/%{name}-%{version}/scripts/.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -I%{_includedir}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG scripts
%attr(755,root,root) %{_bindir}/wmciv
%{_desktopdir}/docklets/*
