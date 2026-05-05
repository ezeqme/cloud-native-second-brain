---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Community"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Swetha Repakula", "Google", "Antonio Ojea Garcia", "RedHat"]
sched_url: https://kccncna2022.sched.com/event/182E6/sigs-arent-silos-a-case-study-into-solving-inter-domain-problems-in-kubernetes-development-swetha-repakula-google-antonio-ojea-garcia-redhat
youtube_search_url: https://www.youtube.com/results?search_query=SIGs+Aren%E2%80%99t+Silos%3A+A+Case+Study+Into+Solving+Inter-Domain+Problems+In+Kubernetes+Development+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SIGs Aren’t Silos: A Case Study Into Solving Inter-Domain Problems In Kubernetes Development - Swetha Repakula, Google & Antonio Ojea Garcia, RedHat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Community]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Swetha Repakula, Google, Antonio Ojea Garcia, RedHat
- Schedule: https://kccncna2022.sched.com/event/182E6/sigs-arent-silos-a-case-study-into-solving-inter-domain-problems-in-kubernetes-development-swetha-repakula-google-antonio-ojea-garcia-redhat
- Busca YouTube: https://www.youtube.com/results?search_query=SIGs+Aren%E2%80%99t+Silos%3A+A+Case+Study+Into+Solving+Inter-Domain+Problems+In+Kubernetes+Development+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SIGs Aren’t Silos: A Case Study Into Solving Inter-Domain Problems In Kubernetes Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182E6/sigs-arent-silos-a-case-study-into-solving-inter-domain-problems-in-kubernetes-development-swetha-repakula-google-antonio-ojea-garcia-redhat
- YouTube search: https://www.youtube.com/results?search_query=SIGs+Aren%E2%80%99t+Silos%3A+A+Case+Study+Into+Solving+Inter-Domain+Problems+In+Kubernetes+Development+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iQAl8pc21kU
- YouTube title: SIGs Aren’t Silos: A Case Study Into Solving Inter-Domain... Swetha Repakula & Antonio Ojea Garcia
- Match score: 0.765
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sigs-arent-silos-a-case-study-into-solving-inter-domain-problems-in-ku/iQAl8pc21kU.txt
- Transcript chars: 27434
- Keywords: network, working, endpoint, cubelet, another, controller, traffic, terminal, little, endpoints, happens, remove, actually, important, questions, happening, failed, deleted

### Resumo baseado na transcript

this is a developer talk as you can see we are I imagine that all of you are contributors or willing to contribute or people interested in kubernetes is anybody that is a developing kubernetes can raise the hand okay and people that are going to contribute to kubernetes ever here okay so you are going to find this issue because this is a talk about a Horror history that we we have to suffer and you may think that kubernetes is this fancy project is super cool but there

### Excerpt da transcript

this is a developer talk as you can see we are I imagine that all of you are contributors or willing to contribute or people interested in kubernetes is anybody that is a developing kubernetes can raise the hand okay and people that are going to contribute to kubernetes ever here okay so you are going to find this issue because this is a talk about a Horror history that we we have to suffer and you may think that kubernetes is this fancy project is super cool but there are a lot of horror histories and this is one of them so first of all we need to this is myself Anthony I'm working at Google Now I was working at Tech Hub before and I'm Suite also at Google uh previously worked at IBM on different open source projects okay so first of all just for the people that know is not used to kubernetes yes to understand a bit better how how the project work how the project is organized so uh basically the the project is is government on on the developer side is based on a special interest group so we can have this groups or six that are horizontal like API Machinery or excalibility or we have another internet or another group that are vertical like network node scheduler most of the people are used to these verticals in their companies and to the problems that this represent what is the problem uh this General problem in the network not this is a problem in your site and you have this wall going back and forth and this happens in kubernetes too we have people that is in signaled we have people at least six Network and we have bikes and we never know who is the who is the responsible but instead of fighting the ball we try to collaborate to solve the problem and this this talk is about one of these examples where about in a component that is responsible from when she was affecting another six and how do we solve it in collaborate so this is how the we talked about how the project is organized in terms of development but this is how the kubernetes components look like we have accumulate we have a API server we have a controller manager we have q proxy and the components are more or less related to one seek but doesn't mean that the seek is the owner so for example the qlip most of the code is responsibility or responsibility of signal but Sig network has a lot of bits there same happens in API Machinery with the or the best sample is the controller manager the controller manages a component that has a lot of code from different six and at the end we have all this shu
