---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Observability", "Security", "Runtime Containers"]
speakers: ["Anna Kapuścińska", "Kornilios Kourtis", "Isovalent"]
sched_url: https://kccncna2024.sched.com/event/1i7ma/from-observability-to-enforcement-lessons-learned-implementing-ebpf-runtime-security-anna-kapuscinska-kornilios-kourtis-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=From+Observability+to+Enforcement%3A+Lessons+Learned+Implementing+eBPF+Runtime+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Observability to Enforcement: Lessons Learned Implementing eBPF Runtime Security - Anna Kapuścińska & Kornilios Kourtis, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Observability]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Salt Lake City
- Speakers: Anna Kapuścińska, Kornilios Kourtis, Isovalent
- Schedule: https://kccncna2024.sched.com/event/1i7ma/from-observability-to-enforcement-lessons-learned-implementing-ebpf-runtime-security-anna-kapuscinska-kornilios-kourtis-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=From+Observability+to+Enforcement%3A+Lessons+Learned+Implementing+eBPF+Runtime+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Observability to Enforcement: Lessons Learned Implementing eBPF Runtime Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ma/from-observability-to-enforcement-lessons-learned-implementing-ebpf-runtime-security-anna-kapuscinska-kornilios-kourtis-isovalent
- YouTube search: https://www.youtube.com/results?search_query=From+Observability+to+Enforcement%3A+Lessons+Learned+Implementing+eBPF+Runtime+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Hw469I5GKmY
- YouTube title: From Observability to Enforcement: Lessons Learned Implementing eBPF R... A. Kapuścińska, K. Kourtis
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-observability-to-enforcement-lessons-learned-implementing-ebpf-ru/Hw469I5GKmY.txt
- Transcript chars: 31484
- Keywords: tetragon, policy, kernel, enforcement, security, access, policies, observability, container, actually, running, filter, events, filtering, applications, application, another, secret

### Resumo baseado na transcript

uh welcome everyone to our talk um my name is Anna and today with me is my colleague Cornelius and we are going to talk about what we are working on so runtime security with ebpf so let's start with quick intro um my name is Anna I work at is of Valen on observability mainly observability for networking and security these days I'm focusing on uh tetragon which is observability tool that uh we develop Cornelius can you introduce yourself um hi hopefully you can hear me I'm Cornelius

### Excerpt da transcript

uh welcome everyone to our talk um my name is Anna and today with me is my colleague Cornelius and we are going to talk about what we are working on so runtime security with ebpf so let's start with quick intro um my name is Anna I work at is of Valen on observability mainly observability for networking and security these days I'm focusing on uh tetragon which is observability tool that uh we develop Cornelius can you introduce yourself um hi hopefully you can hear me I'm Cornelius I'm a software engineer uh withan now part of Cisco and I work on tetr all right so our goal today is to move from observability to enforcement uh we work on two aspects of runtime security with BPF observability and enforcement and observability in security context often means um inspecting interactions between applications between workloads and uh operating system um because um applications need to ask uh operating system for many many things they uh need to do but also many attack vectors uh essentially are abusing uh what application can do can ask operating system to do do uh for example um a pot might attempt to load a kernel module uh when it shouldn't really do it um or uh might access a secret file that it shouldn't really access uh when we are doing observability for security we can alert on such events and then uh ask a user a security engineer to investigate it to process data stor in some cm and do something with it we want to move step further and do enforcement so instead of just alerting on whenever a ker module is loaded we want to block it instead of just alerting a user whenever um a file is accessed a secret file is access accessed we want to just block it and not allow um the application to access this file uh in the first place uh so there are outline of our talk first we will uh briefly talk about how ebpf is used for security observability and enforcement we won't cover how ebpf Works under the hood this is not really necessary for the stock so if uh you don't know BPF internals don't worry about it uh then we'll cover how um to build a tetron enforcement policy and uh how this works in a kubernetes world so BPF Works within Linux kernel that means on a single machine kubernetes is a distributed system of them with a kubernetes cluster can have like thousand machines um distributed globally some interaction between these two worlds like local and globally distributed are interesting so we are going to cover this two and we show some uh exam more examples
