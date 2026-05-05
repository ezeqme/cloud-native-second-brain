---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Kubernetes Core", "SRE Reliability"]
speakers: ["Liam Mackie", "Octopus Deploy"]
sched_url: https://kccncna2025.sched.com/event/27FcT/diagnosing-application-performance-with-ebpf-pyroscope-and-kubernetes-liam-mackie-octopus-deploy
youtube_search_url: https://www.youtube.com/results?search_query=Diagnosing+Application+Performance+With+EBPF%2C+Pyroscope%2C+and+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Diagnosing Application Performance With EBPF, Pyroscope, and Kubernetes - Liam Mackie, Octopus Deploy

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Liam Mackie, Octopus Deploy
- Schedule: https://kccncna2025.sched.com/event/27FcT/diagnosing-application-performance-with-ebpf-pyroscope-and-kubernetes-liam-mackie-octopus-deploy
- Busca YouTube: https://www.youtube.com/results?search_query=Diagnosing+Application+Performance+With+EBPF%2C+Pyroscope%2C+and+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Diagnosing Application Performance With EBPF, Pyroscope, and Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcT/diagnosing-application-performance-with-ebpf-pyroscope-and-kubernetes-liam-mackie-octopus-deploy
- YouTube search: https://www.youtube.com/results?search_query=Diagnosing+Application+Performance+With+EBPF%2C+Pyroscope%2C+and+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RrlF7OzCojE
- YouTube title: Diagnosing Application Performance With EBPF, Pyroscope, and Kubernetes - Liam Mackie
- Match score: 1.0
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/diagnosing-application-performance-with-ebpf-pyroscope-and-kubernetes/RrlF7OzCojE.txt
- Transcript chars: 26877
- Keywords: cluster, actually, memory, performance, software, clusters, trying, running, pyroscope, application, customers, little, ebpf, wanted, locally, testing, traces, everything

### Resumo baseado na transcript

Uh originally I was a systems engineer pulling things in and out of racks, dealing with networks, all of that fun stuff. Uh then I decided that SLAs and SLOs's were my ideal and I became an S. Now, we almost fell into a very similar trap, but just by setting performance targets. We don't want to be the guys at the back that just throw CPU and memory metrics at a wall. So, uh, the latency, which is essentially how long it takes for something to change in Kubernetes, be detected, and then sent back to the Octopus server. Um the other thing we wanted to be careful about is um the the kind of scale targets that we're setting at.

### Excerpt da transcript

All righty. My name is Liam. Um, I'm giving this talk. Hello. Uh, um, I'm from Australia, Brisbane, uh, to be exact. So, uh, pardon any flubs. I promise it's jet lag. So, uh, like I said before, I'm Liam. Uh, I'm a lead cloud engineer, modern deployments. Um, I've been at Octopus for about 4 years. Um, but I've worked with Kubernetes for about 9 since about 1.5. Uh originally I was a systems engineer pulling things in and out of racks, dealing with networks, all of that fun stuff. Uh then I decided that SLAs and SLOs's were my ideal and I became an S. Um then I became a cloud engineer because that's what people wanted me to do. Um uh at the moment, uh I'm really writing software in Go and C and I'm trying to mix in a lot of my reliability experience with that to try and get the best possible software outcomes as we possibly can at Octopus Deploy. So what we built um in Octopus deploy the mob deployments team is kind of like the Kubernetes team and inside that mo deployments uh Kubernetes team I'm the Kubernetes guy and so this talk is really about my personal experience trying to build a piece of software that we call the Kubernetes monitor.

It's a component of Octopus deploy. um it runs in customer clusters and when people deploy with Octopus deploy to those customer um to those clusters essentially what happens is the monitor goes through has a look at what's there and sends back resources and the current status of things. Um it sends that over gRPC. It's really cool. It was very fun to build. Um and customers just install it by helm. The catch is yeah we ship that software using Helm. Um for me as an S sur that makes things like right sizing performance engineering debugging and no SLOs's or SLAs's it's terrible can't do any of it. So before we get too far in, a quick show of hands here. How many of you guys at some point have just picked a random resource limit? Anything like that? Oh yeah, come on. Don't lie. We're not going to judge you here. Yeah. No. Now, we almost fell into a very similar trap, but just by setting performance targets. Again, we can't see anything in these clusters. So, we need to have like a a baseline, a default to give to people.

Um, but we didn't have that at the time. Um, we kind of threw some numbers at the wall. We kind of tried to talk to people and figure out what that number should be, but they just didn't have any context. We were just like, I think at the end, we just went, you know what, we want it to be fast and res
