---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Goutam Verma", "Google Summer of Code", "Dean Troyer", "Salad"]
sched_url: https://kccncna2023.sched.com/event/1R2pp/maximizing-gpu-utilization-in-kubernetes-with-virtual-kubelets-goutam-verma-google-summer-of-code-dean-troyer-salad
youtube_search_url: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+in+Kubernetes+with+Virtual+Kubelets+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Maximizing GPU Utilization in Kubernetes with Virtual Kubelets - Goutam Verma, Google Summer of Code & Dean Troyer, Salad

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Goutam Verma, Google Summer of Code, Dean Troyer, Salad
- Schedule: https://kccncna2023.sched.com/event/1R2pp/maximizing-gpu-utilization-in-kubernetes-with-virtual-kubelets-goutam-verma-google-summer-of-code-dean-troyer-salad
- Busca YouTube: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+in+Kubernetes+with+Virtual+Kubelets+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Maximizing GPU Utilization in Kubernetes with Virtual Kubelets.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pp/maximizing-gpu-utilization-in-kubernetes-with-virtual-kubelets-goutam-verma-google-summer-of-code-dean-troyer-salad
- YouTube search: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+in+Kubernetes+with+Virtual+Kubelets+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QqJLsdFnm4A
- YouTube title: Maximizing GPU Utilization in Kubernetes with Virtual Kubelets - Goutam Verma & Dean Troyer
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/maximizing-gpu-utilization-in-kubernetes-with-virtual-kubelets/QqJLsdFnm4A.txt
- Transcript chars: 25284
- Keywords: virtual, gpu, question, multiple, running, cluster, physical, itself, little, process, provider, actually, existing, probably, control, network, pretty, whatever

### Resumo baseado na transcript

all right good morning everyone um this is a huge room feel free to move forward so it doesn't feel quite so big um hope you all had a good first or maybe second day of cubec con this year we're going to talk today a little bit about gpus with kubernetes and virtual cubts and uh well let's get going my name is Dean Troyer I'm with solad technology uh um we a relatively new GPU cloud provider um distributed clouds on all sorts of locations distributed gpus I

### Excerpt da transcript

all right good morning everyone um this is a huge room feel free to move forward so it doesn't feel quite so big um hope you all had a good first or maybe second day of cubec con this year we're going to talk today a little bit about gpus with kubernetes and virtual cubts and uh well let's get going my name is Dean Troyer I'm with solad technology uh um we a relatively new GPU cloud provider um distributed clouds on all sorts of locations distributed gpus I I should say um this talk was actually uh proposed and primarily written by gam Vena who is unable to be here today um so it is just me um we're going to talk a little bit I've got a I've got a a story about a mythical app that um needs some AI capabilities and we're going to kind of walk through how uh how you might add that capability to an existing platform um we'll look a little bit about what they've got the back end and what the what the exact needs are then we'll examine one one specific solution that um spoiler alert it's a virtual cuet and uh look at how that can uh can solve their problems and if the demo winds are uh favorable for us today we're actually going to walk through bringing one up so our story is around um an app called Slackers at work this is a mythical app that uh has a feature called the slacker tracker um every everybody's worked with a guy probably named Joe dittle who takes 30 minutes to get his coffee in the morning he spends two hours at lunch he's got to make the rounds of all the Departments before Coffee Break um and this app is for people to keep track of where he's at at any given time we've all worked with somebody like him probably more so before 2020 than now but anyway that's that's the situation that we're in it's just your basic mobile app and and they've decided product has decided that they want to add QR code tracking to this app so all you got to do is point your phone at Joe to Mark exactly where he is at any given time uh like like too many product teams they leave the implementation of getting the QR code onto Joe as a as a detail that someone else will solve now more realistically it's a it's a cloud-based app so they don't really have any local hosting abilities you know they don't they don't operate any of their own servers it's all it's all cloud-based um which means they also don't have any data center resources any of that usual stuff and their existing cloud provider uh well let's just say they don't have an affordable GPU offering without minimum
