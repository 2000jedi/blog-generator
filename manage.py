import os

import json_parser, file_supervisor

global_settings = json_parser.parse('global.json')
if (global_settings == None):
    print("Unable to open `global.json`, halting.")
    exit(-1)

files = file_supervisor.supervise(directory = global_settings['BLOG_DIR'])

file_supervisor.clean(global_settings['OUTPUT_DIR'], files)

for directory in files.keys():
    for f in files[directory]:
        file_supervisor.generate_pandoc(os.path.join(global_settings['BLOG_DIR'], directory), f, os.path.join(global_settings['OUTPUT_DIR'], directory))

if (global_settings['STATIC_SERVER']):
    import static_server
    static_server.serve(directory = global_settings['OUTPUT_DIR'])
