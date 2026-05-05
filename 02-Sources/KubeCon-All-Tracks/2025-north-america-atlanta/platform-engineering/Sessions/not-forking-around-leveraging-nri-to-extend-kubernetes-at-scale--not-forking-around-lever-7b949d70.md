---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Johan Jensen", "Wesley Bermbach", "Uber"]
sched_url: https://kccncna2025.sched.com/event/27Fay/not-forking-around-leveraging-nri-to-extend-kubernetes-at-scale-johan-jensen-wesley-bermbach-uber
youtube_search_url: https://www.youtube.com/results?search_query=Not+Forking+Around%3A+Leveraging+NRI+To+Extend+Kubernetes+at+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Not Forking Around: Leveraging NRI To Extend Kubernetes at Scale - Johan Jensen & Wesley Bermbach, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Johan Jensen, Wesley Bermbach, Uber
- Schedule: https://kccncna2025.sched.com/event/27Fay/not-forking-around-leveraging-nri-to-extend-kubernetes-at-scale-johan-jensen-wesley-bermbach-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Not+Forking+Around%3A+Leveraging+NRI+To+Extend+Kubernetes+at+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Not Forking Around: Leveraging NRI To Extend Kubernetes at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fay/not-forking-around-leveraging-nri-to-extend-kubernetes-at-scale-johan-jensen-wesley-bermbach-uber
- YouTube search: https://www.youtube.com/results?search_query=Not+Forking+Around%3A+Leveraging+NRI+To+Extend+Kubernetes+at+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=V0afXi4mOiU
- YouTube title: Not Forking Around: Leveraging NRI To Extend Kubernetes at Scale - Johan Jensen & Wesley Bermbach
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/not-forking-around-leveraging-nri-to-extend-kubernetes-at-scale/V0afXi4mOiU.txt
- Transcript chars: 24454
- Keywords: container, features, platform, resources, plugin, containers, changes, actually, create, resource, containerd, essentially, upstream, cublet, trying, llm, workloads, specific

### Resumo baseado na transcript

I'm also working together with Yan at Uber on our stateful container platform. And uh we're going to talk a bit about noting around or leveraging NI to extend Kubernetes at scale. The last two they have already been moved towards Kubernetes and are running on a Kubernetes platform but our staple platform has been like a proprietary built container platform and we're now trying trying to see can we actually move that towards Kubernetes. And by trying to unify all of these different platforms on Kubernetes, we get this kind of common layer where we can reduce fragmentation and enable a lot of like common tooling and basically get obsibility and policy and service mesh all of these different things get them unified to run on top of Kubernetes. The challenge is that on our proprietary container platform, we've been a able to build a lot of different sort of uh integrations that we needed and to run to basically build our stack. If you end up regressing a lot of these features this going to be quite costly to the business itself.

### Excerpt da transcript

I'm Johan. I am a software engineer working at Uber. And with me I got Wesley. >> Hi everyone. Yeah, my name is Wesley. I'm also working together with Yan at Uber on our stateful container platform. >> Yes. And uh we're going to talk a bit about noting around or leveraging NI to extend Kubernetes at scale. Essentially we're going to talk a bit about our container platform and how we are trying to do certain things on Kubernetes um that we haven't been possible to do before. So, does it work? Um, Uber does 1.5 million trips per hour. We do this across like uh 70 countries and that's both for like rides and delivery. We underneath all of these rides are of course a lot of containers. So we have 8 million containers that are running on more than 200,000 hosts and we do this on multiple uh platforms. The Uber Stafle platform is a platform uh that both Wes and I are working on. We're running 400,000 stafle workloads uh across 3 million containers and on 100,000 hosts. But at we have multiple different container platforms.

The ster one of course runs databases, storage systems, anything that relies on local disk or persistent volumes in general. We also have a stateless container platform that runs services, APIs, microservices uh and anything else uh that doesn't require state. Then we also have a batch processing uh platform which does all kind of like data processing and analytics as well. The last two they have already been moved towards Kubernetes and are running on a Kubernetes platform but our staple platform has been like a proprietary built container platform and we're now trying trying to see can we actually move that towards Kubernetes. is the last major hold out. And by trying to unify all of these different platforms on Kubernetes, we get this kind of common layer where we can reduce fragmentation and enable a lot of like common tooling and basically get obsibility and policy and service mesh all of these different things get them unified to run on top of Kubernetes. The challenge is that on our proprietary container platform, we've been a able to build a lot of different sort of uh integrations that we needed and to run to basically build our stack.

And these features they are now dependent on by a lot of these stateful workloads. Kubernetes might not have all of these features available. So essentially the business doesn't care about putts. All these features that you built they set some kind of like expectation the stakeholders they rely on the
