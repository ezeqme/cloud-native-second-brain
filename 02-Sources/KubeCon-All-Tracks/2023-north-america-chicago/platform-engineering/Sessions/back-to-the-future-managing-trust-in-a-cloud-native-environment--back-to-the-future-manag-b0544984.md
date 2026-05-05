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
themes: ["Platform Engineering"]
speakers: ["Eli Nesterov", "SPIRL"]
sched_url: https://kccncna2023.sched.com/event/1R2lx/back-to-the-future-managing-trust-in-a-cloud-native-environment-eli-nesterov-spirl
youtube_search_url: https://www.youtube.com/results?search_query=Back+to+the+Future%3A+Managing+Trust+in+a+Cloud-Native+Environment+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Back to the Future: Managing Trust in a Cloud-Native Environment - Eli Nesterov, SPIRL

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: Eli Nesterov, SPIRL
- Schedule: https://kccncna2023.sched.com/event/1R2lx/back-to-the-future-managing-trust-in-a-cloud-native-environment-eli-nesterov-spirl
- Busca YouTube: https://www.youtube.com/results?search_query=Back+to+the+Future%3A+Managing+Trust+in+a+Cloud-Native+Environment+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Back to the Future: Managing Trust in a Cloud-Native Environment.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2lx/back-to-the-future-managing-trust-in-a-cloud-native-environment-eli-nesterov-spirl
- YouTube search: https://www.youtube.com/results?search_query=Back+to+the+Future%3A+Managing+Trust+in+a+Cloud-Native+Environment+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hYQGaHoGhXc
- YouTube title: Back to the Future: Managing Trust in a Cloud-Native Environment - Eli Nesterov, SPIRL
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/back-to-the-future-managing-trust-in-a-cloud-native-environment/hYQGaHoGhXc.txt
- Transcript chars: 20504
- Keywords: certificates, basically, bundle, workload, identity, anchors, interesting, company, private, container, certificate, server, operation, called, probably, propagate, another, managing

### Resumo baseado na transcript

so welcome everyone to a talk where we are going to discuss very interesting topic on managing trust anchors in a cloud native environment and kind of going back a little bit Back to the Future right we'll look into how trust anchor has been managed historically and how we can do better in a cloud native environment but hi everyone my name is Eli minister of and uh such a pleasure to present here I think I still remember like our very first Cube con that I attended in

### Excerpt da transcript

so welcome everyone to a talk where we are going to discuss very interesting topic on managing trust anchors in a cloud native environment and kind of going back a little bit Back to the Future right we'll look into how trust anchor has been managed historically and how we can do better in a cloud native environment but hi everyone my name is Eli minister of and uh such a pleasure to present here I think I still remember like our very first Cube con that I attended in San Francisco like many many years ago and it's like very small so it's always good to get back on stage and talk about some Co stuff that's happening here um so I've been long time as a community I happen to run one of their world largest deployment of spire scaled Beyond million nodes and and uh in 2020 I don't know a few months through the pandemic we've been writing a book about this kind of infinite regress problems in security and how spe Inspire helps to solve them uh the book called solving the bottom Turtle so if you want to read it it's completely free uh you go to spy.

iBook and you can get a awesome PDF in there and I'm also a co-founder and C of a company called spiral where we building workload identity platform based on spe specification so getting back to 2020 I've been thinking about like the trust and I kind of get to this idea of U identity trust Paradox or we're just starting with very interesting observation of like we as a human beings usually tend to grow trust between each other over time uh and surprisingly or not surprisingly there's lots of different researches how it's happening but in many cases the trust like between human beings started on some kind of maybe close to zero maybe higher depends on reputation and other things but over time it usually tends to go up up north and east very different researchers related how it's the trust ER between human beings happening but I found it's interesting that in digital world it's a little bit an opposite right so uh if you think about hey here's my server and I standed up today and I connected it to internet but in a year you probably will trust this server less than today if you didn't touch it because you didn't do any software updates in there and if it's been connected to internet probably someone find a vulnerability already own it right so there is kind of idea of erosion of trust over time in uh digital world and the same same related to digital identities right we used to issue certificates for our Rob servers f
