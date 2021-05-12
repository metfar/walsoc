for f in ../pa/*py ; do n="${#f}";n=$((n-9));echo touch ${f:6:n}.js; done
