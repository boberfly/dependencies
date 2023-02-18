{

	"downloads" : [

		"https://github.com/OpenImageDenoise/oidn/releases/download/v2.2.2/oidn-2.2.2.src.tar.gz"

	],

	"url" : "https://www.openimagedenoise.org/",

	"license" : "LICENSE.txt",

	"dependencies" : ["ISPC"],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",

	},

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D TBB_ROOT={buildDir}"
			" -D Python_EXECUTABLE=${buildDir}/bin/python"
			" -D OIDN_APPS=OFF"
			" {extraArgs}"
			" ..",
		"cd gafferBuild && cmake --build . --config Release --target install -- -j {jobs}",

	],

	"manifest" : [

		"cmake/OpenImageDenoise*",
		"include/OpenImageDenoise*",
		"lib/*OpenImageDenoise*",

	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",
			"CUDACXX" : "/usr/local/cuda/bin/nvcc",

		},

		"publicVariables" : {

			"extraArgs" : ""

		},

	},

	"platform:osx" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",

		},

		"publicVariables" : {

			"extraArgs" : ""

		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}/lib;%PATH",

		},

		"publicVariables" : {

			"extraArgs" : ""

		},

	},

}
