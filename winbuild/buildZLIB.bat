cd %~dp0%..\zlib-1.2.11

mkdir %BUILD_DIR%\doc\licenses
copy LICENSE %BUILD_DIR%\doc\licenses\libpng

mkdir gafferBuild
cd gafferBuild
del CMakeCache.txt

cmake -Wno-dev -G %CMAKE_GENERATOR% -DCMAKE_INSTALL_PREFIX=%BUILD_DIR% ..
cmake --build . --config Release --target install

cd %ROOT_DIR%