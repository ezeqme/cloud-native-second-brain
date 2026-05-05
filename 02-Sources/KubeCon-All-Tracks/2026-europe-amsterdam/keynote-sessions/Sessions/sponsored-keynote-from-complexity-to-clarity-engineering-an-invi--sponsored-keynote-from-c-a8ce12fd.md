---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["Kubernetes Core"]
speakers: ["Jesse Butler", "Principal Product Manager and Technologist", "Amazon Elastic Kubernetes Service (EKS)"]
sched_url: https://kccnceu2026.sched.com/event/2HgFN/sponsored-keynote-from-complexity-to-clarity-engineering-an-invisible-kubernetes-jesse-butler-principal-product-manager-and-technologist-amazon-elastic-kubernetes-service-eks
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Complexity+to+Clarity%3A+Engineering+an+Invisible+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sponsored Keynote: From Complexity to Clarity: Engineering an Invisible Kubernetes - Jesse Butler, Principal Product Manager and Technologist, Amazon Elastic Kubernetes Service (EKS)

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jesse Butler, Principal Product Manager and Technologist, Amazon Elastic Kubernetes Service (EKS)
- Schedule: https://kccnceu2026.sched.com/event/2HgFN/sponsored-keynote-from-complexity-to-clarity-engineering-an-invisible-kubernetes-jesse-butler-principal-product-manager-and-technologist-amazon-elastic-kubernetes-service-eks
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Complexity+to+Clarity%3A+Engineering+an+Invisible+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: From Complexity to Clarity: Engineering an Invisible Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgFN/sponsored-keynote-from-complexity-to-clarity-engineering-an-invisible-kubernetes-jesse-butler-principal-product-manager-and-technologist-amazon-elastic-kubernetes-service-eks
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Complexity+to+Clarity%3A+Engineering+an+Invisible+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-DhYRFNipcI
- YouTube title: Sponsored Keynote: From Complexity to Clarity: Engineering an Invisible Kubernetes - Jesse Butler
- Match score: 1.005
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sponsored-keynote-from-complexity-to-clarity-engineering-an-invisible/-DhYRFNipcI.txt
- Transcript chars: 5009
- Keywords: platforms, together, resources, complexity, systems, managing, across, operational, platform, scaled, working, cluster, object, authorizer, invisible, everyone, little, primitives

### Resumo baseado na transcript

Uh so Kubernetes is the backbone of some of the world's most in-demanding distributed systems. Uh beyond workload orchestration, we're managing application life cycle, we're provisioning cloud infrastructure, and we're uh enforcing organizational governance across fleets of clusters. Kubernetes is not invisible, and maybe that's not the goal, but we can push the complexity down into the system so we can use Kubernetes more effectively to build these scaled platforms. We need compute, nodes, and entire clusters to scale in and out of our system freely. These projects all started by thinking about the cluster features that we wish we had for customers and a desire to leverage Kubernetes more effectively to mitigate that operational burden at scale. It's the node life cycle manager for Kubernetes, providing just-in-time infrastructure based on node uh workload demand.

### Excerpt da transcript

And uh welcome everyone. Uh thank you so much for having me. Um I'm going to talk a little bit about primitives. Uh so Kubernetes is the backbone of some of the world's most in-demanding distributed systems. Uh beyond workload orchestration, we're managing application life cycle, we're provisioning cloud infrastructure, and we're uh enforcing organizational governance across fleets of clusters. Its extensibility and customization have led to entire ecosystem of open solutions to solve nearly every operational challenge. In the enterprise, we've fully leaned in to Kubernetes being a platform for building platforms. In the EKS team at AWS, we've seen this firsthand. >> [snorts] >> Uh nearly all of our scaled customers operate a Kubernetes-based platform in order to abstract the cloud complexity and enable developers to deliver and maintain at safe velocity. Very few have reinvented the wheel here. Most of these platforms are built on open standards from the CNCF ecosystem, but everyone's solving the same problems operationally.

The effort comes in tying all these pieces together, keeping it running, scaled, and conformant. System primitives don't simplify or the layers below. They abstract them, making them easier to consume, leveraging their power more easily. Kubernetes is not invisible, and maybe that's not the goal, but we can push the complexity down into the system so we can use Kubernetes more effectively to build these scaled platforms. These enterprise systems have common set of needs. We need compute, nodes, and entire clusters to scale in and out of our system freely. We need databases and caches and all the other things in the cloud to be integrated well and deeply, and we need to keep everything on the rails with safe and compliant governance. >> [snorts] >> We've been working in these foundational areas across three community projects that we'd like to bring to your attention today. These projects all started by thinking about the cluster features that we wish we had for customers and a desire to leverage Kubernetes more effectively to mitigate that operational burden at scale.

[clears throat] Carpenter is a subproject of SIG autoscaling. It's the node life cycle manager for Kubernetes, providing just-in-time infrastructure based on node uh workload demand. Instead of pre-configuring node groups and scaling them up and down, Carpenter provisions the optimal instance in real time from the universe of what's available to it. We shift from human
