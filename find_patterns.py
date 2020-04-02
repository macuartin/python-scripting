import sys, os, shutil, re, pwd, grp

properties_path = sys.argv[1]

for dirpath, dirname, filenames in os.walk(properties_path):
  for f in filenames:
    if re.search("^(application|secrets)-.*\.(properties|yml|yaml)$",f) is not None:
      propertie_ext = f.split(".")[-1]

print propertie_ext