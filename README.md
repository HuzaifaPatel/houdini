<h1 align="center">Houdini</h1>

<div align="center">
  <strong>Container Escape Artist</strong>
</div>

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

To enter Python 3 virtual environment, run:

```bash
python3 -m venv venv
. venv/bin/activate
```

## Tricks

| Trick          | Link                                            | Completion Status |
|----------      |----------                                       |----------|
| CVE-2024-21616 | https://nvd.nist.gov/vuln/detail/CVE-2023-21616 | Complete |
| CVE-2019-14271 | https://nvd.nist.gov/vuln/detail/CVE-2019-14271 | Complete |
| CVE-2019-5736  | https://nvd.nist.gov/vuln/detail/CVE-2019-5736  | Docker Version < 18.09.2 doesn't work. Socket doesn't start idk why |
| CVE-2018-15664 | https://nvd.nist.gov/vuln/detail/cve-2018-15664 | Incomplete |
| CVE-2022-0492  | https://nvd.nist.gov/vuln/detail/CVE-2022-0492  | Complete |


# **Houdini Documentation**

Dockerfile: takes a path to a dockerfile

  Dependency : Only two are implemented at the moment
  -   Server (must be at port 8000)
  -   File
   

# **Docker Config**

      

### Network

   Options:\
    - `Bridge`\
    - `Host`

  

### read_only (read only filesystem)

  Options:\
    - True\
    - False\

### security_opt

  Options:\
    - ["no-new-privileges"]\
    - []\

### pid_mode

  Options:\
    - Host\
    - None
