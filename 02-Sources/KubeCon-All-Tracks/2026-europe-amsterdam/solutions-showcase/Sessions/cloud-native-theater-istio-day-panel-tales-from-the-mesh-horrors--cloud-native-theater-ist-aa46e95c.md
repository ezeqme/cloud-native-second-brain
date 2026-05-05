---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking"]
speakers: []
sched_url: https://kccnceu2026.sched.com/event/2EG0z/cloud-native-theater-istio-day-panel-tales-from-the-mesh-horrors-and-successes-of-running-istio-in-production
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Panel%3A+Tales+From+the+Mesh%3A+Horrors+and+Successes+of+Running+Istio+in+Production+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Istio Day: Panel: Tales From the Mesh: Horrors and Successes of Running Istio in Production

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: N/A
- Schedule: https://kccnceu2026.sched.com/event/2EG0z/cloud-native-theater-istio-day-panel-tales-from-the-mesh-horrors-and-successes-of-running-istio-in-production
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Panel%3A+Tales+From+the+Mesh%3A+Horrors+and+Successes+of+Running+Istio+in+Production+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Istio Day: Panel: Tales From the Mesh: Horrors and Successes of Running Istio in Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0z/cloud-native-theater-istio-day-panel-tales-from-the-mesh-horrors-and-successes-of-running-istio-in-production
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Panel%3A+Tales+From+the+Mesh%3A+Horrors+and+Successes+of+Running+Istio+in+Production+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-Z9zvo6leRY
- YouTube title: Cloud Native Theater | Istio Day: Panel: Horrors and Successes of Running Istio in Production
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-istio-day-panel-tales-from-the-mesh-horrors-and-s/-Z9zvo6leRY.txt
- Transcript chars: 36559
- Keywords: clusters, multicluster, traffic, cluster, running, having, started, working, production, gateway, mesh, actually, envoy, network, policies, course, ambient, product

### Resumo baseado na transcript

Um, so welcome to our lovely panel, the tales from the mesh, horrors and successes from running ISTO in production. I work at Solo and have done a lot of work integrating K gateway and agent gateway with ISTTO. Uh we've been using STO in production since 2019 when we did a massive overhaul of our Kubernetes estate, moving from one or two clusters, which were PETs into um a salesbased architecture of 24 production clusters and many other around the periphery and yeah, I'm working in TomTom as a software engineer basically dealing with Kubernetes. So we have a big challenge with uh few hundreds of Kubernetes clusters that has to be consolidated because you know 100 teams having and running their own clusters inevitably end up in uh quite a mess. So um we started consolidating these things and now kind of comes to be one of the main components that we're looking to solve problems like multicluster service mesh multi-reional support.

### Excerpt da transcript

Okay, cool. Everyone can hear me. Um, so welcome to our lovely panel, the tales from the mesh, horrors and successes from running ISTO in production. Um, I'm going to give a quick intro then introduce the panelists. Um, I'm Yophikova. I was the Kubernetes 133 release lead. I work at Solo and have done a lot of work integrating K gateway and agent gateway with ISTTO. Um, I also last KubeCon Amsterdam I gave I was the moderator for a panel of a lot of ISTO developers. So I'm really excited to be back to moderate this panel that's filled with ISTTO end users. So with that I'd like all of our panelists to introduce say your name, where you work and the year you started using ISTO. So uh let's start with Augustine here. >> Okay. Hi, I'm Augustine. I belong to Kaisante. Kaisaban Techch is a company inside the Kaisaban group and Kaisaban Group is a group of companies which belongs which has the biggest banking in Spain called Kaisa the biggest insurance companies also in Spain and one of the major banks also in Portugal called BPI.

So I'm the communities lead architect for Kaiser Bank. I'm managing from the infrastructure to all the marvelous DN CMCF products running on top of Kubernetes and well we've been working with histo22 main at the beginning as an English controller but also starting in 2022 like for a zero trust as a zero trust product I mean nobody can go out outside of his name space without a uh without submitting ordering I a rule for getting out of the nice space there's we have a self-service portal where you ask where you want to go and in what in in case of what you're ordering some rules are approved automatically other rules are are not and then we have some magic we have charts argo CD and all stuff and that get automatically applied in the class >> awesome thanks um maybe Alex you want to go next >> yeah hi everyone my name is Alex Williams I'm a principal software engineer at Skyscanner, which is a travel meta uh website. Hopefully, you've heard of it before. Uh we've been using STO in production since 2019 when we did a massive overhaul of our Kubernetes estate, moving from one or two clusters, which were PETs into um a salesbased architecture of 24 production clusters and many other around the periphery and yeah, using it mainly for our um ingress gateways, our east west gateways, and of course, service to service communication.

Um, so yeah, hopefully share some some stories from the good and bad days of uh of ISTTO throughout the last s
