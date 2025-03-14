## Backups Security

Annualized Failure Rate - probability that a product completely breaks in a year (3%)

Assuming mirroring to 2 drives:

* New Annual Failure Rate = $(0.03)^2$ = $0.09%$
* assume independent failures
* you'll replace a bad drive quickly, time frame before good drive fails in one day = $(0.03)(0.03)(\frac{1}{365})$

What do you back up?

* File contents
* File system metadata
    * directory organization
    * ownership, timestamps, permission, etc
        * you cannot recover inode number (unique to file)
    * block structured, internally
        * back up these blocks instead of the file system level
        * slightly more efficient and simpler

What do you reclaim storage used for backups?

How to do backups more cheaply?

* Do them less often
* Do them to a cheaper device: flash --> harddisk --> tape
* Do them to a remote server
* Incremental Backups
    * First backup everything; later backup just the changes
        * How do we represent change?
            * filedata and metadata
            * block level backups
            * store differences between the two versions
* Deduplication at low level speeds up backups
    * this is like how cp will make a ptr to an existing file
* Automated data grooming (configure this)
* Compression
* Encryption, if you are backing up to remote servers
* Staging: flash --> disk --> tape --> remote
* Multiplexing, you have multiple servers and you backup all of them into a single backup server

## Recovery

* test your recovery procedure periodically
* checksumming cna make your recovery checking faster
    * make a checksum of the data and store it somewhere
    * when you test the backup, if the backup has same checksum, you are good to go

Version File Systems

* save operation on files (Files-11, OpenVMS)

```
cat foo.c';'1
cat foo.c';'2
```

Seasnet uses Snapshot Variant, WAFL(Seasnet), ZFS(Linux)

* there is no save operation
* the file system makes a snapshot periodically clones itself atomically

Users can look at old clones

* indirectly maintaining a pointer to the "write" log

`cd .snapshot` to see snapshots

* snapshots can contain inconsistent state (you are in the middle of changing a file)
* no changes to apps

## Security Basics

1. a security model(what you're defending)
2. a threat model(who's attacking and how)

Security is comprised of: CIA triad

* Confidentiality (Privacy) keeping info secret
* Integrity, no tampering from outside into system
* Availibility (service), the system stays up and you can get your work done

Identifiy the following in your security model:

1. assets  (data, software, firmware, hardware, network configuration)
2. vulnerabilities
3. threats

General Functions needed in most security models;

* Authentication (password, DUO key)
* Authorization (access control list ACLs)
* INtegrity (checksums)
* AUditing (log files)

### Threat Modeling and Classification: 

`risk analysis` which of these threats are worth your time and money

* insiders
* social engineering (masquerading as an insider)
* network attacks
* phishing - breaking into program by finding bugs in outdated browser (anonymous emails)
* drive-by downloads
* denial of service (DoS)
* buffer overruns
* cross-site scripting - browser pretends to be victim and access credentials
* prototype pollution
* device attacks - USB stick virus, usb chargers

### OWASP open world-wide application security project 2021 List of Web App Security Failures:

1. Broken access control (modifying URLS; cookies; JWT JSON Web Token)
2. Cryptofailures (http: ; weak crypto system; not validating certificates)
3. Injection (attacker misuses forms) Ex: Name: egger";drop all tables;"
4. Insecure design (not following good practices overall)
5. Security Misconfiguration (default accounts + passwords; maintanence ports open)
6. Vulnerable and Outdated components
7. ID + auth failures (allowing easy passwords; allowing password guessing)
8. Software and data integrity failures (not checking the software you use; bad access control to development repo)
9. logging and monitoring failures
10. Server-side request forgery (SSRF) client passes "weird" URL to server
