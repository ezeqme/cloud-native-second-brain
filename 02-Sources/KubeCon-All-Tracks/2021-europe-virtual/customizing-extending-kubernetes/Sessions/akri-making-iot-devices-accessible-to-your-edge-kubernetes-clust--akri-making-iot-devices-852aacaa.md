---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Kate Goldenring", "Microsoft", "Jiří Appl", "Microsoft"]
sched_url: https://kccnceu2021.sched.com/event/iE2E/akri-making-iot-devices-accessible-to-your-edge-kubernetes-clusters-kate-goldenring-microsoft-jiri-appl-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Akri%3A+Making+IoT+Devices+Accessible+to+Your+Edge+Kubernetes+Clusters+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Akri: Making IoT Devices Accessible to Your Edge Kubernetes Clusters - Kate Goldenring, Microsoft & Jiří Appl, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Kate Goldenring, Microsoft, Jiří Appl, Microsoft
- Schedule: https://kccnceu2021.sched.com/event/iE2E/akri-making-iot-devices-accessible-to-your-edge-kubernetes-clusters-kate-goldenring-microsoft-jiri-appl-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Akri%3A+Making+IoT+Devices+Accessible+to+Your+Edge+Kubernetes+Clusters+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Akri: Making IoT Devices Accessible to Your Edge Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2E/akri-making-iot-devices-accessible-to-your-edge-kubernetes-clusters-kate-goldenring-microsoft-jiri-appl-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Akri%3A+Making+IoT+Devices+Accessible+to+Your+Edge+Kubernetes+Clusters+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mcKNistZkrY
- YouTube title: Akri: Making IoT Devices Accessible to Your Edge Kubernetes Clusters - Kate Goldenring & Jiří Appl
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/akri-making-iot-devices-accessible-to-your-edge-kubernetes-clusters/mcKNistZkrY.txt
- Transcript chars: 21066
- Keywords: discovery, devices, handler, cluster, application, cameras, discover, deploy, configuration, camera, automatically, device, broker, frames, gpu, server, handlers, deployed

### Resumo baseado na transcript

hi everyone my name is kate goldenring my name is yugi apple and we're both software engineers at microsoft working on an open source project called ocry and today we're going to talk about how you can use ocari to make iot devices accessible to your edge kubernetes clusters so we'll first start off by talking about the motivation behind ocari and then we'll look at an iot edge scenario and how it can be simplified using ocry then we'll dive into awk's architecture and look at one of awk's

### Excerpt da transcript

hi everyone my name is kate goldenring my name is yugi apple and we're both software engineers at microsoft working on an open source project called ocry and today we're going to talk about how you can use ocari to make iot devices accessible to your edge kubernetes clusters so we'll first start off by talking about the motivation behind ocari and then we'll look at an iot edge scenario and how it can be simplified using ocry then we'll dive into awk's architecture and look at one of awk's latest enhancements that make it more easily extensible and finally we'll talk about how you can get involved okay so a bit of motivation a typical cloud kubernetes application has a fixed set of dependencies these are other cloud services that the application depends on for their functionality and these services are generally highly available on the other hand an edge application depends on variable number of data sources especially in each application that does any data processing now these data sources they might not be highly available because they might be represented by a simple devices such as ip cameras temperature sensors your edge application can also do control such as control of robotic arms and again these are not highly available sources so then the question is how can your application discover these uh then when there is a variable number of them we we cannot put these devices to be part of a kubernetes cluster because many times there are single purpose devices they have a small footprint or they have not been certified to run kubernetes and so how can your application take a dependency on them when we looked at this when we look at this we couldn't find a standardized way to achieve this and that's where we came up with agree akri exposes the individual iot devices into kubernetes clusters extended resources this then allows your application to take a dependency on them similarly like you would do on any gpu where you can ex where you can request uh access to the extended resource acry itself is the name is an acronym it stands for a kubernetes resource interface for the edge and it also stands for edge in greek now akri works in two phases first it discovers and advertises the iot devices to the cluster it then monitors the availability of those devices to make sure if a device disappears maybe it's disconnected or starts malfunctioning it stops advertising it to the cluster second this is an optional piece you can request accrete to schedule a workload
