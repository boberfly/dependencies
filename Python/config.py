{

	"downloads" : [ "https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz" ],

	"publicVariables" : {

		"pythonVersion" : "3.10",
		"pythonMajorVersion" : "3",
		"pythonMinorVersion" : "10",
		"pythonIncludeDir" : "{buildDir}/include/python{pythonVersion}",
		"pythonLibDir" : "{buildDir}/lib",

	},

	"url" : "https://www.python.org",

	"license" : "LICENSE",

	"dependencies" : [ "LibFFI" ],

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",
		"CPPFLAGS" : "-I{buildDir}/include",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"{environmentCommand} ./configure --prefix={buildDir} {libraryType} --enable-unicode=ucs4 --with-ensurepip=install --with-system-ffi",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/python",
		"bin/python*[0-9]",

		"include/python*",

		"lib/libpython*{sharedLibraryExtension}*",
		"lib/Python.framework*",
		"lib/python{pythonVersion}",

	],

	"variables" : {

		"libraryType" : "--enable-shared",
		"environmentCommand" : "",

	},

	"symbolicLinks" : [

		( "{buildDir}/bin/python", "python3" ),

	],

	"platform:linux" : {

		"variables" : {

			# Needed to build Python with OpenSSL 1.1.1 support on Centos 7
			"environmentCommand" : "CPPFLAGS=\"$(pkg-config --cflags openssl11)\" LDFLAGS=\"$(pkg-config --libs openssl11)\""

		}

	},

	"platform:macos" : {


		"variables" : {

			"libraryType" : "--enable-framework={buildDir}/lib",

		},

		"environment" : {

			"MACOSX_DEPLOYMENT_TARGET" : "11.0",

		},

		"publicVariables" : {


			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonMajorVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonVersion}" ),
			( "{buildDir}/lib/Python.framework/Versions/Current/lib/libpython{pythonMajorVersion}.dylib", "libpython{pythonMajorVersion}.{pythonMinorVersion}.dylib" ),
		],

	},

}
