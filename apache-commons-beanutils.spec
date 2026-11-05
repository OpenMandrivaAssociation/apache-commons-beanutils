Name:		apache-commons-beanutils
Version:	1.9.4
Release:	1
Summary:	Utility methods for reading and writing JavaBeans properties
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-beanutils/
Source0:	https://archive.apache.org/dist/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(commons-collections:commons-collections)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-beanutils --link %{name}

%description
Apache Commons BeanUtils wraps reflection and introspection for
JavaBeans. 1.9.4 adds SuppressPropertiesBeanIntrospector, which
Velocity Tools imports. Commons Parent 47 is not used.

%prep
%autosetup -n commons-beanutils-%{version}-src
# Parent 47 is not the packaged commons-parent. Flattening drops the
# versionless site plugins that parent would otherwise keep.
python - <<'PY'
import xml.etree.ElementTree as ET
NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", NS)

def local(tag):
    return tag.split("}", 1)[-1]

tree = ET.parse("pom.xml")
root = tree.getroot()
for node in list(root):
    if local(node.tag) == "parent":
        root.remove(node)
tree.write("pom.xml", encoding="utf-8", xml_declaration=True)
PY

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt README.md
