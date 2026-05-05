---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["Kubernetes Core"]
speakers: ["Jago Macleod", "Engineering Director", "Kubernetes", "GKE", "Google"]
sched_url: https://kccncna2025.sched.com/event/27dCm/sponsored-keynote-accelerating-innovation-the-evolution-of-kubernetes-and-the-road-ahead-jago-macleod-engineering-director-kubernetes-gke-google
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Accelerating+Innovation%3A+The+Evolution+of+Kubernetes+and+the+Road+Ahead+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: Accelerating Innovation: The Evolution of Kubernetes and the Road Ahead - Jago Macleod, Engineering Director, Kubernetes & GKE, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Jago Macleod, Engineering Director, Kubernetes, GKE, Google
- Schedule: https://kccncna2025.sched.com/event/27dCm/sponsored-keynote-accelerating-innovation-the-evolution-of-kubernetes-and-the-road-ahead-jago-macleod-engineering-director-kubernetes-gke-google
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Accelerating+Innovation%3A+The+Evolution+of+Kubernetes+and+the+Road+Ahead+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Accelerating Innovation: The Evolution of Kubernetes and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dCm/sponsored-keynote-accelerating-innovation-the-evolution-of-kubernetes-and-the-road-ahead-jago-macleod-engineering-director-kubernetes-gke-google
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Accelerating+Innovation%3A+The+Evolution+of+Kubernetes+and+the+Road+Ahead+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NjiUXyU8E08
- YouTube title: Sponsored Keynote: Accelerating Innovation: The Evolution of Kubernetes and the Road A... J. Macleod
- Match score: 1.025
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-accelerating-innovation-the-evolution-of-kubernetes/NjiUXyU8E08.txt
- Transcript chars: 4477
- Keywords: adoption, google, update, especially, reliability, hardware, orchestration, announce, better, accelerating, innovation, source, couple, little, framework, running, upgrade, across

### Resumo baseado na transcript

Uh, this week I lead open source Kubernetes at Google and it's never been more fun than it is right now. So last year I gave an update at the same conference and I talked about how Kubernetes was following a typical adoption curve until a couple of years ago and then there was this big plot twist of the AI age and we were caught Using this and some other things, we've been able to achieve an almost four nines of reliability in our upgrade success rate across all of control planes and nodes. And this is something we're building on and extending into the scheduler and autoscaler making them more aware of the underlying infrastructure and the specific nuances there. We've been working really hard with the slurm and ray communities to make those frameworks work better on Kubernetes so that you get a consistent operational experience across the frameworks that you have to use. some amazing updates especially in the node side for in place pod resizing makes ray work much better and on the slurm side we've been learning a lot from the HPC community about how to make scheduling work better and at higher performance than ever before.

### Excerpt da transcript

Hello and good morning. My name is JGO Mloud and I have the greatest job in the world. No, for real. Uh, this week I lead open source Kubernetes at Google and it's never been more fun than it is right now. So last year I gave an update at the same conference and I talked about how Kubernetes was following a typical adoption curve until a couple of years ago and then there was this big plot twist of the AI age and we were caught a couple years ago a little flatfooted uh and I shared that we were in the midst of a real transformation in this space and the adoption curve and the consumption curve outstrips the adoption curve. So we we identified these three core stories that we rallied around at Google and invested a ton in the open source community, especially in Kubernetes. Reliability, the relationship with hardware, and moving from container orchestration to framework orchestration. I'm going to give a quick update and then a little bit about what's ahead. On the reliability side, I am so happy to announce that Kubernetes roll back is finally actually here.

This has taken literally a decade of effort. This is so awesome. And we knew early on that we needed to do this and it was just really hard to pull off. So now roll back is really here. It's upstream. There are tests running. You can do this. Uh and it is uh enabled in GKE today. Using this and some other things, we've been able to achieve an almost four nines of reliability in our upgrade success rate across all of control planes and nodes. And 97% of our fleet is on the most recent three versions. We know that it's sometimes you have good reasons to fall behind and you have maybe questionable reasons for not running on GKE. So, I'm also really happy to announce the same primitives that we did for rollbacks enable skip version upgrades. Imagine just one upgrade once a year safely. I would be remiss if I did not call out specifically Han Kang who passed away earlier this year. Uh the relationships we make in this community are not superficial. When you join this community, you really do join a family.

And this one really hurts. Um but this is a lasting legacy and I had to call him out. Thank you, Han. On the hardware side, you heard that DRA is GA, DRA is GA, DRA is GA, and all of this. Um, but it really does make your AI workloads especially a lot more portable uh, and functional. Uh, and this same approach is extending to CPUs and networking and all kinds of new and interesting areas. The after pic
