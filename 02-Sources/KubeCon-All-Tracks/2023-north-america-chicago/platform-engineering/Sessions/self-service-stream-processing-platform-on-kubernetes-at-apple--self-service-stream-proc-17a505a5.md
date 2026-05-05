---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Chenya Zhang", "Apple Inc."]
sched_url: https://kccncna2023.sched.com/event/1R2oZ/self-service-stream-processing-platform-on-kubernetes-at-apple-chenya-zhang-apple-inc
youtube_search_url: https://www.youtube.com/results?search_query=Self-service+Stream+Processing+Platform+on+Kubernetes+at+Apple+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Self-service Stream Processing Platform on Kubernetes at Apple - Chenya Zhang, Apple Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Chenya Zhang, Apple Inc.
- Schedule: https://kccncna2023.sched.com/event/1R2oZ/self-service-stream-processing-platform-on-kubernetes-at-apple-chenya-zhang-apple-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Self-service+Stream+Processing+Platform+on+Kubernetes+at+Apple+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Self-service Stream Processing Platform on Kubernetes at Apple.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oZ/self-service-stream-processing-platform-on-kubernetes-at-apple-chenya-zhang-apple-inc
- YouTube search: https://www.youtube.com/results?search_query=Self-service+Stream+Processing+Platform+on+Kubernetes+at+Apple+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-qYL9VylEZw
- YouTube title: Self-service Stream Processing Platform on Kubernetes at Apple - Chenya Zhang, Apple Inc.
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/self-service-stream-processing-platform-on-kubernetes-at-apple/-qYL9VylEZw.txt
- Transcript chars: 24709
- Keywords: cluster, resource, operator, processing, control, application, applications, support, gateway, running, multiple, automatically, upgrade, request, moving, deployment, actually, cost

### Resumo baseado na transcript

hey everyone good afternoon uh welcome to join our session today so we are going to share about uh the self-service stream processing platform on kubernetes uh M chya from Apple's AIML data platform this is our agenda today so we will talk about our journey moving to the cloud and kubernetes and why we adopt a Pache Flink for real-time data processing then our challenges while moving to production at large scale and the solutions that we have figured out so far so first about our journey moving to

### Excerpt da transcript

hey everyone good afternoon uh welcome to join our session today so we are going to share about uh the self-service stream processing platform on kubernetes uh M chya from Apple's AIML data platform this is our agenda today so we will talk about our journey moving to the cloud and kubernetes and why we adopt a Pache Flink for real-time data processing then our challenges while moving to production at large scale and the solutions that we have figured out so far so first about our journey moving to the cloud and kubernetes so our users expect very quickly scale up and down of the cluster resource to match their real-time traffic pattern and we cannot wait for long right and we also don't want to preempt user applications to honor some of them so we can see this is like a for the deployment itself we have the autoscaling and how about the cluster and from a platform's perspective sometimes it can be ideal that we decouple ourself a little bit away from the infrastructure maintainance overhead and when we move from virtualized deployment to Containers it actually help us abstract away the physical Hardware complexities so here we can see the containers can move free around clouds and also the OS distributions and in the multicloud environment there are a lot of benefits for us to Leverage The Available support from different Cloud providers the hardware resource and the cost efficiency and kubernetes can help us to organize this containers workloads in a consistent approach to provide the compatibility so there can always be limited admins who can help us address cluster issues at a very large scale luckily we can leverage kubernetes automatic recovery capability to solve some issues and to keep the cluster resilient and self-healing in case of failures and we know many platforms have this need to add additional components on top of an orchestration layer and here we can kubernetes has this modularized architecture that can allow us to integrate with multiple components and extensions okay so that's about our journey moving to the cloud and kubernetes and why we adopt a Pache Flink for real-time data processing so we know users have a very high expectation in terms of latency when they try to process data in real time right they expect the data can be immediately processed upon arriving the the system and we can see Flink supports a pipeline in memory execution model so data can be accessed from local and when there is a slow operation Flink is able to adjust
