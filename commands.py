import subprocess

def banner(text:str):
    data = f"""
```
    Your results 🚀
========================================
{text}
========================================
```
    """

    return data

def ls(param:str):
    raw = subprocess.run(['ls', *param], capture_output=True)
    stdout = raw.stdout.decode('UTF-8')
    
    data = banner(stdout)
    return data

def ps(param:str):
    raw = subprocess.run(['ps', *param], capture_output=True)
    stdout = raw.stdout.decode('UTF-8')
    
    data = banner(stdout)
    return data

def cat(param:str):
    raw = subprocess.run(['cat', *param], capture_output=True)
    stdout = raw.stdout.decode('UTF-8')
    
    data = banner(stdout)
    return data
