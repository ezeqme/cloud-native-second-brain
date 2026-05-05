---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Networking"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Rahul Joshi", "Sudeep Modi", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE3F/discontiguous-cidrs-for-dynamic-cluster-scaling-rahul-joshi-sudeep-modi-google
youtube_search_url: https://www.youtube.com/results?search_query=Discontiguous+CIDRs+for+Dynamic+Cluster+Scaling+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Discontiguous CIDRs for Dynamic Cluster Scaling - Rahul Joshi & Sudeep Modi, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Rahul Joshi, Sudeep Modi, Google
- Schedule: https://kccnceu2021.sched.com/event/iE3F/discontiguous-cidrs-for-dynamic-cluster-scaling-rahul-joshi-sudeep-modi-google
- Busca YouTube: https://www.youtube.com/results?search_query=Discontiguous+CIDRs+for+Dynamic+Cluster+Scaling+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Discontiguous CIDRs for Dynamic Cluster Scaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3F/discontiguous-cidrs-for-dynamic-cluster-scaling-rahul-joshi-sudeep-modi-google
- YouTube search: https://www.youtube.com/results?search_query=Discontiguous+CIDRs+for+Dynamic+Cluster+Scaling+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HgRJpV-jvGU
- YouTube title: Discontiguous CIDRs for Dynamic Cluster Scaling - Rahul Joshi & Sudeep Modi, Google
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/discontiguous-cidrs-for-dynamic-cluster-scaling/HgRJpV-jvGU.txt
- Transcript chars: 19640
- Keywords: cluster, traffic, allocate, proposal, network, allocator, addresses, ranges, allocation, external, controller, discontiguous, support, single, create, however, larger, another

### Resumo baseado na transcript

hello everyone welcome to our talk on discontiguous ciders for dynamic cluster scaling uh let's jump into some introductions my name is rahul zoshi i am a software engineer working at google on gk networking hello everyone my name is sudeep modi and i am a software engineer working in the same team as rahul gk networking and the two of us have been working on this problem for about over a year so what is the goal of the talk today we want to present our proposal to support parts uh pod sitters and certain cloud providers already do this as well as certain cni also have the ability to do this our motivation for this project is to support this feature out of the box from for kubernetes so that anybody can make use of this so we are actively working with sig network on refining this proposal we are iterating on this and figuring out what the final design should be and then the next step would be to implement which leaves you with a call to

### Excerpt da transcript

hello everyone welcome to our talk on discontiguous ciders for dynamic cluster scaling uh let's jump into some introductions my name is rahul zoshi i am a software engineer working at google on gk networking hello everyone my name is sudeep modi and i am a software engineer working in the same team as rahul gk networking and the two of us have been working on this problem for about over a year so what is the goal of the talk today we want to present our proposal to support discontiguous ranges for port ips and the reason why we want to support discontiguous ranges is to enable flexible ip address allocation as well as remove one of the major bottlenecks for scaling a cluster by the end of this talk our goal is that you understand the problem we are trying to solve you understand why it's important to solve this problem we'll introduce some of the difficulties and challenges in solving the problem and finally we are going to present a proposal on how to actually solve the problem so that's the agenda today we i'm going to talk about how kubernetes pod ip allocation is done one thing to note is i'm talking about vanilla open source kubernetes i'm not talking about some of the bells and whistles that cloud providers had and how kubernetes works out of the box basically i'm going to talk about some potential improvements that we can make to the way we do pod ip allocation today we are going to talk about cluster cider in kubernetes and cluster cider is this one single pod ip range that you provide today and then finally we're going to talk through our proposal on enhancing and supporting this contiguous spot ip ranges and finally we will talk about some of the ongoing work that's going on in the community as at the time of this recording so this is a typical way a cluster comes up for a customer you have on your network ip space and when you bring up a cluster kubernetes ask you to ask you this question give me a cluster slider the cluster slider is this one large range from which all pod ips are allocated and in our example cluster over here we have allocated a 17 range for this new cluster and this gives us roughly 32 000 ips for that cluster in addition to the cluster cider kubernetes also asks you to provide a node cider mass size the way this works is every single time a new node comes up the range allocator for kubernetes internally chops up the large cluster slider into blocks of the node zero mass size so in this case 24 is the node center mass size so
