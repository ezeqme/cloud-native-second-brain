---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Jan Willies", "Contributor"]
sched_url: https://kccnceu2026.sched.com/event/2EFy8/project-lightning-talk-kcp-scaling-the-kubernetes-control-plane-for-the-multi-cluster-era-jan-willies-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+kcp%3A+Scaling+The+Kubernetes+Control+Plane+For+The+Multi-Cluster+Era+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Cluster Era - Jan Willies, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jan Willies, Contributor
- Schedule: https://kccnceu2026.sched.com/event/2EFy8/project-lightning-talk-kcp-scaling-the-kubernetes-control-plane-for-the-multi-cluster-era-jan-willies-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+kcp%3A+Scaling+The+Kubernetes+Control+Plane+For+The+Multi-Cluster+Era+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Cluster Era.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFy8/project-lightning-talk-kcp-scaling-the-kubernetes-control-plane-for-the-multi-cluster-era-jan-willies-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+kcp%3A+Scaling+The+Kubernetes+Control+Plane+For+The+Multi-Cluster+Era+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-GJgzn3pyvM
- YouTube title: Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Clust... Jan Willies
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-kcp-scaling-the-kubernetes-control-plane-for-th/-GJgzn3pyvM.txt
- Transcript chars: 3835
- Keywords: basically, namespace, cluster, control, around, isolated, workspace, called, clears, throat, account, infrastructure, backing, experience, managed, lightweight, without, exactly

### Resumo baseado na transcript

I work for a company called Accenture and today I'll be presenting about the KCP project. So, basically the problem [clears throat] statement in Kubernetes is a bit and I'm sure many of you have been there already. KCP is an open source horizontally scalable control plane for Kubernetes like APIs and that provides isolated Kubernetes endpoints. And an endpoint in in KCP is called a workspace and what you get with a workspace is basically a full-blown Kubernetes API without all the workload and infrastructure stuff. And since it's a Kubernetes like API you can use all the familiar tools to access it like kubectl, helm, basically everything which is based on client go. So, you can just run it on on your laptop or on on a managed service or of course on Kubernetes as well to play around with it but it is also can be deployed as a global control plane with multi-region support with many caching layers and aggregate APIs um based on the on the deployment infrastructure.

### Excerpt da transcript

Hi, my name is Jan Viegas. I work for a company called Accenture and today I'll be presenting about the KCP project. So, basically the problem [clears throat] statement in Kubernetes is a bit and I'm sure many of you have been there already. When I want something in Kubernetes a space for me, myself, the team, I either have something called a namespace and have projects around the namespace who promise me to do like namespace on steroids to have a isolated account at Kubernetes or I get the full Kubernetes cluster experience via an isolated own tenant. And while a namespace is very quick to provision, a full Kubernetes cluster with if additionally have some opinion about it is from like even from a managed cloud provider half an hour to an hour so it's very heavy as an account and it shouldn't be heavy. So, being coming back to the roots here, what if we have both of that? So, we have a lightweight Kubernetes API and still have the full isolated experience. >> [clears throat] >> So, basically true isolation without the infrastructure backing it.

And a vanilla Kubernetes cluster has around 80 built-in resources last time I checked and for a use case where you are working with extending Kubernetes and like doubling down on CRDs, that is a lot and a lot of stuff you don't need for that. So, basically have a bit of a lightweight API server which which can be provisioned in seconds. So, that exactly is the KCP project. KCP is an open source horizontally scalable control plane for Kubernetes like APIs and that provides isolated Kubernetes endpoints. And an endpoint in in KCP is called a workspace and what you get with a workspace is basically a full-blown Kubernetes API without all the workload and infrastructure stuff. So, there are no nodes, no pods, no deployments, nothing like that. And inside a workspace you are cluster admin. So, you are basically in your in your own account and you can do whatever you want. And KCP serves as the as the housing around it. So, when you create a workspace it's up there in in literally a second and it allows you to do to um well, yeah, to control everything, not just the non-namespace stuff on the just the namespace stuff.

And since it's a Kubernetes like API you can use all the familiar tools to access it like kubectl, helm, basically everything which is based on client go. Oops. So, it's a single binary. It's it's in go written and it's compiled to a single binary. So, you can just run it on on your laptop or on on a mana
