---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccnceu2026.sched.com/event/2CVzO/real-world-supply-chain-security-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Real-World+Supply-Chain+Security+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Real-World Supply-Chain Security - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccnceu2026.sched.com/event/2CVzO/real-world-supply-chain-security-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Real-World+Supply-Chain+Security+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Real-World Supply-Chain Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzO/real-world-supply-chain-security-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Real-World+Supply-Chain+Security+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1Pd28J4kpN8
- YouTube title: Real-World Supply-Chain Security - Alex Leong, Buoyant
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/real-world-supply-chain-security/1Pd28J4kpN8.txt
- Transcript chars: 29429
- Keywords: software, supply, images, information, documents, vulnerabilities, attestations, buoyant, consumers, security, registry, running, signed, enterprise, sbombs, document, signatures, called

### Resumo baseado na transcript

Uh Buoyant is the creator of the linkerd service mesh and I have been working on linkerd for just over 10 years now. Um and kind of in addition to that there is also something called the buoyant enterprise for linkard or bellbe uh which is an enterprise distribution of linkerty created by buoyant. Uh so we're going to talk about what is supply chain security, why does it matter, why should you care, and how uh how does it work and how do you use it? And we we've seen this uh time and again when some dependency way down in your in your dependency tree has a problem that can affect you. Uh it depends on the container that you're running inside the operating system that you're running on the hardware that you're running on the networking stack that you're running on CNI plugins uh etc etc depends on Kubernetes depends on any APIs that you interact with or utilities that you use. So ideally, supply chain security would mean that we can say here is our software.

### Excerpt da transcript

Hi everyone, welcome. This is supply chain security in the real world. Uh so my name is Alex Leong. I am a software engineer at a company called Buoyant. Uh Buoyant is the creator of the linkerd service mesh and I have been working on linkerd for just over 10 years now. So it's been a big part of my life for for a really long time. uh and uh service meshes uh obviously as well. Um and so why am I here talking about supply chain security? Well, let me give you a little bit of context to understand that. Um so, linkerd itself is a service mesh. It's an open source project. It's part of the CNCF. It's one of the graduated projects. It was actually the first service mesh. Uh very very proud of that. Um and kind of in addition to that there is also something called the buoyant enterprise for linkard or bellbe uh which is an enterprise distribution of linkerty created by buoyant. So I have the uh the privilege of working on both of these things. I spend some of my time as an open- source uh project link maintainer and and part of my time working on this enterprise distribution.

And one of the things that really differentiates the enterprise distribution uh from the open source is the fact that we do a lot of supply chain security. Uh this is something that you know is is very important for enterprises. And so that's a big the big piece of the value there. So over the past maybe year or so, I've learned a lot about the supply chain security ecosystem and what tools are out there, how people are interacting with them, how to to use them. And so I wanted to share what what I've learned uh about that ecosystem which is I think is really rapidly evolving right now. Um and so all of this is kind of going to be mostly from the perspective of Buoyant as a software producer. But in order to understand that in order to do that effectively you also really have to think about software consumers the people who are who are using that software. So kind of by show of hands, who here considers yourself a software producer? I would say most people. Who considers yourself a software consumer?

Should be everybody, right? Everybody is a software consumer. So you're always going to be running software and you want to know what software you're running and want to know that it's secure. So that's that's uh uh what I'm going to be mostly talking about today. Uh so we're going to talk about what is supply chain security, why does it matter, why should you care, and how uh how does it w
