# Client Server Computing

```mermaid
    graph LR
    client <-- network --> server
    style client fill:#900
    style server fill:#049
```

`Server` has authority of what happens to the clients. `Client` requests permission from the server through the `network` to do tasks.

`Node` and `React` environments are used to create client-server architechtures. They are built atop of GNU, Linux. Some concepts in common with emacs is:

* configuration
* quoting

## Alternatives to Client Server Systems:

### Peer-to-Peer (P2P)

* no single peer has all of the authority
* even if one peer goes down, the system can still run

```mermaid
    graph LR
    p1@{shape: circle} <--> network <--> p2@{shape: circle}
    p3@{shape: circle} <--> network <--> p4@{shape: circle}
    p5@{shape: circle} <--> network <--> p6@{shape: circle}
    style p1 fill:#900
    style p2 fill:#900
    style p3 fill:#900
    style p4 fill:#900
    style p5 fill:#900
    style p6 fill:#900
    style network fill:#049
```

### Primary-Secondary

* primary keeps track of what secondary does and tells them what to do. Primary has all of the authority.

```mermaid
    graph TB
        subgraph Secondaries
            direction TB
            s1@{shape: circle}
            s2@{shape: circle}
            s3@{shape: circle}
            s4@{shape: circle}
            s5@{shape: circle}
            s6@{shape: circle}
        end
    Primary ---> Secondaries
    style s1 fill:#900
    style s2 fill:#900
    style s3 fill:#900
    style s4 fill:#900
    style s5 fill:#900
    style s6 fill:#900
    style Primary fill:#049

```

## Issues with these Distributive Systems

`Performance`

* `throughput` how much useful work per second can the system do (important for server operators)
    * to improve throughput
        * do actions in parallel
        * do actions out of order
* `latency` time between request and response time (important to end users/clients)
    * to improve latency
        * clients can cache data

`Correctness`

* `serialization` take all actions done, put them in a serial order and use that order to explain observations
* Does the cache need to be correct?
    * can client code do useful work witho ut of date caches.
* `Cache Validation` expensive to fetch cache. An alternative is to fetch the timestamp of the last cache and compare current version of cache.

## Networking

Before the internet, there was `circuit switching`

```mermaid
    graph LR
        UCLA ---> CO1@{shape: circle, label: "Central Office"}
        CO1 ---> triangle@{shape: triangle, label: " "} ---> CO2@{shape: circle, label: "Central Office"}
        CO2 ---> MIT
        style UCLA fill:#049
        style CO1 fill:#850
        style CO2 fill:#850
        style triangle fill:#807
        style MIT fill:#900
```

* there was a reserved capcity
* this means there was gauranteed performance(throughput and latency)
* typically it transmitted at `20 kb/s`

`Packet Switching`

```mermaid
    graph LR
        subgraph UCLA
            p1@{label: " "}
            p2@{label: " "}
            p3@{label: " "}
            p4@{label: " "}
            p5@{label: " "}
        end
        UCLA --> r1@{shape: triangle, label: "UCLA Router"}
        r1 --> triangle@{shape: triangle, label: " "} ---> r2@{shape: triangle, label: "Mit Router"}
        r2 --> MIT
        style UCLA fill:#049
        style r1 fill:#850
        style r2 fill:#850
        style triangle fill:#807
        style MIT fill:#900
```

* messages were divided into `packets`
* there is no reservation of capacity
* packets were typically 1500 bytes

Packet Switching is `more effiecient` with `less setup`, but it was `less reliable`.

### 3 Problems with Packets

* they can be lost (router overload)
* they can be received out of order
* they can be duplicated (bridge/router misconfiguration)

```mermaid
    packet-beta
        0-4: "header"
        5-31: "for recipient"
```

`header` also `network overhead` is what the network uses to identify a packet.

The right part of the packet is the info that is being transmitted.

`Protocols` are rules for exchanging packets

## Internet Protocol Suite (Internet RFC, Request for Comments)

### Layers:

* Application Layer: app specific
* Transport Layer: data channels
* Internet Layer: packets
* Link layer: point-to-point

### Internet Layer

#### Internet Protocol (IPv4)

* connectionless
* header:
    * length
    * protocol number
    * source and destination address (32 bits each. Ex: 192.54.239.12. Each decimal between the periods is a byte)
    * `TTL` time to live or hop count. Each time a packet is transmitted this gets decremented. When it is0, the packet is ignored
    * checksum (16 bit) deals with hardware errors.

#### IPv6

* same as IPv4 with improvments
* 128 bit addresses instead of 32 bits

### Transport Layer

`UDP` User Datagram Protocol

* thin layer over IP

`TCP` Transmission Control Protocol

* data stream that is:
    * reliable
    * ordered
    * error-checked
* so it does:
    * divides stream into packets
    * flow control - makes sure data isn't transmitted too quickly
    * retransmission & reassembly

### Application Protocol

`RTP` real time protocol

* runs ontop of UDP. Does not use TCP because it jitters
* designed for video/audio

Examples:

* Zoom WebRTC (atop RTP)
* `HTTP` HyperText Transfer Protocol

1. `HTTP` protocol for exchanging interesting documents
2. `HTML` standard format for text multimedia document

HTTP is a super-simple protocol

* each request and response has a seperate TCP stream
* security was not in mind when HTTP was created. 
* HTTPS is the secure alternative.

