Summary:	Mpg123-clone
Name:		mpg321
Version:	0.2.12
Release:	%mkrel 1
Group:		Sound
License:	GPL
URL: 		http://sourceforge.net/projects/mpg321
Source: 	http://kent.dl.sourceforge.net/project/mpg321/mpg321/%version/%name-%version-1.tar.gz
Patch0:		mpg321-help.patch
Patch1:		mpg321-0.2.12-fix-str-fmt.patch
Patch2:		mpg321-0.2.11-set-channel-mapping.patch
BuildRequires:	mad-devel >= 0.13 libao-devel >= 0.8.0 perl
BuildRequires:  libid3tag-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mpg321 is a Free clone of mpg123, a command-line MP3 player. It is designed to
be a drop-in replacement for mpg123, and therefore its interface has been
designed around that of mpg123, without using any of its code. mpg321 has been
designed for use with frontends such as gqmpeg, although it is just as useful
on the command-line. Unlike mpg123, it supports ESD and ALSA output without
recompiling, and it does all MP3 decoding with only fixed-point math by using
the mad MPEG audio decoder library.
	
%prep
%setup -qn %name-%version-1
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%configure2_5x --enable-mpg123-symlink=no # Uncomment option once mainstream.
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc AUTHORS COPYING ChangeLog HACKING NEWS README* TODO
%{_mandir}/man1/*
%{_bindir}/*

# Other option to test and create symlink.
#%post
#test -e /usr/bin/mpg123 || ln -s /usr/bin/mpg321 /usr/bin/mpg123
#%postun
#test -L /usr/bin/mpg123 && rm -f /usr/bin/mpg123


