import os

def supervise(directory):
    # list all markdown files in the category folders in destinated directory
    files = {}

    if not (os.path.exists(directory) and os.path.isdir(directory)):
        return files
    categories = os.listdir(directory)
    for c in categories:
        if (os.path.isdir(os.path.join(directory, c))):
            files[c] = []
            files_raw = os.listdir(os.path.join(directory, c))
            for f in files_raw:
                if os.path.isfile(os.path.join(directory, c, f)) and f.split('.')[-1] == 'md':
                    files[c].append(f)
        
    return files

def generate_pandoc(directory, f, output_dir):
    file_real_path = os.path.realpath(os.path.join(directory, f))
    out_real_path  = os.path.realpath(os.path.join(output_dir, f[:-3] + ".html"))

    command = "pandoc -s -f markdown -t html %s --metadata pagetitle=\"%s\" -o %s -c '/style/markdown.css'" % (file_real_path, f[:-3], out_real_path)
    print(command)
    os.system(command)

def generate_index(out_dir, dirs):
    pass

def clean(out_dir, files):
    os.system("rm -r %s" % os.path.realpath(out_dir))
    os.system("mkdir %s" % os.path.realpath(out_dir))

    os.system("mkdir %s" % os.path.realpath(os.path.join(out_dir, "style")))
    os.system("cp ./style.css %s" % os.path.realpath(os.path.join(out_dir, "style", "markdown.css")))
    
    for d in files.keys():
        command = "mkdir %s" % os.path.realpath(os.path.join(out_dir, d))
        # print(command)
        os.system(command)
