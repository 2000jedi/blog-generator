import os

import file_supervisor, static_server

markdown_directory = 'blog'
output_directory = 'serv'

files = file_supervisor.supervise(directory = markdown_directory)

file_supervisor.clean(output_directory, files)

for directory in files.keys():
    for f in files[directory]:
        file_supervisor.generate_pandoc(os.path.join(markdown_directory, directory), f, os.path.join(output_directory, directory))

static_server.serve(directory=output_directory)
