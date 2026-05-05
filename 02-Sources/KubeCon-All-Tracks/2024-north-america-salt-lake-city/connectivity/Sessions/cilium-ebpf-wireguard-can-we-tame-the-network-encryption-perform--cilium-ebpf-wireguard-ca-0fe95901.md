---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Networking", "SRE Reliability"]
speakers: ["Daniel Borkmann", "Anton Protopopov", "Isovalent"]
sched_url: https://kccncna2024.sched.com/event/1i7lP/cilium-ebpf-wireguard-can-we-tame-the-network-encryption-performance-gap-daniel-borkmann-anton-protopopov-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Cilium%2C+eBPF%2C+WireGuard%3A+Can+We+Tame+the+Network+Encryption+Performance+Gap%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cilium, eBPF, WireGuard: Can We Tame the Network Encryption Performance Gap? - Daniel Borkmann & Anton Protopopov, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Daniel Borkmann, Anton Protopopov, Isovalent
- Schedule: https://kccncna2024.sched.com/event/1i7lP/cilium-ebpf-wireguard-can-we-tame-the-network-encryption-performance-gap-daniel-borkmann-anton-protopopov-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium%2C+eBPF%2C+WireGuard%3A+Can+We+Tame+the+Network+Encryption+Performance+Gap%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cilium, eBPF, WireGuard: Can We Tame the Network Encryption Performance Gap?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lP/cilium-ebpf-wireguard-can-we-tame-the-network-encryption-performance-gap-daniel-borkmann-anton-protopopov-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Cilium%2C+eBPF%2C+WireGuard%3A+Can+We+Tame+the+Network+Encryption+Performance+Gap%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oXhNVj80Z8A
- YouTube title: Cilium, eBPF, WireGuard: Can We Tame the Network Encryption Performanc... D. Borkmann, A. Protopopov
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cilium-ebpf-wireguard-can-we-tame-the-network-encryption-performance-g/oXhNVj80Z8A.txt
- Transcript chars: 26626
- Keywords: basically, kernel, traffic, device, actually, better, packet, performance, encryption, packets, single, devices, configure, receive, implementation, second, decryption, public

### Resumo baseado na transcript

okay it's time hello hello uh Welcome to our talk uh I'm Anton there is Danielle we're both engineers at isand which is now part of Cisco and island is a company behind siai and tbbf technology and Daniel happens to be co-creator of both cni and ebpf in Linux Kel so let's start have many slides today so year ago at uh this same conference Daniel presented a talk uh where he showed uh how to tune the kubernetes networking stack under selum uh to the maximum performance and

### Excerpt da transcript

okay it's time hello hello uh Welcome to our talk uh I'm Anton there is Danielle we're both engineers at isand which is now part of Cisco and island is a company behind siai and tbbf technology and Daniel happens to be co-creator of both cni and ebpf in Linux Kel so let's start have many slides today so year ago at uh this same conference Daniel presented a talk uh where he showed uh how to tune the kubernetes networking stack under selum uh to the maximum performance and this year we decided to add um another uh variable to this equation uh and this variable is encryption so um doesn't fit okay so there are definitely like use cases for encrypting traffic uh from uh application to application and probably the most common one is that you must be compliant with some framework and um yeah using the fact that there are so many people here so how many of you have to encrypt traffic in your clusters awesome awesome and how many of you do not know that it is super simple inum to enable transparent encryption okay um so transparent encryption uh means means that um we enable it once for the whole cluster and then applications without any configuration without any change to Applications uh they uh their traffic will be uh encrypted and for uh doing this on a cni level there are not actually too many options to do this it's IPC and Ward okay so IPC both have benefits uh IPC the first benefit probably is uh that it's compliant to many Frameworks and some environments require uh to use compliant uh implementations uh it is typically a little bit more complex in configuration than wiard but for the most part hides this so it's really easy to use it uh one thing users still need to do is provide uh keys and rotate them themselves so with wire guard it's a new encryption um system there are also benefits of it uh it's really simple really easy to understand uh this makes it uh more reliable in some cases uh because users can't misconfigure it and um it also provides automatic key rotation uh and uh in some cases it's easier for users to do this so in some cases wi guard is better than IPC for example if you consider applications which needs more throughput you can use wire guard in some cases uh IPC behaves better than um wiard if you need applications which need more request response uh then you can use IPC but it's on you to decide uh this talk is more focused on wire guard uh because just because it was too broad scope to to take both into account for for like 35 min
