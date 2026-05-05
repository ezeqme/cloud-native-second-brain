---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Kubernetes", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/autoscaling-all-things-kubernetes-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=yaB8I6_qR_k
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+All+Things+Kubernetes+with+Prometheus+PromCon+2018
video_match_score: 1.013
status: video-found
---

# Autoscaling All Things Kubernetes with Prometheus

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Kubernetes]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/autoscaling-all-things-kubernetes-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=yaB8I6_qR_k

## Resumo

Speakers: Michael Hausenblas Frederic Branczyk Autoscaling in Kubernetes used to be an inconsistent concept, however using the new metrics APIs defined by Kubernetes SIG Instrumentation the monitoring system of choice can be used. As it turns out, Prometheus is a popular system being used alongside Kubernetes, and the community has already developed a custom-metrics-api adapter to be used for Prometheus. This means, we can now perform autoscaling on the cluster and application level with metrics collected by Prometheus.

## Abstract oficial

Speakers:


Michael Hausenblas
Frederic Branczyk


Autoscaling in Kubernetes used to be an inconsistent concept, however using the new metrics APIs defined by Kubernetes SIG Instrumentation the monitoring system of choice can be used. As it turns out, Prometheus is a popular system being used alongside Kubernetes, and the community has already developed a custom-metrics-api adapter to be used for Prometheus. This means, we can now perform autoscaling on the cluster and application level with metrics collected by Prometheus.

While for some use cases single values are enough, for others more sophisticated historic metrics are necessary. In the context of the SIG Autoscaling, we're working on a Vertical Pod Autoscaler (VPA), allowing for vertical autoscaling of pods (that is, adapting resource limits and requests) based on metrics from Prometheus (see https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/vertical-pod-autoscaler.md).

Frederic and Michael will review the history of metrics in Kubernetes, discuss the current state of metrics and autoscaling on Kubernetes using Prometheus with a focus on VPAs as well as show it in action.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/autoscaling-all-things-kubernetes-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=yaB8I6_qR_k
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yaB8I6_qR_k
- YouTube title: PromCon 2018: Autoscaling All Things Kubernetes with Prometheus
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/autoscaling-all-things-kubernetes-with-prometheus/yaB8I6_qR_k.txt
- Transcript chars: 22591
- Keywords: actually, scaling, prometheus, resources, metrics, request, memory, anything, obviously, whatever, scheduler, basically, auto-scaling, horizontal, little, applications, certain, probably

### Resumo baseado na transcript

hi I'm Michael I'm a promise addict I work in the cloud platform team at Red Hat and hi Michael so I'm I'm Frederick I lead the monitoring team at Red Hat previously Korres and I basically work on anything Karuna DS and Prometheus and anything in between which is also why I work on the prometheus operator for example because that connects the two worlds so but today concretely we want to talk about auto-scaling everything on kubernetes with Prometheus and before we really dive into how all of

### Excerpt da transcript

hi I'm Michael I'm a promise addict I work in the cloud platform team at Red Hat and hi Michael so I'm I'm Frederick I lead the monitoring team at Red Hat previously Korres and I basically work on anything Karuna DS and Prometheus and anything in between which is also why I work on the prometheus operator for example because that connects the two worlds so but today concretely we want to talk about auto-scaling everything on kubernetes with Prometheus and before we really dive into how all of that works let's make sure we all understand what we mean when we talk about auto-scaling so let's make sure we're all on the same page so on an abstract level auto-scaling is really about calculating the resources that we are going to need to cover the demand so really what why all of us are working on infrastructure is because our companies need to make money somehow right and we are the ones that provide resources to the rest of our companies to do this and to satisfy all of that and really how demand is measured is by metrics and obviously we do that with Prometheus which is why why we're here and in order to actually make use of all these things we need to collect them we need to make them queryable and we need to store them to query over time and what I started with is we ultimately do this in order to fulfill our service level objectives of our service level agreements so that basically means that we've promised our users some sort of availability or really whatever your service level objective is if you want to know more about these things I highly recommend reading the Google SR eBook there's loads of examples and even in the new workbook there are examples based on Prometheus and even prometheus direct queries and alerting rules and all of that but yeah basically the objective means I am promising my user 99.99% uptime or availability and that's the SLO of the SLA and the indicator could be the combination of multiple services availability or really anything that influences that objective so now we know on a on an abstract level what auto-scaling is and why we do it now in kubernetes how does that what does that look like in kubernetes we really have two high-level kinds of auto scaling and one of them is not really auto scaling which is why I'm going to start start with that which is cluster level auto scaling so sizing our cluster based on the man and why I'm saying that is because in kubernetes this is not really based on any metrics in kubernetes cluster
