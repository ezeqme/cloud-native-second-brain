---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Lior Lieberman", "Google", "Igor Velichkovich", "Stealth Startup"]
sched_url: https://kccnceu2025.sched.com/event/1txER/encryption-identities-and-everything-in-between-building-secure-kubernetes-networks-lior-lieberman-google-igor-velichkovich-stealth-startup
youtube_search_url: https://www.youtube.com/results?search_query=Encryption%2C+Identities%2C+and+Everything+in+Between%3B+Building+Secure+Kubernetes+Networks+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Encryption, Identities, and Everything in Between; Building Secure Kubernetes Networks - Lior Lieberman, Google & Igor Velichkovich, Stealth Startup

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Lior Lieberman, Google, Igor Velichkovich, Stealth Startup
- Schedule: https://kccnceu2025.sched.com/event/1txER/encryption-identities-and-everything-in-between-building-secure-kubernetes-networks-lior-lieberman-google-igor-velichkovich-stealth-startup
- Busca YouTube: https://www.youtube.com/results?search_query=Encryption%2C+Identities%2C+and+Everything+in+Between%3B+Building+Secure+Kubernetes+Networks+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Encryption, Identities, and Everything in Between; Building Secure Kubernetes Networks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txER/encryption-identities-and-everything-in-between-building-secure-kubernetes-networks-lior-lieberman-google-igor-velichkovich-stealth-startup
- YouTube search: https://www.youtube.com/results?search_query=Encryption%2C+Identities%2C+and+Everything+in+Between%3B+Building+Secure+Kubernetes+Networks+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q15XbASxHM0
- YouTube title: Encryption, Identities, and Everything in Between; Building Se... Lior Lieberman & Igor Velichkovich
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/encryption-identities-and-everything-in-between-building-secure-kubern/Q15XbASxHM0.txt
- Transcript chars: 29532
- Keywords: network, policy, policies, identity, security, authorization, labels, traffic, cluster, support, obviously, identities, actually, access, account, standardization, control, namespace

### Resumo baseado na transcript

And today we're going to talk about encryption, identities, everything in between. Kind of some, you know, some tips on building secure Kubernetes networks and some of the hopes we're hoping to get out of this presentation and out of standardization efforts in this aspect. Um, the weak link thing is going to be a pattern that you'll see in the following examples where someone is able to get in through a weak link in your security and because of a lack of network segmentation, they're able to get to other more protected resources. 148 million people's personal information was stolen, including social security numbers and financial records. So, they tried to do their due diligence and they did a 10-month security assessment. So, it's designed for developers, namespace admins, app owners to control their traffic like maybe between a front-end pod and a backend pod or the backend pod and the database within that, you know, application and those microservices.

### Excerpt da transcript

Hey everyone. Uh, thanks for attending our talk. Um, I'm Leo Lieberman. I'm engineer lead at Google. And I'm Igor Velichkovich. I'm a engineer at a stealth startup focused on AI infrastructure. Yeah. And today we're going to talk about encryption, identities, everything in between. Kind of some, you know, some tips on building secure Kubernetes networks and some of the hopes we're hoping to get out of this presentation and out of standardization efforts in this aspect. But I'm gonna hand it off to Eager to kind of walk us through and you know get us into the domain. Yeah. So let's start with a story. Um so suppose you have this environment. You have some ingress coming into your cluster and a proxy pod. Um and you have a rate limit config. Pretty common setup, right? Um but now you have some issue with your rate limiter. It's not rate limiting what it should and it's overrate limiting other things. So you need to go and troubleshoot that. So you add a debug path and a debug pod because you remember that the rate limiter is based on headers.

So you add the debug pod to intercept some traffic and um try to see what's going on. That debug pod is meant to be temporarily lived and you do figure out what's wrong and fix your rate limit. Um but because it was supposed to be temporarily lived um it has broad unrestricted network access right you didn't mo bother to secure it um so you can see in the graph that debug pod can access everything in your cluster. So that ingress was exposed on the public internet and you forgot to clean it up. So now suppose someone gets into that debug pod and they start accessing your user information, payment information, transactions um and the attackers move all over your network because you don't have any segmentation. Um after this you have reputation and compliance issues that follow. Um that was a madeup story but this has happened many times in the past. So this is a good example. Um, this led to chip and EMV cards in the US. Um, they weren't really very popular before that, so had like a cultural impact.

Um, but attackers got into Target and they were able to steal 70 million people's PII, 40 million credit card numbers, and they got in through a weak link in a contractor, through an HVAC contractor that was using free anti malware software that was not robust enough. Um, the weak link thing is going to be a pattern that you'll see in the following examples where someone is able to get in through a weak link in your securi
