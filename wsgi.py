from app import app
from os import path, walk

extra_dirs = ['templates',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


if __name__ == "__main__":
	app.run(extra_files=extra_files)
