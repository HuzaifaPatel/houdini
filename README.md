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
   

# **YAML Documentation**

### Network

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `bridge`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `Host`

### read_only (read only filesystem)

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `True`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `False`


### security_opt

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `["no-new-privileges"]`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `[]`

### pid_mode

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `Host`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `null`

### cpu_shares

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '512'  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `any value`


### mem_limit

  &nbsp;&nbsp;&nbsp;&nbsp;**options:**  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '512 * 1024 * 1024'  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `null`
