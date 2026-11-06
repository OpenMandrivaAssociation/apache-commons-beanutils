Name:		apache-commons-beanutils
Version:	1.11.0
Release:	1
Summary:	Utility methods for reading and writing JavaBeans properties
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-beanutils/
Source0:	https://github.com/apache/commons-beanutils/archive/refs/tags/rel/commons-beanutils-%{version}.tar.gz#/commons-beanutils-%{version}.tar.gz

BuildArch:	noarch
# The site checkout profile is active when site-content is absent, and
# antrun is on the sysjar keep list.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
BuildRequires:	mvn(org.apache:apache:pom::)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(commons-collections:commons-collections)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-beanutils --link %{name}

%description
Apache Commons BeanUtils wraps reflection and introspection for
JavaBeans. 1.11.0 needs Java 8 and adds
SuppressPropertiesBeanIntrospector.SUPPRESS_DECLARING_CLASS.
BeanComparator and ResultSetIterator throw a narrower exception
instead of RuntimeException. Tests are skipped.

%prep
%autosetup -n commons-beanutils-rel-commons-beanutils-%{version}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt README.md
