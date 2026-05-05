---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Experience"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Xiaoman Dong", "Alex Pucher", "Parasail"]
sched_url: https://kccncna2024.sched.com/event/1i7oe/tackling-gpu-shortages-and-high-costs-by-harnessing-hybrid-kubernetes-clusters-xiaoman-dong-alex-pucher-parasail
youtube_search_url: https://www.youtube.com/results?search_query=Tackling+GPU+Shortages+and+High+Costs+by+Harnessing+Hybrid+Kubernetes+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tackling GPU Shortages and High Costs by Harnessing Hybrid Kubernetes Clusters - Xiaoman Dong & Alex Pucher, Parasail

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Xiaoman Dong, Alex Pucher, Parasail
- Schedule: https://kccncna2024.sched.com/event/1i7oe/tackling-gpu-shortages-and-high-costs-by-harnessing-hybrid-kubernetes-clusters-xiaoman-dong-alex-pucher-parasail
- Busca YouTube: https://www.youtube.com/results?search_query=Tackling+GPU+Shortages+and+High+Costs+by+Harnessing+Hybrid+Kubernetes+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tackling GPU Shortages and High Costs by Harnessing Hybrid Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oe/tackling-gpu-shortages-and-high-costs-by-harnessing-hybrid-kubernetes-clusters-xiaoman-dong-alex-pucher-parasail
- YouTube search: https://www.youtube.com/results?search_query=Tackling+GPU+Shortages+and+High+Costs+by+Harnessing+Hybrid+Kubernetes+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sxv7XqhPVhE
- YouTube title: Tackling GPU Shortages and High Costs by Harnessing Hybrid Kubernetes Clusters - X. Dong, A. Pucher
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tackling-gpu-shortages-and-high-costs-by-harnessing-hybrid-kubernetes/sxv7XqhPVhE.txt
- Transcript chars: 31171
- Keywords: actually, cluster, gpu, providers, essentially, workloads, already, running, question, control, lambda, figure, latency, trying, provider, talking, everything, networking

### Resumo baseado na transcript

before we actually start I I would really love to we would really love to know the audience a little bit a quick poll how many people have actually provision GPU raise your hand oh that's nice in the cloud like ews or something like that okay okay I this is but this is like 2/3 all right all right how many are in in the kubernetes class already oh that's a essentially the same all right that's great good okay but wait wait so who has provisioned CPUs not

### Excerpt da transcript

before we actually start I I would really love to we would really love to know the audience a little bit a quick poll how many people have actually provision GPU raise your hand oh that's nice in the cloud like ews or something like that okay okay I this is but this is like 2/3 all right all right how many are in in the kubernetes class already oh that's a essentially the same all right that's great good okay but wait wait so who has provisioned CPUs not from AWS gcp or uh maybe Azure okay okay nice nice okay great okay good see hope you are in the right place so uh I would introduce myself first so I'm saman I've being in the well uh data and infrastructure in for for quite a long time and many companies right now uh we are in a very early stage stter yeah uh my name is Alex or you know Alexander poer same thing here we kind of both founding engineers at parale um but essentially our like the whole focus of what we've tried to kind of get in our minds over the last like I guess like one and a half years or so right was really to go and say how do we build scalable but also cheap and easy to use AI infrastructure right and then the funny thing is you know if you as you can already tell from the poll right if you ever go and you say Hey you want gpus and want to do something for them chances are you want to be a kubernetes cluster because well all the nice things of like you know service measures and all the access control like all the things that come with kubernetes are really nice to have uh when you already work with uh you know just llms and other just the GPU heavy workloads right because the GPU heavy workloads alone already complicated enough so if there's something to take care of the operations piece then that's great right let's use it so about a year and a half ago right so we uh talk to our acquaintances and friends and we like hey we want to do AI infrastructure and gpus and uh essentially the resounding uh response that we got is to just use AWS you know it's it's great it's easy and you know build your product there and then everything is going to be fine and that sounds good you know you you just you create an account you know you sign up and you go hey this is great you know I'm a funded startup I even get startup credits so how about I spawn a few gpus so that I get to try out you know what say VM has to offer right now so you go you want to start the GPU instance and you look through it and you go hey uh can I have like an a100 or like m
