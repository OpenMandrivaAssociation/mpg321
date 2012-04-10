Summary:	Mpg123-clone
Name:		mpg321
Version:	0.3.2
Release:	1
Group:		Sound
License:	GPLv2+
URL:		http://sourceforge.net/projects/mpg321
Source:		http://downloads.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
Patch0:		mpg321-help.patch
Patch1:		mpg321-0.2.12-fix-str-fmt.patch
Patch2:		mpg321-0.2.11-set-channel-mapping.patch
BuildRequires:	mad-devel >= 0.13 
BuildRequires:	libao-devel >= 0.8.0
BuildRequires:	libid3tag-devel
BuildRequires:	libasound-devel

%description
mpg321 is a Free clone of mpg123, a command-line MP3 player. It is designed to
be a drop-in replacement for mpg123, and therefore its interface has been
designed around that of mpg123, without using any of its code. mpg321 has been
designed for use with frontends such as gqmpeg, although it is just as useful
on the command-line. Unlike mpg123, it supports ESD and ALSA output without
recompiling, and it does all MP3 decoding with only fixed-point math by using
the mad MPEG audio decoder library.


%prep
%setup -qn %{name}-%{version}-orig
%patch0 -p0
%patch1 -p0
%patch2 -p1
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r//' NEWS

%build
%configure2_5x --enable-mpg123-symlink=no # Uncomment option once mainstream.
%make

%install
%makeinstall_std

%files
%doc BUGS AUTHORS HACKING NEWS README* THANKS TODO
%{_mandir}/man1/*
%{_bindir}/*
