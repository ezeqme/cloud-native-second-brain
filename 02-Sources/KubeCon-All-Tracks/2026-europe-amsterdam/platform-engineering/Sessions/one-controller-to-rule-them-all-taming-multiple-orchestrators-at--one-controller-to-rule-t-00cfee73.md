---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Srikar Paruchuru", "Egor Grishechko", "Uber"]
sched_url: https://kccnceu2026.sched.com/event/2CW3V/one-controller-to-rule-them-all-taming-multiple-orchestrators-at-uber-scale-srikar-paruchuru-egor-grishechko-uber
youtube_search_url: https://www.youtube.com/results?search_query=One+Controller+to+Rule+Them+All+-+Taming+Multiple+Orchestrators+at+Uber+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# One Controller to Rule Them All - Taming Multiple Orchestrators at Uber Scale - Srikar Paruchuru & Egor Grishechko, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Srikar Paruchuru, Egor Grishechko, Uber
- Schedule: https://kccnceu2026.sched.com/event/2CW3V/one-controller-to-rule-them-all-taming-multiple-orchestrators-at-uber-scale-srikar-paruchuru-egor-grishechko-uber
- Busca YouTube: https://www.youtube.com/results?search_query=One+Controller+to+Rule+Them+All+-+Taming+Multiple+Orchestrators+at+Uber+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre One Controller to Rule Them All - Taming Multiple Orchestrators at Uber Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3V/one-controller-to-rule-them-all-taming-multiple-orchestrators-at-uber-scale-srikar-paruchuru-egor-grishechko-uber
- YouTube search: https://www.youtube.com/results?search_query=One+Controller+to+Rule+Them+All+-+Taming+Multiple+Orchestrators+at+Uber+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lVt510hb8kY
- YouTube title: One Controller to Rule Them All - Taming Multiple Orchestrator... Srikar Paruchuru & Egor Grishechko
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/one-controller-to-rule-them-all-taming-multiple-orchestrators-at-uber/lVt510hb8kY.txt
- Transcript chars: 25528
- Keywords: deployment, controller, status, pretty, literally, essentially, simple, production, speaking, solution, second, object, failover, scaling, integration, multiple, compute, running

### Resumo baseado na transcript

Stateless compute to be specific because well stateful is a different beast entirely altogether. Um today we're going to talk about uh how we tamed multiple scale orchestrators. At the top we have up the federation layer and then Kubernetes which is essentially what as comput team we manage and then Linux at the end of the day up interacts with Kubernetes via CD which I'll get into a little bit later. We call deployment, a play on deployment and then Kubernetes interacts with Linux via pod and multiple container runtime components and the way back up is essentially you understand uh how much resources on the node are left. You aggregate that at the Kubernetes level which is then sent up to up which uh understands how much square capacity is present in a cluster and that lets it federate uh makes smarter decisions in zone placement. So this is where I suppose the Kubernetes part uh we zoom into the Kubernetes part which is essentially what our team does.

### Excerpt da transcript

Evening folks. Uh I'm Sri and this is my colleague Eager. Uh we are from uh Uber's compute team here in Amsterdam. Stateless compute to be specific because well stateful is a different beast entirely altogether. Um today we're going to talk about uh how we tamed multiple scale orchestrators. Uh we have millions of workloads running and what if multiple orchestrators get to claim authority over the scale of an individual workload. How do you reconcile that? How we reconcile that? how we settled on a solution, the things we broke, fixed, learned, all the while saving tens of millions of dollars for Uber. So, we're going to take you on that journey with us. It's been Yeah. more than a year on this journey. >> All right. Before I do that, let me uh walk you through uh a brief overview of how the stateless compute platform is set up. Up at the top, we have the platform called UP, which is essentially the face of compute. That's what service owners at stateless service owners at Uber interact with every day to scale deploy their services to scale up scale down their services and what have you.

Underneath up we have we have a lot lots of Kubernetes clusters from different zones spanning multiple regions. We ingest hardware from cloud GCP Oracle onrem and we manage this I mean that's where our team exists. We manage these Kubernetes clusters at scale for Uber. As I mentioned, up is essentially like sort of the face of the compute. Uh but that's an oversimplification really. Uh so if you look at I mean a picture is worth thousand words. So if you look at this is the UI of up. This is what our platform service owners see every day. You can see how featurerich it is. You can deploy a custom build of your choice. You can uh you can mention the kind of uh failure domain resiliency. I mean zone is a failure domain for us. So you can say oh I want my service to be alive in like three zones at least or two regions. You can specify that on up. and up serves as a federation layer. It's going to decide which zones to place the workload of the service in. Uh and if you can see from the UI, you see that there are two running instances of the service in something known as DC22 which is the zone and then DC22 stateless 01 which is the cluster.

So that's the kind of well that's the kind of experience like service owners at Uber have. That's a reimagining of uh what I've said so far. So you got these three interfaces. At the top we have up the federation layer and then Kubernete
