---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Yury Tsarev", "Steven Borrelli", "Upbound"]
sched_url: https://kccncchn2025.sched.com/event/1x5jS/resilient-multiregion-global-control-planes-with-crossplane-and-k8gb-yury-tsarev-steven-borrelli-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Resilient+Multiregion+Global+Control+Planes+With+Crossplane+and+K8gb+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Resilient Multiregion Global Control Planes With Crossplane and K8gb - Yury Tsarev & Steven Borrelli, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: China / Hong Kong
- Speakers: Yury Tsarev, Steven Borrelli, Upbound
- Schedule: https://kccncchn2025.sched.com/event/1x5jS/resilient-multiregion-global-control-planes-with-crossplane-and-k8gb-yury-tsarev-steven-borrelli-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Resilient+Multiregion+Global+Control+Planes+With+Crossplane+and+K8gb+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Resilient Multiregion Global Control Planes With Crossplane and K8gb.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5jS/resilient-multiregion-global-control-planes-with-crossplane-and-k8gb-yury-tsarev-steven-borrelli-upbound
- YouTube search: https://www.youtube.com/results?search_query=Resilient+Multiregion+Global+Control+Planes+With+Crossplane+and+K8gb+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L9mRWljLnzw
- YouTube title: Resilient Multiregion Global Control Planes With Crossplane and K8gb - Yury Tsarev & Steven Borrelli
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/resilient-multiregion-global-control-planes-with-crossplane-and-k8gb/L9mRWljLnzw.txt
- Transcript chars: 28594
- Keywords: crossplane, cluster, global, actually, management, active, application, status, resources, infrastructure, failover, resource, passive, clusters, control, ingress, policies, currently

### Resumo baseado na transcript

I'm a principal solutions architect at Upbound and uh this is my colleague Yuri. Uh so we are from Upbound and if you heard about Abound you can you probably know that we are creators as a company. folks who are building these platforms and it's very important for us like how do restructure these so that they scale and also that we could fail them over. Um but basically the idea for this demo today and the project that we're working on is we want to work not only do workloads but also infrastructure provisioning. the chief architects of the KGB project this is a global load balancer that runs on a Kubernetes cluster um and the second one is crossplane which has been mentioned a few times here already at the conference uh crossplane is a universal control plane uh it extends Kubernetes to be able to manage anything Okay, so this looks like a very complex diagram.

### Excerpt da transcript

Hello everyone. Welcome to our talk. We're about building globally resilient control planes. Um I'm Steven Burley. I'm a principal solutions architect at Upbound and uh this is my colleague Yuri. Hi everyone. I'm Yuri. Thanks a lot for joining our talk today. Uh so we are from Upbound and if you heard about Abound you can you probably know that we are creators as a company. We are creators of crossplane project and uh uh today we are going to combine the power of two projects of crossplane and KGB and KGB is a a project that was created by me in a organization uh before a bound in ABSA and uh basically currently it's also CNCF sandbox project and I'm really excited about the opportunity today to show the powerful combination of two projects coming together. So Stephen, please kick us off. All right. Hello folks. So the first thing I want to talk about is just some of the really basics of building infrastructure platforms. Um and this is really simplified. Um but just talking about some of the kinds of major use cases that we see.

Um the first one is obviously end users and these are the folks who consume the applications that the organization provides. Uh the second group of users um are developers. um as platform engineers these are some of our pre you know our most important users uh we structure a lot of work around them and their main uh goals are to be able to deploy code um using CI/CD systems and also request infrastructure um you know this is a big thing for crossplane that allowing developers to self-service infrastructure and then finally uh platform engineers uh Yuri and I are both solution architects so we kind of do a lot in this role and this is basically the folks who are building these platforms and it's very important for us like how do restructure these so that they scale and also that we could fail them over. Um our goals today, we have a demo, we've written some code. Um but basically the idea for this demo today and the project that we're working on is we want to work not only do workloads but also infrastructure provisioning.

We actually want to have two clusters that's doing this. Um we want to have an active passive model even for the infrastructure management. Um and what we're going to do is we're going to key off the active and passive failover based on the health of the application that we're managing. Um and the way we're going to do active passive failover is we're going to do DNS-based right so that's part of the strength o
