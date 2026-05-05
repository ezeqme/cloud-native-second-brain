---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Multi-tenancy"
themes: ["Networking", "GitOps Delivery"]
speakers: ["Lin Sun", "Solo.io", "Faseela K", "Ericsson Software Technology"]
sched_url: https://kccnceu2023.sched.com/event/1Hyd1/operate-multi-tenancy-service-mesh-with-argocd-in-production-lin-sun-soloio-faseela-k-ericsson-software-technology
youtube_search_url: https://www.youtube.com/results?search_query=Operate+Multi-Tenancy+Service+Mesh+with+ArgoCD+in+Production+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Operate Multi-Tenancy Service Mesh with ArgoCD in Production - Lin Sun, Solo.io & Faseela K, Ericsson Software Technology

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Networking]], [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Lin Sun, Solo.io, Faseela K, Ericsson Software Technology
- Schedule: https://kccnceu2023.sched.com/event/1Hyd1/operate-multi-tenancy-service-mesh-with-argocd-in-production-lin-sun-soloio-faseela-k-ericsson-software-technology
- Busca YouTube: https://www.youtube.com/results?search_query=Operate+Multi-Tenancy+Service+Mesh+with+ArgoCD+in+Production+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Operate Multi-Tenancy Service Mesh with ArgoCD in Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyd1/operate-multi-tenancy-service-mesh-with-argocd-in-production-lin-sun-soloio-faseela-k-ericsson-software-technology
- YouTube search: https://www.youtube.com/results?search_query=Operate+Multi-Tenancy+Service+Mesh+with+ArgoCD+in+Production+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w3d8gxGpaNQ
- YouTube title: Operate Multi-Tenancy Service Mesh with ArgoCD in Production - Lin Sun & Faseela K
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/operate-multi-tenancy-service-mesh-with-argocd-in-production/w3d8gxGpaNQ.txt
- Transcript chars: 26623
- Keywords: istio, control, cluster, mesh, multiple, single, application, namespace, tenant, policy, deploy, applications, multi-tenancy, default, spaces, running, gateway, already

### Resumo baseado na transcript

all right looks like we are finally live here thank you so much for joining us on this beautiful day in Amsterdam by the way they are still quite a few seats in the front uh feel free to come to the front make yourself feel comfortable uh I hate you see you guys standing so thank you so much oh today we're going to talk about operate multi-dependency service match with Argo CD in production my name is lensang I'm the director of Open Source at solo.io it's a what we wanted to show in the demo uh the demo material is all available in the public GitHub you can use that I have put the references in the yeah on the slides towards the end as well now Lynn will again talk about the other different deployment models which are possible and with multi-tenancy yeah thank you thank you facila that's a great demo you did awesome to see it actually works so just to summarize uh multi-tenancy service mesh with a single uh istio service mesh you

### Excerpt da transcript

all right looks like we are finally live here thank you so much for joining us on this beautiful day in Amsterdam by the way they are still quite a few seats in the front uh feel free to come to the front make yourself feel comfortable uh I hate you see you guys standing so thank you so much oh today we're going to talk about operate multi-dependency service match with Argo CD in production my name is lensang I'm the director of Open Source at solo.io it's a small company how many of you heard of our company all right wow many of you thank you um so I've been a very long time it's your maintaining one of the founding members in the SEO Community I actually wrote two books about istio my most recent book is istio ambient to explain how many of you actually tried istio before wow many of you awesome how many of you actually heard about istio ambient wow are you surprised all right awesome so if you want to learn a little bit more about Ambien we do have a book signing tonight uh with me and my co-author Christian poster um and since I don't have my family traveling with me I in Amsterdam I thought I'd share of a team dinner picture and walk last night so I hope you guys are enjoying food in Amsterdam and also the canal now I'm going to pass to my co-speaker Priscilla hello everyone I'm Priscilla I work as a cloud native developer at Ericsson software technology which is open source software development division of Ericsson I primarily work from the Ericsson Euro lab office in Germany and my role includes prioritizing the Telco Cloud requirements in the open source communities especially istion and voy I'm I'm a maintainer of some of this working groups in istio and avoid prior to istio I have also served in the technical steering committee of open daylight and some of the other networking projects another Linux Foundation so I'm currently a steering committee member of istio as well yes I'm basically from India and that's my family and I have a eight-year-old daughter who had an amazing time here last Sunday in the CNC of kids day thanks to cnco for that and now over to you Lynn to get started with our presentation awesome thank you so much Priscilla can you guys all heal her fine she needs to good in the back okay awesome thank you so today we're going to talk about uh give you guys an overview of service mesh sounds you guys all know pretty much well about istio and service match so we're going to jump fast through that section then we're going to talk abo
