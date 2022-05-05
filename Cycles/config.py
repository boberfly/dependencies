{

	"downloads" : [

		"https://github.com/blender/cycles/archive/refs/tags/v3.1.1.tar.gz",

	],

	"url" : "https://www.cycles-renderer.org/",

	"license" : "LICENSE",

	"dependencies" : [ "Boost", "OpenImageIO", "TBB", "Alembic", "Embree", "OpenColorIO", "OpenVDB", "OpenShadingLanguage" ],

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -DCMAKE_INSTALL_PREFIX={buildDir}/cycles"
			" -DCMAKE_PREFIX_PATH={buildDir}"
			" -DWITH_CYCLES_OPENIMAGEDENOISE=OFF"
			" -DWITH_CYCLES_DEVICE_CUDA=OFF"
			" -DWITH_CYCLES_DEVICE_OPTIX=OFF"
			" -DCMAKE_POSITION_INDEPENDENT_CODE=ON"
			" ..",
		"cd build && make install -j {jobs} VERBOSE=1",

		"mkdir -p {buildDir}/cycles/include",
		"cp -r build/bin {buildDir}/cycles",
		"cp -r build/lib {buildDir}/cycles",
		"cp -r build/shader {buildDir}/cycles",
		"cp -r build/source {buildDir}/cycles",
		"cd src && cp --parents */*.h */*/*.h {buildDir}/cycles/include",
		"cp -r third_party/atomic/* {buildDir}/cycles/include",
		"cp -r third_party/cuew/include/cuew.h {buildDir}/cycles/include/cuew.h",
		"cp -r third_party/hipew/include/hipew.h {buildDir}/cycles/include/hipew.h",
		"cp -r third_party/sky/*/*.h {buildDir}/cycles/include",
	],

	"manifest" : [

		"cycles",

	],

}
