import platform
import os
import django
import datetime
# from PIL import __version__


# print("Current Pillow version is:", __version__)
# print("Pillow package path:", os.path.dirname(__file__))
print(f"Django version: {django.get_version()}")
print("Django package path:", os.path.dirname(django.__file__))

print(f"Python version: {platform.python_version()}")
print("Python package path:", os.path.dirname(platform.__file__))

log_filename = "log.txt"

if os.path.exists(log_filename):
    # read the existing log file and extract the version numbers
    with open(log_filename, "r") as log_file:
        lines = log_file.readlines()
        django_version = lines[1].split(": ")[1].strip()
        python_version = lines[3].split(": ")[1].strip()

    # compare the version numbers with the ones currently installed
    if django_version == django.get_version() and python_version == platform.python_version():
        # nothing has changed, exit the script
        exit()

# if we get here, the log file needs to be updated
with open(log_filename, "w") as log_file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"Log created at {timestamp}\n\n")

    log_file.write(f"Django version: {django.get_version()}\n")
    log_file.write("Django package path: " + os.path.dirname(django.__file__) + "\n\n")

    log_file.write(f"Python version: {platform.python_version()}\n")
    log_file.write("Python package path: " + os.path.dirname(platform.__file__) + "\n\n")





