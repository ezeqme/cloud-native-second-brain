---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Storage Data", "Kubernetes Core"]
speakers: ["Laurent Bernaille", "Maxime Visonneau", "Datadog"]
sched_url: https://kccnceu2025.sched.com/event/1txAT/cloudy-with-a-chance-of-kubernetes-going-from-one-to-three-cloud-providers-laurent-bernaille-maxime-visonneau-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Cloudy+With+a+Chance+of+Kubernetes%3A+Going+From+One+To+Three+Cloud+Providers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Cloudy With a Chance of Kubernetes: Going From One To Three Cloud Providers - Laurent Bernaille & Maxime Visonneau, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Laurent Bernaille, Maxime Visonneau, Datadog
- Schedule: https://kccnceu2025.sched.com/event/1txAT/cloudy-with-a-chance-of-kubernetes-going-from-one-to-three-cloud-providers-laurent-bernaille-maxime-visonneau-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Cloudy+With+a+Chance+of+Kubernetes%3A+Going+From+One+To+Three+Cloud+Providers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Cloudy With a Chance of Kubernetes: Going From One To Three Cloud Providers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAT/cloudy-with-a-chance-of-kubernetes-going-from-one-to-three-cloud-providers-laurent-bernaille-maxime-visonneau-datadog
- YouTube search: https://www.youtube.com/results?search_query=Cloudy+With+a+Chance+of+Kubernetes%3A+Going+From+One+To+Three+Cloud+Providers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iCAFXF5ECto
- YouTube title: Cloudy With a Chance of Kubernetes: Going From One To Three...  Laurent Bernaille & Maxime Visonneau
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cloudy-with-a-chance-of-kubernetes-going-from-one-to-three-cloud-provi/iCAFXF5ECto.txt
- Transcript chars: 33512
- Keywords: providers, application, clusters, looking, multiple, cluster, control, actually, course, deploy, manage, applications, running, region, started, regions, abstraction, provider

### Resumo baseado na transcript

Thank you very much for uh staying with us up until the very last session of the day. We are both working for data dog as part of the infrastructure engineering group. customers if it solves our problem potentially it solves theirs and of course uh more locations to operate from and also a good starting point to establish partnerships with those providers. And of course, as Maxim was saying, one of the reason we're sharing it here today is because we're using Kubernetes to make it work. consider different regions um in in the same way and of course I mean I'm sure you know the answer the answer felt uh very clear at the time it was it was Kubernetes right and the idea is that Kubernetes offers us a unified But something that was important to very similar to using multiple clouds is that our customers were running were starting to run Kubernetes in 2018 and we were not and so uh in order to make our integration and our support for communities better, it made a lot of sense for us to also run on Kubernetes.

### Excerpt da transcript

Hello. Hey everyone. Thank you very much for uh staying with us up until the very last session of the day. Highly appreciate it. Um so my name is Maxim Vizeno. I'm here today alongside Laurai. We are both working for data dog as part of the infrastructure engineering group. And if we're here with you today is to talk to you about uh our story on how we operate our infrastructure over not only one but three cloud providers now. and uh how Kubernetes helped us uh in that journey. Uh we'll be happy to take questions after the talk. I'm not sure we'll have enough time, but happy to take them offline. Otherwise, you can always find us on the Kubernetes Slack. And in case you do not know about data dog, we are a software as a service obser observability platform uh that help our and we aim to help our customers obtain better visibility into their infrastructure and applications. And to give you a bit of sense of scale of uh what we operate at, we have about 800 integration as of today and we handle more than 10 trillions events on a daily basis.

Uh if we're here today is to talk about Kubernetes. So on that front uh we have hundreds of clusters uh tens of thousands of nodes and hundreds of thousands of pods and uh they are all uh living in the cloud uh among three of uh three providers public cloud providers namely Azure AWS and GCP and if we did that uh spoiler alert uh it wasn't because it was fun uh surprisingly perhaps but we had some reasons to do so first uh our customers were looking for us to be uh close to them. Uh there is also this uh interesting philosophy that we have at data dog that we call dog fooding which is basically looking to experiment uh as much as we can in order to potentially provide solutions for that are um more pertinent for our customers if it solves our problem potentially it solves theirs and of course uh more locations to operate from and also a good starting point to establish partnerships with those providers. And uh so to get started I'll hand it over to Lauron who will dig into will get you into where we started and uh where we are today.

So let's start with a bit of history. Um until 2018 dead dog was running on a single region uh in the US on AWS uh what we could refer to as classic and everything was operated with virtual machines managed by chef and application were deployed with capistrano. In 2018, we decided to expand and we created our first region outside of the US on GCP in Europe. And over the years, we added mor
