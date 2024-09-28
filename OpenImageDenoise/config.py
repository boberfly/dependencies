{

	"downloads" : [

		"https://github.com/RenderKit/oidn/releases/download/v2.3.0/oidn-2.3.0.src.zip"

	],

	"url" : "https://www.openimagedenoise.org/",

	"license" : "LICENSE.txt",

	"dependencies" : [],

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -G {cmakeGenerator}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D Python_EXECUTABLE={buildDir}/bin/python"
			" -D OIDN_APPS=ON"
			" -D OIDN_APPS_OPENIMAGEIO=ON"
			" -D OIDN_LIBRARY_NAME=MoonrayOpenImageDenoise"
			" {extraArgs}"
			" ..",
		"cd build && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"cmake/OpenImageDenoise*",
		"include/OpenImageDenoise*",
		"lib/*",
		"bin/*",

	],

	"platform:linux" : {

		"environment" : {

			"PATH" : "{buildDir}/bin:$PATH",
			"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",
			"CUDACXX" : "/usr/local/cuda/bin/nvcc",

		},

		"publicVariables" : {

			"extraArgs" : " -D OIDN_DEVICE_CUDA=ON"

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

			"PATH" : "{buildDir}/lib;%PATH%",

		},

		"publicVariables" : {

			"extraArgs" : " -D OIDN_DEVICE_CUDA=ON"

		},

	},

}
