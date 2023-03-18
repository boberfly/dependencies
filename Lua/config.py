{

	"downloads" : [

		"https://www.lua.org/ftp/lua-5.4.6.tar.gz"

	],

	"url" : "https://www.lua.org/",

	"license" : "LICENSE",

	"dependencies" : [],

	"commands" : [

		"make generic MYCFLAGS=-fPIC MYLIBS=-ldl",
		"cp src/lua src/luac {buildDir}/bin",
		"cp src/lua.h src/luaconf.h src/lualib.h src/lauxlib.h src/lua.hpp {buildDir}/include",
		"cp src/liblua.a {buildDir}/lib",

	],

	"manifest" : [

		"bin/lua*",
		"include/lua*",
		"include/lauxlib.h"
		"lib/liblua*",

	],

}
