---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking"]
speakers: ["Arun Sriraman", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV0b/k8snetlook-root-causing-k8s-network-problems-in-an-automated-way-arun-sriraman-vmware
youtube_search_url: https://www.youtube.com/results?search_query=K8snetlook+%E2%80%93+Root-Causing+K8s+Network+Problems+in+an+Automated+Way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# K8snetlook – Root-Causing K8s Network Problems in an Automated Way - Arun Sriraman, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: United States / Los Angeles
- Speakers: Arun Sriraman, VMware
- Schedule: https://kccncna2021.sched.com/event/lV0b/k8snetlook-root-causing-k8s-network-problems-in-an-automated-way-arun-sriraman-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=K8snetlook+%E2%80%93+Root-Causing+K8s+Network+Problems+in+an+Automated+Way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre K8snetlook – Root-Causing K8s Network Problems in an Automated Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0b/k8snetlook-root-causing-k8s-network-problems-in-an-automated-way-arun-sriraman-vmware
- YouTube search: https://www.youtube.com/results?search_query=K8snetlook+%E2%80%93+Root-Causing+K8s+Network+Problems+in+an+Automated+Way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_BDoxy9h95U
- YouTube title: k8snetlook – Root-Causing k8s Network Problems in an Automated Way - Arun Sriraman, VMware
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/k8snetlook-root-causing-k8s-network-problems-in-an-automated-way/_BDoxy9h95U.txt
- Transcript chars: 27109
- Keywords: within, network, running, cluster, networking, working, problems, debugging, either, source, issues, destination, trying, external, causing, everything, balancer, automated

### Resumo baseado na transcript

hello everyone good afternoon welcome to this talk on root causing kubernetes networking problems in an automated way i wish this session was in person and interactive i still would like to have this as interactive as possible so keep your questions coming in on chat and i'll answer them as we go i will also locate some time at the end as much as possible for q a i've debugged network problems in over 100 customer cost clusters in production so whatever you hear today as well as what that information is present in uh in the github repo with that i hope you've had a good session and learned something about kubernetes networking looked at various problems that can happen within kubernetes when you're deploying pods or apps as well as hopefully kds network will help you to get to that first level debugging and at least finding out where the problem could could lie and then getting to the right people for fixing it um as always looking for contributors there's a lot of things that needs

### Excerpt da transcript

hello everyone good afternoon welcome to this talk on root causing kubernetes networking problems in an automated way i wish this session was in person and interactive i still would like to have this as interactive as possible so keep your questions coming in on chat and i'll answer them as we go i will also locate some time at the end as much as possible for q a i've debugged network problems in over 100 customer cost clusters in production so whatever you hear today as well as what you'll see from a tool kds network perspective it is from my that experience all right so what is this talk all about right have you been in a situation where everything looks okay all of the points are running but then your app just won't communicate or it works most of the times but does not work sometime now if you look at the the cartoons there that could turn from an exciting happy person running kubernetes and happen within kubernetes to a very frustrated person especially when it comes to a network networking problem at the end of the talk i'm hoping that you feel less intimidated about networking issues as well as a lot more comfortable within kubernetes networking and i leave you equipped with a couple of tools and ways in which you can get to root causing a kubernetes networking problem in an automated way as well as if not getting to the problem getting to the place where you can find right help it's always beneficial to know some basics of kubernetes networking um rest assured most of the hard stuff is going to be done by k this network in that sense i will be talking about kubernetes networking uh in brief uh it is a big topic in itself and a whole talk so think of it as a crash course uh we'll then look at the problems that you normally see with kubernetes networking and running pods within kubernetes and how to classify these issues and then we'll look at what people do to resolve these issues it's very interesting what people do and that slide is exciting after that the important part we'll look at some open source tools and how we can use them to [Music] debug any networking issue and how to go about that debugging process and then we'll look at kts network in detail uh give you an inflection on it and a quick demo on how to work with it all right without further ado let's get started so kubernetes networking to keep it simple right there are three golden rules um and when it comes to communication within kubernetes and they are that all containers within the
