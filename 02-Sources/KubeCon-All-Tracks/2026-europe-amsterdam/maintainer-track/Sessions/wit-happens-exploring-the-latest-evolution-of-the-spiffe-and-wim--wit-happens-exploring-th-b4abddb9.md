---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Noah Stride", "Teleport", "Arndt Schwenkschuster", "Defakto Security"]
sched_url: https://kccnceu2026.sched.com/event/2EF5G/wit-happens-exploring-the-latest-evolution-of-the-spiffe-and-wimse-workload-identity-standards-noah-stride-teleport-arndt-schwenkschuster-defakto-security
youtube_search_url: https://www.youtube.com/results?search_query=WIT+Happens%3A+Exploring+the+Latest+Evolution+of+the+SPIFFE+and+WIMSE+Workload+Identity+Standards.+CNCF+KubeCon+2026
slides: []
status: parsed
---

# WIT Happens: Exploring the Latest Evolution of the SPIFFE and WIMSE Workload Identity Standards. - Noah Stride, Teleport & Arndt Schwenkschuster, Defakto Security

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Noah Stride, Teleport, Arndt Schwenkschuster, Defakto Security
- Schedule: https://kccnceu2026.sched.com/event/2EF5G/wit-happens-exploring-the-latest-evolution-of-the-spiffe-and-wimse-workload-identity-standards-noah-stride-teleport-arndt-schwenkschuster-defakto-security
- Busca YouTube: https://www.youtube.com/results?search_query=WIT+Happens%3A+Exploring+the+Latest+Evolution+of+the+SPIFFE+and+WIMSE+Workload+Identity+Standards.+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre WIT Happens: Exploring the Latest Evolution of the SPIFFE and WIMSE Workload Identity Standards..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5G/wit-happens-exploring-the-latest-evolution-of-the-spiffe-and-wimse-workload-identity-standards-noah-stride-teleport-arndt-schwenkschuster-defakto-security
- YouTube search: https://www.youtube.com/results?search_query=WIT+Happens%3A+Exploring+the+Latest+Evolution+of+the+SPIFFE+and+WIMSE+Workload+Identity+Standards.+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bwCYG6NWh44
- YouTube title: WIT Happens: Exploring the Latest Evolution of the SPIFFE and... Noah Stride & Arndt Schwenkschuster
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/wit-happens-exploring-the-latest-evolution-of-the-spiffe-and-wimse-wor/bwCYG6NWh44.txt
- Transcript chars: 25686
- Keywords: spiffe, workload, identity, certificate, client, public, possession, actually, security, signature, server, particularly, standards, credential, called, workloads, standard, private

### Resumo baseado na transcript

Well, welcome to WIT Happens, exploring the latest evolution of the SPIFFE and SPIRE workload identity standards. Today, we'll be taking a brief recap of SPIFFE and then we'll be talking about the upcoming WIT SVID credential. Um legacy techniques for identifying workloads and infrastructure simply just don't scale, right? Um the reason this is an IETF is because it benefits from a lot of related security standards and knowledge. Currently, we focus on architecture, securing service-to-service traffic, and also document existing workload identity patterns. Now, we can then pass that client certificate forward in a header, but this kind of introduces its own security concerns and challenges.

### Excerpt da transcript

Cool. Well, welcome to WIT Happens, exploring the latest evolution of the SPIFFE and SPIRE workload identity standards. Today, we'll be taking a brief recap of SPIFFE and then we'll be talking about the upcoming WIT SVID credential. I'm Noah Stride and I'm the lead of machine and workload identity at a vendor called Teleport. I'm also a member of the SPIFFE steering committee and a maintainer of the SPIFFE specification. I'm joined here today by Arn. Hi, I'm Arn. I'm a software engineer and standards architect at DeFactor Security. Also, like Noah, I'm steering committee member and maintainer for SPIFFE and and I I'm also active at the OAuth and WIMSE working groups at the IETF. Cool. So, a quick refresher on SPIFFE. I'd be interested, kind of hands in the air, who has SPIFFE deployed in their organization today? Great. Cool. So, SPIFFE, the Secure Production Identity Framework for Everyone. The official uh definition is a set of open source standards for securely identifying software systems in dynamic and heterogeneous environments, which is not easy to say quick.

>> [laughter] >> Um there's two parts of that I'd like to zoom in on. The first is software systems. I think in common parlance today we'd say workloads, but we're referring to running code running anywhere, right? We're talking about virtual machines, containers, serverless functions, uh like physical machines, right? The list goes on and on. The other part, dynamic and heterogeneous, which I might be pronouncing incorrectly. Um kind of to me refers to modern infrastructure, right? In modern infrastructure, lots of organizations were split across uh you know, on-prem, multiple cloud providers, and the dynamic part, you know, workloads are constantly spooling up and down. Um legacy techniques for identifying workloads and infrastructure simply just don't scale, right? Now, SPIFFE is just a specification, it is not an implementation. The most commonly well-known sort of uh implementation will be SPIRE. So, this is a CNCF graduate project, but there's also other implementations from vendors available and such.

So, what does SPIFFE define? SPIFFE defines many, many things. Uh some implementations will only implement part of the spec. Some of them will implement all of the spec. For the purposes of today's conversation, the most interesting part to us is the SPIFFE ID and the SPIFFE verifiable identity document. So, the SPIFFE ID, this is really foundational to all parts of the SPIFFE specificati
