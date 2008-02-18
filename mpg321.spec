%define name mpg321
%define version 0.2.10
%define release %mkrel 6

Summary:	Mpg123-clone
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPL
URL: 		http://sourceforge.net/projects/mpg321
Source: 	http://prdownloads.sourceforge.net/mpg321/%name-%version.tar.bz2 
BuildRequires:	mad-devel >= 0.13 libao-devel >= 0.8.0 perl
BuildRequires:  libid3tag-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
#Provides:	mpg123
#Obsoletes:	mpg123

%description
mpg321 is a Free clone of mpg123, a command-line MP3 player. It is designed to
be a drop-in replacement for mpg123, and therefore its interface has been
designed around that of mpg123, without using any of its code. mpg321 has been
designed for use with frontends such as gqmpeg, although it is just as useful
on the command-line. Unlike mpg123, it supports ESD and ALSA output without
recompiling, and it does all MP3 decoding with only fixed-point math by using
the mad MPEG audio decoder library.
	
%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
#fix path in man page
perl -pi -e "s!/usr/share/doc/mpg321!/usr/share/doc/mpg321-%{version}!" mpg321.1

%build

%configure2_5x --enable-mpg123-symlink=no # Uncomment option once mainstream.
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

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


