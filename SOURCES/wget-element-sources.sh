if (( $# != 1 )) ; then
    echo "Usage: $0 <version>"
    return 1
fi

wget https://github.com/vector-im/element-web/archive/refs/tags/v$1.tar.gz -O element-web-$1.tar.gz
wget https://github.com/vector-im/element-desktop/archive/refs/tags/v$1.tar.gz -O element-desktop-$1.tar.gz
ls -lh element-*-$1.tar.gz
