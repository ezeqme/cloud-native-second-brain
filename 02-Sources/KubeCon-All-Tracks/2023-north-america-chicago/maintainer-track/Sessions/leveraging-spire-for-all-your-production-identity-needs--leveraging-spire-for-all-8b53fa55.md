---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Ryan Turner", "Uber", "Chirag Kapadia", "Uber Technologies", "Inc"]
sched_url: https://kccncna2023.sched.com/event/1R2th/leveraging-spire-for-all-your-production-identity-needs-ryan-turner-uber-chirag-kapadia-uber-technologies-inc
youtube_search_url: https://www.youtube.com/results?search_query=Leveraging+SPIRE+for+All+Your+Production+Identity+Needs+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Leveraging SPIRE for All Your Production Identity Needs - Ryan Turner, Uber & Chirag Kapadia, Uber Technologies, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Ryan Turner, Uber, Chirag Kapadia, Uber Technologies, Inc
- Schedule: https://kccncna2023.sched.com/event/1R2th/leveraging-spire-for-all-your-production-identity-needs-ryan-turner-uber-chirag-kapadia-uber-technologies-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Leveraging+SPIRE+for+All+Your+Production+Identity+Needs+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Leveraging SPIRE for All Your Production Identity Needs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2th/leveraging-spire-for-all-your-production-identity-needs-ryan-turner-uber-chirag-kapadia-uber-technologies-inc
- YouTube search: https://www.youtube.com/results?search_query=Leveraging+SPIRE+for+All+Your+Production+Identity+Needs+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QKWxkXfnKRs
- YouTube title: Leveraging SPIRE for All Your Production Identity Needs - Ryan Turner & Chirag Kapadia
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/leveraging-spire-for-all-your-production-identity-needs/QKWxkXfnKRs.txt
- Transcript chars: 29084
- Keywords: server, workload, identity, spiffy, certificate, plugin, subject, certificates, container, database, credential, composer, workloads, client, signing, plug-in, reloader, running

### Resumo baseado na transcript

hello everyone good afternoon I'm chak karia and I'm a software engineer at Uber and I have my colleague Ryan Turner with me who's a maintainer on the Spire project and today we'll be presenting how you can leverage Spire for all your production identity needs so this will be the agenda for today's session uh we'll start with an overview of spiffy and Spire then talk about SP architecture plugins and x509 certificates we'll then our use case for Mutual TLS encrypted MySQL connections using Spire along with the

### Excerpt da transcript

hello everyone good afternoon I'm chak karia and I'm a software engineer at Uber and I have my colleague Ryan Turner with me who's a maintainer on the Spire project and today we'll be presenting how you can leverage Spire for all your production identity needs so this will be the agenda for today's session uh we'll start with an overview of spiffy and Spire then talk about SP architecture plugins and x509 certificates we'll then our use case for Mutual TLS encrypted MySQL connections using Spire along with the demo so let's get started so what's spiffy it stands for secure production identity framework for everyone which is a set of standards for securely issuing identity to workloads it consists of three main components uh first is the spiffy ID which is a URI string that uniquely represents the name or ID of a workload and workload here could be any anything like a web server a database a micros service or any single piece of software the spiffy ID URI uh format is spiffy colon dou SL followed by the trust domain and path uh the trust domain here represents the trust root of the system uh which for example could be the domain name for an organization and the path is unique for a workload the whole spfy ID string can thereby be used to uniquely identify a workload second is the spiffy verifiable identity document also known as swid uh it is a document which proves the identity of a workload uh it carries the spiffy ID and is used by a workload to identify itself um for example a workload trying to authenticate uh to to an API on a web server uh the current supported document types are x509 which is the format for for public key certificates and jot which is Json web token and lastly we have the workload API uh which is a set of API specifications for workloads to be able to securely fetch swits next we'll discuss spy uh which is short for spiffy runtime environment uh and it it provides production ready implementation of the spiffy apis uh primarily Spire works on two main processes around workloads uh that is workload registration and workload attestation registration is a way to tell Spire how to identify a workload uh and Spire uses that when it's trying to attest a workload uh attestation is a way for Spire to figure out details regarding who the process requesting an swi is and uses those details to find the corresponding registration information in order to issue an swid usually workloads use Spire issued swis to authenticate to other workloads for
