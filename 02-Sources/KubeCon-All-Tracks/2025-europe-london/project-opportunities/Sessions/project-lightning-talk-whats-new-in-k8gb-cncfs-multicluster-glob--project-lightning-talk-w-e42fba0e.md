---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["Kubernetes Core", "Community Governance"]
speakers: ["Bradley Andersen", "Community Manager"]
sched_url: https://kccnceu2025.sched.com/event/1tcvf/project-lightning-talk-whats-new-in-k8gb-cncfs-multicluster-global-balancer-bradley-andersen-community-manager
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+k8gb%3A+CNCF%27s+Multicluster+Global+Balancer+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: What's New in k8gb: CNCF's Multicluster Global Balancer - Bradley Andersen, Community Manager

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Bradley Andersen, Community Manager
- Schedule: https://kccnceu2025.sched.com/event/1tcvf/project-lightning-talk-whats-new-in-k8gb-cncfs-multicluster-global-balancer-bradley-andersen-community-manager
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+k8gb%3A+CNCF%27s+Multicluster+Global+Balancer+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's New in k8gb: CNCF's Multicluster Global Balancer.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvf/project-lightning-talk-whats-new-in-k8gb-cncfs-multicluster-global-balancer-bradley-andersen-community-manager
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+k8gb%3A+CNCF%27s+Multicluster+Global+Balancer+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YMyrcqZ2sbU
- YouTube title: Project Lightning Talk: What's New in k8gb: CNCF's Multicluster Global Balancer - Bradley Andersen
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-whats-new-in-k8gb-cncfs-multicluster-global-bal/YMyrcqZ2sbU.txt
- Transcript chars: 5371
- Keywords: cluster, particular, region, global, little, operator, couple, already, ingress, balancer, application, sandbox, happening, health, number, everybody, update, multiple

### Resumo baseado na transcript

Um I'm here today to talk to you a little bit about KGB if you don't know much about it. Um and I'm going to tell you a little bit about uh where we're going and how you can get involved. We believe it's the only cloudnative uh Kubernetes global load b load balancer. So it's Kubernetes native application health checks and it commoditizes GLB for Kubernetes. So um if one if this region A cluster is down, region B cluster is going to know it's down, update DNS, and then nobody's going to get sent over to region A cluster until region A cluster uh resolves whatever its problem is. Two-time security slam finalist, perfect CLO monitor score, maintainers from Absa, Abbound, Katify, Accenture, contributors from Millennium, BCP, etc.

### Excerpt da transcript

Hi, welcome everybody to London. I'm Bradley Anderson. I'm a community uh manager at uh KGB. Um I'm here today to talk to you a little bit about KGB if you don't know much about it. Um and I'm going to tell you a little bit about uh where we're going and how you can get involved. I'm not seeing a timer here. Hey, there we go. So yeah, this is going to be our project update for for this particular KubeCon. Um, KGB is a global service load balancer. So think about if you've got um an application you want to service it in multiple u multiple geographies, maybe EU, maybe United States, maybe China. um you want to make sure that that thing is always up and you may want to make sure that people from China are getting something closer to where they live so that there's low latency. You want to make sure that somebody in the US is getting something close to them so that there's uh low latency. So KGB is uh is OSS. It's following the Kubernetes operator platform. I'll show a couple of things after uh with that.

So it's implemented with Kubernetes operators. So it's things that you know about already. It's implemented with a single GS um LB CRD to enable the global load balancing. I'll show one of those after. It is vendor neutral. It's environment agnostic and it's a CNCF sandbox project. We have recently applied for incubating u and I'll talk about that in a little bit. We believe it's the only cloudnative uh Kubernetes global load b load balancer. So it provides an independent u gslb capacity to any ingress or service. there's no dedicated management cluster so that there's no single point of failure. Basically what's happening is the operator is doing what an operator does and it's checking uh the health of its it's checking the health of the applications through the service through the ingress using normal things like liveness readiness probes um and then it's updating DNS right and it's saying hey this particular cluster the application on this particular cluster is ready to serve so if it's not then the other cluster is going to notice it because one other thing that the operators are doing is talking to each other to make sure that um they know the state of the world.

So it's Kubernetes native application health checks and it commoditizes GLB for Kubernetes. So it's using all the same things that you know about already. You don't have to really learn anything new. You just have to plop in a a YAML file as we'll see in a minute. This is just a diagram that
