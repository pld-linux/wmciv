Summary:	Freeciv launcher for Window Maker Dock
Summary(pl):	Odpalacz Freeciv dla Doku Window Makera
Name:		wmciv
Version:	0.2
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source:		http://www.chez.com/soap/wmciv/%{name}-%{version}.tar.gz
URL:		http://www.chez.com/soap/wmciv/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 	/usr/X11R6

%description
wmciv is a dock-application designed for Window Maker. It allows you to
easily launch a Freeciv game. Any relatively recent version of Freeciv 
should	be supported.

After installing this package you have to create a directory named .wmciv 
in your home directory and copy in it the files contained in 
%{_defaultdocdir}/%{name}-%{version}/scripts/.

%description -l pl
wmciv jest dokowalnym apletem zaprojektowanym dla Window Makera.
Pozwala Ci na ³atwe uruchamianie gry Freeciv. Powinien wspó³pracowaæ 
z ka¿d±, w miarê now±, wersj± Freeciv.

Po zainstalowaniu tego pakietu musisz stworzyæ katalog .wmciv 
w swoim katalogu domowym i skopiowaæ do niego pliki znajduj±ce siê
w %{_defaultdocdir}/%{name}-%{version}/scripts/.

%prep
%setup -q

%build

make CFLAGS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

make install DESTDIR=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGELOG 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz scripts

%attr(755,root,root) %{_bindir}/wmciv
