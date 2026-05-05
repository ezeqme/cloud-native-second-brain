---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["John Belamaric", "Morten Torkildsen", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tx9D/more-nodes-more-problems-solving-multi-host-gputpu-scheduling-with-dynamic-resource-allocation-john-belamaric-morten-torkildsen-google
youtube_search_url: https://www.youtube.com/results?search_query=More+Nodes%2C+More+Problems%3A+Solving+Multi-Host+GPU%2FTPU+Scheduling+With+Dynamic+Resource+Allocation+CNCF+KubeCon+2025
slides: []
status: parsed
---

# More Nodes, More Problems: Solving Multi-Host GPU/TPU Scheduling With Dynamic Resource Allocation - John Belamaric & Morten Torkildsen, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United Kingdom / London
- Speakers: John Belamaric, Morten Torkildsen, Google
- Schedule: https://kccnceu2025.sched.com/event/1tx9D/more-nodes-more-problems-solving-multi-host-gputpu-scheduling-with-dynamic-resource-allocation-john-belamaric-morten-torkildsen-google
- Busca YouTube: https://www.youtube.com/results?search_query=More+Nodes%2C+More+Problems%3A+Solving+Multi-Host+GPU%2FTPU+Scheduling+With+Dynamic+Resource+Allocation+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre More Nodes, More Problems: Solving Multi-Host GPU/TPU Scheduling With Dynamic Resource Allocation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9D/more-nodes-more-problems-solving-multi-host-gputpu-scheduling-with-dynamic-resource-allocation-john-belamaric-morten-torkildsen-google
- YouTube search: https://www.youtube.com/results?search_query=More+Nodes%2C+More+Problems%3A+Solving+Multi-Host+GPU%2FTPU+Scheduling+With+Dynamic+Resource+Allocation+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YqIHESG0suI
- YouTube title: More Nodes, More Problems: Solving Multi-Host GPU/TPU Scheduli... John Belamaric & Morten Torkildsen
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/more-nodes-more-problems-solving-multi-host-gpu-tpu-scheduling-with-dy/YqIHESG0suI.txt
- Transcript chars: 24744
- Keywords: devices, resource, device, working, available, multiple, selector, schedule, request, claims, scheduler, features, capacity, resources, gpu, certain, mentioned, possible

### Resumo baseado na transcript

Um well uh today we're going to talk a little bit about some of the really future-looking things we're doing in the Kubernetes project. Um what we're going to show you today uh is only partly available today and some of it's coming in the release that's about to happen. Um I'm going to use uh TPUs as an example, but a lot of these same um problems uh apply also in GPU training issues, although they may solve the problems in different ways. Um so that that's not really the kind of self-healing we expect from a Kubernetes solution. But this dynamic resource allocation is a a new resource request API in Kubernetes that as I mentioned uh Patrick and Kevin and others have been working on for quite some time. So that means that the scheduleuler understands what's available in the cluster and this information is also available to the Kubernetes autoscaler which means that it can cons take devices in into consideration when it for autoscaling decisions uh which is one of the uh

### Excerpt da transcript

All right. Hello everybody. Uh welcome. Um uh pretty good turnout here. I hope you're not not too sleepy after lunch. Um well uh today we're going to talk a little bit about some of the really future-looking things we're doing in the Kubernetes project. Um what we're going to show you today uh is only partly available today and some of it's coming in the release that's about to happen. But um hopefully you'll you'll uh see some of the the great work that the community is doing um to to handle these more advanced use cases that we're seeing these days. Um my name is John Bellame. I'm from Google and I've been involved in Kubernetes for maybe seven or eight years. Um so uh but for the last year I've been working on DRRA um which was uh initiated by Patrick Oolie from Intel who's here in the third row and and Kevin Clues has done a ton of work on this as well but many other contributors um from the community. So we are uh you know we're all um we're we're all in it together here and with me. Yeah, my name is Morton.

I'm also from Google. Uh I've been involved with the communities project for like few years a little bit on and off and been working on dr for last six months roughly. All right. So let's see what we're uh what we're talking about here as far as these problems. I mean I think that the really simple way to put it is as workloads uh get larger when you're doing large training jobs or things like that you're using lots of accelerators. That means lots of nodes and of course lots of any kind of machine means more probability for failure. So more failure points more failures and um with some of these kind of coordinated mechanisms across nodes the failure of one node can kind of uh impact all of the nodes involved in the job. So how can Kubernetes help manage those type of situations? to kind of illustrate the the problems we're talking about. Um I'm going to use uh TPUs as an example, but a lot of these same um problems uh apply also in GPU training issues, although they may solve the problems in different ways.

Um we'll see a little bit of that later. and and uh but for now for our illustr illustration we're going to assume we have um 64 accelerators TPUs they're called um but they're similar to GPUs um and there's four per node and so we have 16 nodes um for for these particular uh jobs um or rather for for this particular cluster in our example and then we'll have several different jobs that are each using a portion of that cluster but not the wh
