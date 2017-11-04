#!/usr/bin/python3
import os,subprocess,re,tempfile,socket,uuid,datetime

def isClearRsaPrivateKey(filename: str):
  f = open(filename)
  lines = f.readlines()
  m = re.compile("BEGIN RSA PRIVATE KEY").search(lines[0])
  if m is None: return False
  m = re.compile("ENCRYPTED").search(lines[1])
  if m is None: return True;
  return False

def isOpenSshPublicKeyFile(filename: str):
  f = open(filename)
  lines = f.readlines()
  m = re.compile("^ssh-rsa ").search(lines[0])
  return m is not None

def rsaPrivateKeyFileToRsaPublicKey(filename:str):
  opensslRsa = subprocess.run(["openssl", "rsa", "-pubout", "-RSAPublicKey_out", "-in", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  rsaPublicKey = opensslRsa.stdout.decode("ascii")
  return rsaPublicKey


def rsaPublicKeyToOpenSshPublicKey(rsaPublicKey:str):
  temporaryFile = tempfile.NamedTemporaryFile(delete=False)
  temporaryFile.write(rsaPublicKey.encode("ascii"))
  temporaryFile.close()
  sshKeyGenProcess = subprocess.run(["ssh-keygen", "-i", "-m", "PEM", "-f", temporaryFile.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  openSshPublicKey = sshKeyGenProcess.stdout.decode("ascii")
  return openSshPublicKey

def openSshPublicKeyToFingerprint(openSshPublicKey:str):
  sshKeyGenFingerprint = subprocess.Popen(["ssh-keygen", "-l", "-E", "md5", "-f", "-"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  fingerprintLine = sshKeyGenFingerprint.communicate(openSshPublicKey.encode("ascii"))[0].decode("ascii")
  return parseFingerprintLine(fingerprintLine)

def openSshPublicKeyFileToFingerprint(filename:str):
  return openSshPublicKeyToFingerprint(open(filename).read())

def rsaPrivateKeyFileToFingerprint(filename: str):
  rsaPublicKey = rsaPrivateKeyFileToRsaPublicKey(filename)
  openSshPublicKey = rsaPublicKeyToOpenSshPublicKey(rsaPublicKey)
  fingerprint = openSshPublicKeyToFingerprint(openSshPublicKey)
  return fingerprint

def parseFingerprintLine(fingerprintLine:str):
  m = re.compile("^([0-9]+) +MD5:([0-9A-Fa-f:]+) +(.*)$").match(fingerprintLine)
  bits = m.group(1)
  md5 = m.group(2)
  comment = m.group(3)
  return [bits, md5, comment]

if __name__ == "__main__":
  result = []
  macAddress = hex(uuid.getnode())[2:].zfill(12)
  hostname = socket.gethostname()
  datetime = datetime.datetime.now().isoformat()
  files = os.listdir(".")
  for filename in files:
    d = {}
    if not os.path.isfile(filename): continue
    d["datetime"] = datetime
    d["hostname"] = hostname
    d["macAddress"] = macAddress
    d["absolutePath"] = os.path.abspath(filename)
    try: 
      fingerprint = None
      if isClearRsaPrivateKey(filename):
        fingerprint = rsaPrivateKeyFileToFingerprint(filename)
        d["private"] = True
      elif isOpenSshPublicKeyFile(filename):
        fingerprint = openSshPublicKeyFileToFingerprint(filename)
        d["private"] = False
      else: continue
      d["bits"] = fingerprint[0]
      d["md5"] = fingerprint[1]
      d["comment"] = fingerprint[2]
      print(d)
    except UnicodeDecodeError as e:
      continue

