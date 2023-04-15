import subprocess

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
print(hwid)

# Mine hwid 20C6DA02-0A07-2DF5-5FF9-04421A2D6077