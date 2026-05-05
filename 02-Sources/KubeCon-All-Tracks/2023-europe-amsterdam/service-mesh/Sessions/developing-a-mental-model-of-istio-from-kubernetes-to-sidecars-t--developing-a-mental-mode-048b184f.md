---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Service Mesh"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Aaron Birkland", "Nina Polshakova", "solo.io"]
sched_url: https://kccnceu2023.sched.com/event/1HyZj/developing-a-mental-model-of-istio-from-kubernetes-to-sidecars-to-ambient-aaron-birkland-nina-polshakova-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Developing+a+Mental+Model+of+Istio%3A+From+Kubernetes+to+Sidecars+to+Ambient+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Developing a Mental Model of Istio: From Kubernetes to Sidecars to Ambient - Aaron Birkland & Nina Polshakova, solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aaron Birkland, Nina Polshakova, solo.io
- Schedule: https://kccnceu2023.sched.com/event/1HyZj/developing-a-mental-model-of-istio-from-kubernetes-to-sidecars-to-ambient-aaron-birkland-nina-polshakova-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Developing+a+Mental+Model+of+Istio%3A+From+Kubernetes+to+Sidecars+to+Ambient+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Developing a Mental Model of Istio: From Kubernetes to Sidecars to Ambient.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZj/developing-a-mental-model-of-istio-from-kubernetes-to-sidecars-to-ambient-aaron-birkland-nina-polshakova-soloio
- YouTube search: https://www.youtube.com/results?search_query=Developing+a+Mental+Model+of+Istio%3A+From+Kubernetes+to+Sidecars+to+Ambient+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0xCsMfPVZ6M
- YouTube title: Developing a Mental Model of Istio: From Kubernetes to Sidecars...- Aaron Birkland & Nina Polshakova
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/developing-a-mental-model-of-istio-from-kubernetes-to-sidecars-to-ambi/0xCsMfPVZ6M.txt
- Transcript chars: 33901
- Keywords: waypoint, ambient, sidecar, policy, istio, traffic, ratings, request, virtual, tunnel, reviews, mesh, actually, destination, account, namespace, header, authorization

### Resumo baseado na transcript

yeah I'm uh Aaron and this is my colleague Nina and we are going to be given the talk on developing a mental model of istio and so at uh at solar organization um there are you know a number of people who are contributors to istio or leaders like we are on definitely in the user camp and so this kind of Chronicles uh our journey for understanding you know how how ambient this deal works and how to interact with it um so yeah let's get started so so let's uh go go to Prometheus copy that over and we're gonna see uh how many istio total requests that we're getting from going to reviews V1 versus the total so when I execute this it might take a couple minutes to get uh going to V1 and then uh 10 to V2 and then in ambient the same thing so V1 um uh about 90 and then the same thing for v2 about 10 percent so uh that's all I had to show demo wise um I encourage

### Excerpt da transcript

yeah I'm uh Aaron and this is my colleague Nina and we are going to be given the talk on developing a mental model of istio and so at uh at solar organization um there are you know a number of people who are contributors to istio or leaders like we are on definitely in the user camp and so this kind of Chronicles uh our journey for understanding you know how how ambient this deal works and how to interact with it um so yeah let's get started so um yeah so we will um so in this talk uh yeah we'll talk about our journey of how we learned um the differences in istio's API so ambient is not a drop-in replacement so there are differences in how uh the API is used inside car versus ambient mode and this was a difficult thing for us to wrap our heads around and so it kind of helped to dig a little bit deeper and understand what's happening under the hood in order to develop that mental model of exactly why why we're seeing what we're seeing and like how to effectively use ambient so that hopefully you should get that out of this talk um so I'm going to start here just thinking about some of the abstractions of kubernetes and we're going to focus on the service abstraction since it's the most relevant for service mesh and so these abstractions can be implemented in a number of ways under the hood uh and we'll use that to motivate our journey so we start off with a service in plain kubernetes and even here there are many different ways to implement it but this is one that I think we're all familiar with and so um what I'm doing here is I'm actually breaking the abstraction a little bit and so how many of you have programmed with the go programming language yes okay so when learning that um learning how interfaces work and learning how slices work uh the way my mind works I kind of had to think of them as like the structures that they were under the hood like an interface being like a pointer to data and then a pointer to like type information stuff I don't really care the details but but just knowing that kind of explained some of the weird behaviors that that that go can can uh that you can see and go so this is kind of similar like knowing what's under the hood can explain a lot so here we go with with plain old kubernetes and when you have a service uh you typically interact with it via a um a URL right which is written According to some convention and the idea is that your application will hit this URL and kubernetes will route it correctly so a service is an a
