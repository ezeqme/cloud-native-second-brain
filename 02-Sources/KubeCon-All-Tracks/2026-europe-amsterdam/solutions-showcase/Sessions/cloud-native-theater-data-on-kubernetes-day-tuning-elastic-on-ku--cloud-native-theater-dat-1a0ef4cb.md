---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Luuk Stolk and Artur Gromek", "ING"]
sched_url: https://kccnceu2026.sched.com/event/2EFzs/cloud-native-theater-data-on-kubernetes-day-tuning-elastic-on-kubernetes-how-assumptions-on-your-persistency-can-wreak-havoc-luuk-stolk-and-artur-gromek-ing
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+Tuning+Elastic+on+Kubernetes%3B+How+Assumptions+On+Your+Persistency+Can+Wreak+Havoc...+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Data on Kubernetes Day: Tuning Elastic on Kubernetes; How Assumptions On Your Persistency Can Wreak Havoc... - Luuk Stolk and Artur Gromek, ING

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Luuk Stolk and Artur Gromek, ING
- Schedule: https://kccnceu2026.sched.com/event/2EFzs/cloud-native-theater-data-on-kubernetes-day-tuning-elastic-on-kubernetes-how-assumptions-on-your-persistency-can-wreak-havoc-luuk-stolk-and-artur-gromek-ing
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+Tuning+Elastic+on+Kubernetes%3B+How+Assumptions+On+Your+Persistency+Can+Wreak+Havoc...+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Data on Kubernetes Day: Tuning Elastic on Kubernetes; How Assumptions On Your Persistency Can Wreak Havoc....

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzs/cloud-native-theater-data-on-kubernetes-day-tuning-elastic-on-kubernetes-how-assumptions-on-your-persistency-can-wreak-havoc-luuk-stolk-and-artur-gromek-ing
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+Tuning+Elastic+on+Kubernetes%3B+How+Assumptions+On+Your+Persistency+Can+Wreak+Havoc...+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LFuEq70lZdo
- YouTube title: Cloud Native Theater | Data on Kubernetes Day: Tuning Elastic on Kube... Luuk Stolk and Artur Gromek
- Match score: 0.777
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-data-on-kubernetes-day-tuning-elastic-on-kubernet/LFuEq70lZdo.txt
- Transcript chars: 20562
- Keywords: elastic, performance, storage, course, testing, basically, replica, platform, portworks, cluster, indeed, consumers, actually, started, provide, journal, clusters, replication

### Resumo baseado na transcript

In 2019, I joined G container hosted platform team and together with Luke, we've been building uh modern cloudnative infrastructure for ING group. I have been working uh for ING since 1992, so quite a few years already in various roles from application developer to solution architect to uh indeed engineer in the cloud native uh space. Um, it's a standardized uh Kubernetes hosting platform based on Open Shift. can tell uh thousands of teams thousands of namespaces nearly uh nearly 65,000 pods running on it but also 100% uptime and zero security breaches, which of course is uh um very important especially because we also host components that are part of of critical So on the on the left hand side you can see the uh the the instance of for stateless workloads where we provide the kubernetes platform u with a namespace as a service layer on it. So there's those are uh configurations, security controls, APIs etc that we provide to make the platform compliant and consumable and then consumers can request a name space via the portal as I uh as I explained and of course these uh stateless applications they

### Excerpt da transcript

Good afternoon. Thank you for uh joining our talk on uh tuning elastic on Kubernetes. Um yeah, Arur and I both work for ING. Maybe Arthur, you want to give? >> Yeah, I I'll try to say a few words about myself. So, my name is Arthur Groc. Uh I work as a DevOps engineer for ING Cahabs Poland. I've been in ING since 2013. In 2019, I joined G container hosted platform team and together with Luke, we've been building uh modern cloudnative infrastructure for ING group. >> Luke, maybe you're you talk. >> Yep. So, my name is Luke Stalk. I have been working uh for ING since 1992, so quite a few years already in various roles from application developer to solution architect to uh indeed engineer in the cloud native uh space. Um yeah, we would like to take you on a a quick journey starting uh with consumers suffering from uh from bad performing elastic uh stacks on uh on on Kubernetes until uh the implementation of fixes that that actually got the uh increased performance to uh to a to a reasonable uh level. Um but yeah, before we dive into the uh uh into the details of it, um maybe it's good to first provide some some context.

Um first of all about ING. Um yeah, as you can tell by uh by the facts and figures, um ING uh is is uh is a large um large bank operating on on a global level in more than 100 100 countries. um our 30 million customers um 60,000 employees so yeah very large um and yeah with that of course that uh comes a uh quite a large IT uh landscape at at scale um where uh indeed one-third of the people are uh are working in uh in tech among us um yeah a large amount of the the IT is is running in a private cloud, the ING private cloud, short called IPC. Um, yeah, that's also where the main Kubernetes platform at ING uh runs. Um, yeah, it started back in 2017. So, yeah, we were there from the beginning uh more or less. Um, and it's called the ING container hosting uh platform. Um, it's a standardized uh Kubernetes hosting platform based on Open Shift. Um yeah, we've got two distinct offerings. U one is um a multi-tenant cluster setup uh for stateless workloads and um also a range of dedicated clusters where uh hosting where we're hosting data services.

So for this for the stateful uh workloads um yeah being in in banking being a financial institution uh uh things like risk and compliance are uh uh of of of of a high essence. Um so yeah we provide a zero trust privilege access uh model but which basically means that that no person can uh can access the cl
