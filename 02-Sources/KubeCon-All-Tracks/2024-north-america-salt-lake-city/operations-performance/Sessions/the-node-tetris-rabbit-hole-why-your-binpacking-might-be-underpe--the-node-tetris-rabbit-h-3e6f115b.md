---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Hannah Taub", "Adobe Inc."]
sched_url: https://kccncna2024.sched.com/event/1i7rY/the-node-tetris-rabbit-hole-why-your-binpacking-might-be-underperforming-hannah-taub-adobe-inc
youtube_search_url: https://www.youtube.com/results?search_query=The+Node+Tetris+Rabbit+Hole%3A+Why+Your+Binpacking+Might+Be+Underperforming+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Node Tetris Rabbit Hole: Why Your Binpacking Might Be Underperforming - Hannah Taub, Adobe Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Hannah Taub, Adobe Inc.
- Schedule: https://kccncna2024.sched.com/event/1i7rY/the-node-tetris-rabbit-hole-why-your-binpacking-might-be-underperforming-hannah-taub-adobe-inc
- Busca YouTube: https://www.youtube.com/results?search_query=The+Node+Tetris+Rabbit+Hole%3A+Why+Your+Binpacking+Might+Be+Underperforming+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Node Tetris Rabbit Hole: Why Your Binpacking Might Be Underperforming.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rY/the-node-tetris-rabbit-hole-why-your-binpacking-might-be-underperforming-hannah-taub-adobe-inc
- YouTube search: https://www.youtube.com/results?search_query=The+Node+Tetris+Rabbit+Hole%3A+Why+Your+Binpacking+Might+Be+Underperforming+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6l1hwJRQBM4
- YouTube title: The Node Tetris Rabbit Hole: Why Your Binpacking Might Be Underperforming - Hannah Taub, Adobe Inc.
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-node-tetris-rabbit-hole-why-your-binpacking-might-be-underperformi/6l1hwJRQBM4.txt
- Transcript chars: 26454
- Keywords: clients, started, clusters, platform, client, packing, better, cost, cluster, resources, shared, allowed, efficiency, resource, running, memory, workloads, requests

### Resumo baseado na transcript

[Music] all right thank you everybody for coming out at the very very end of the conference um thank you I appreciate it I'm Hannah tab I'm a senior engineer on the ethos cost efficiency team at Adobe and this is the node Tetris Rabbit Hole why your bin packing and ours is underperforming quick intro to ethos ethos is adobe's internal kubernetes platform as a service we cover onboarding deployment integration testing monitoring everything in between you know the drill you've been here all week we have different levels

### Excerpt da transcript

[Music] all right thank you everybody for coming out at the very very end of the conference um thank you I appreciate it I'm Hannah tab I'm a senior engineer on the ethos cost efficiency team at Adobe and this is the node Tetris Rabbit Hole why your bin packing and ours is underperforming quick intro to ethos ethos is adobe's internal kubernetes platform as a service we cover onboarding deployment integration testing monitoring everything in between you know the drill you've been here all week we have different levels of guard rails for our different client needs everywhere from just upload your container and we'll take care of the rest to almost unfettered access to the kubernetes ecosystem we are multi cloud and multi- region across Azure AWS Data Center and all over the world we offer both shared and dedicated clusters for our different team needs and all of this is across hundreds of clusters and thousands of nodes it's big our background the cost efficiency team on ethos was and it still somewhat is a tiny team with the focus on cost efficiency start off with pretty much just me and my manager in 2020 and we slowly started beginning to grow over the past few years and all of that was to deal with a huge problem space we had to cover unallocated space we had to cover cost monitoring we had to cover client Resource Management we had to cover everything else that falls under overhead spend reduction and one of the paths we went down was improving our resource management by improving our bin packing a few definitions just before I start for some of the specific terms I'm using a client in this context is an adobe internal namespace owner running pods in one of our managed kubernetes clusters unallocated space is empty space on a kubernetes node that's not reserved by any cluster resource whether that's uh client name space or whether that's a demon set or whether that's just the kernel a pod disruption budget is a kubernetes object that controls how many pods uh with a certain label are allowed to be taken down by manual action at any time this can be from cluster upgrades this can be from nodes getting moved around anything like that taints and tolerations are pod and node properties that make tainted nodes only schedule nodes only schedule pod pods with the corresponding Toleration and pod anti-affinity and topology spread are two separate Concepts but in this particular context they are covering a similar area that Co they cover they are pod specificat
