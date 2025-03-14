**## Backups Security

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
**## Backups Security

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

## Database Security:

Why database? Why not file systems?

* efficiency for search
* organization
* file system copy
    * is not atomic, this may be detrimental to some applications
    * it writes in small portions
* databases have transactions - it either happens or does not (atomic)
* all symbolic links point to a file
    * dependency
* dependencies are enforced in a db

## Database Models

### Relational Model

* a database is a collection of tables
* each table has a known, small set of named columns (each column is an attribute)
    * has a type: string, int, date
* has rows (one per "entity"), relation is the set of rows (no duplicate rows)
* key is a column in a table with no duplicates in the whole table
* null value is associated with 3 valued logic
    * salary < $100k?
    * yes/no/null

#### Relational Operators:

`Selection` table + predicate --> subtable

`S union T` set union (remove duplicates, columns must match)

`S intersect T` set intersection, columns must match

`S x T` cartesian product. Gets all combinations of combining columns of `S` and `T`

`projection` remove columns, remove duplicates

`S join T` takes all tuples in `S` and `T` that have same value in a common column

## SQL Structured Query Language

* set up database with schema (specifies tables and relationship between table + efficiency advice)

```
create table Student(
    ID int primary key,
    FamilyName varchar(255),
    GivenName varchar(255),
    Major varchar(64)
);
create table Grades(
    StudentID int foreign key references Student(ID),
    LetterGrade char(2),
    Course varchar(64)
)
```

`insert into Student(ID, FamilyName, GivenName, Major)values(405..., Chen, Nathan, Computer Science)`

`select FamilyName from Student where GivenName='Paul'`

Index is an auxillary table maintained by implementation to increase search speeds

### Entity Relation Model

* Entities is to row
* Atrributes is to columns
* Relationships is to foreign key

### Object Orientated Database

* Objects is to rows
* Atrributes is to columns
* Classes is to tables
* Methods

## NoSQL (Not Just SQL)

* key-value stores
* wide-column rows (lots of columns: decided dynamically)
* graph database
* document stores (JSON, XML, image)

## Cloud Firestore

* cloud-hosted NoSQL
* no schema
* documents (rows) contain key-value (columns) pairs. These have type determined dynamically
* collections (tables) of documents
* references (values) to documents or collection
* support for transaction

Thought Exercise:

Why doesn't a Firestore-based file-system work?

* Firestore is optimized for large collection of small documents

### Testing Security is different:

* ordinarily assume failures are "random"
* tests to match common usage
* bad guys are out to get you

1. static checking is more important
2. penetration teams are more important

Security often involves breaking abstraction boundaries

```
char goodWord[32];
char password[32];
...read_from_kb(password);
if (strcmp(password, goodword) == 0)
    login_ok();
```

By using page boundaries, attackers can know a character was a correct guess by the way the page loads

#### Spectre/Meltdown Attacks

* find a place where hardware branch prediction tells you about a key in some other process
    * caching of commonly used program/data
* common fix: cache less (hurts performance)
    * don't tell people about clocks

#### Risk Assessment:

* access costs of potential security failures and their probabilities
    * `cost * probability = value` will help you rank which problems you should prioritize
* retrofitting security can be expensive
* look at all phases (pre-requirements)
    * requirements
    * architecture
    * design/coding
    * testing/verification
    * fuzz testing
    * deployment
    * maintanence
* common problem areas
    * training
    * not negating risks
    * no threat model
    * SQL injection, cross-site scripting, DoS, repudiation, elevation of privilege
    * no default configuration or insecure configuration; logout doesn't really logout
    * not finding new threats

### Trust is based on

* trust in system developers
* suppliers of hardware, network, firmware, operating system, libraries
* operations staff
* users

