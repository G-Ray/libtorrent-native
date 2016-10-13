{
    "conditions": [
        [ 'OS=="win"', {
            'conditions': [
                # "openssl_root" is the directory on Windows of the OpenSSL files.
                # Check the "target_arch" variable to set good default values for
                # both 64-bit and 32-bit builds of the module.
                ['target_arch=="x64"', {
                    'variables': {
                        'openssl_root%': 'C:/OpenSSL-Win64'
                    },
                }, {
                    'variables': {
                        'openssl_root%': 'C:/OpenSSL-Win32'
                    },
                }],
            ]
        }]
    ],

    "targets": [
        {
            "target_name": "porla-libtorrent",
            "sources": [
                "src/libtorrent.cc",
                "src/add_torrent_params.cc",
                "src/bdecode.cc",
                "src/read_resume_data.cc",
                "src/session.cc"
            ],

            "include_dirs" : [
                "<!(node -e \"require('nan')\")",
                "C:/Libs/boost_1_61_0",
                "C:/Libs/libtorrent/include",
                '<(openssl_root)/include',
            ],
            'msvs_settings': {
                'VCCLCompilerTool': {
                    'AdditionalOptions': [ '/EHsc' ]
                }
            },
            "defines": [
                "_SCL_SECURE_NO_WARNINGS",
                "_UNICODE",
                "_WIN32",
                "_WIN32_WINNT=0x0600",
                "BOOST_ALL_NO_LIB",
                "NOMINMAX",
                "TORRENT_NO_DEPRECATE",
                "TORRENT_USE_OPENSSL",
                "UNICODE",
                "WIN32",
                "WIN32_LEAN_AND_MEAN"
            ],
            "libraries": [
                "-lC:/Libs/out/libboost_system-vc140-s-1_61.lib",
                "-lC:/Libs/out/libtorrent.lib",
                '-l<(openssl_root)/lib/libeay32.lib',
                '-l<(openssl_root)/lib/ssleay32.lib',
                "iphlpapi.lib"
            ],

            "conditions": [
                [ 'OS=="win"', {
                    "copies": [{
                        'destination': '<(module_root_dir)/build/Release',
                        'files': ['<(openssl_root)/libeay32.dll','<(openssl_root)/ssleay32.dll']
                    }]
                }]
            ]
        }
    ]
}
