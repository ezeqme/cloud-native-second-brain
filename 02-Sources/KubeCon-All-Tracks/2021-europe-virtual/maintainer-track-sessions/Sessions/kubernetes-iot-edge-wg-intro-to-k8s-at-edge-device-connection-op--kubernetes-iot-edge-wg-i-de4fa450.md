---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "VMware", "Dejan Bosanac", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE7A/kubernetes-iot-edge-wg-intro-to-k8s-at-edge-+-device-connection-options-steven-wong-vmware-dejan-bosanac-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+WG%3A+Intro+to+K8s+at+Edge+%2B+Device+Connection+Options+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes IoT Edge WG: Intro to K8s at Edge + Device Connection Options - Steven Wong, VMware & Dejan Bosanac, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Steven Wong, VMware, Dejan Bosanac, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE7A/kubernetes-iot-edge-wg-intro-to-k8s-at-edge-+-device-connection-options-steven-wong-vmware-dejan-bosanac-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+WG%3A+Intro+to+K8s+at+Edge+%2B+Device+Connection+Options+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes IoT Edge WG: Intro to K8s at Edge + Device Connection Options.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7A/kubernetes-iot-edge-wg-intro-to-k8s-at-edge-+-device-connection-options-steven-wong-vmware-dejan-bosanac-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+WG%3A+Intro+to+K8s+at+Edge+%2B+Device+Connection+Options+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_NkuspFW9IQ
- YouTube title: Kubernetes IoT Edge WG: Intro to K8s at Edge + Device Connection Option- Steven Wong & Dejan Bosanac
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-iot-edge-wg-intro-to-k8s-at-edge-device-connection-options/_NkuspFW9IQ.txt
- Transcript chars: 22768
- Keywords: device, network, devices, lorawan, applications, gateway, called, technology, single, events, server, multiple, native, provide, appropriate, coming, gateways, messages

### Resumo baseado na transcript

hi welcome to the kubecon europe session from the kubernetes iot edge working group i'm steve wong i'm a co-chair of the iot edge working group i'm employed as a software engineer working on kubernetes by vmware and i'm coming to you in this recording from los angeles california hello my name is dan i'm a software engineer with earthquake i'm also a colleague of humanity society edge working group and coming from belgrade serbia so here's today's agenda we're going to give contact information and a link to the

### Excerpt da transcript

hi welcome to the kubecon europe session from the kubernetes iot edge working group i'm steve wong i'm a co-chair of the iot edge working group i'm employed as a software engineer working on kubernetes by vmware and i'm coming to you in this recording from los angeles california hello my name is dan i'm a software engineer with earthquake i'm also a colleague of humanity society edge working group and coming from belgrade serbia so here's today's agenda we're going to give contact information and a link to the deck at the end uh i'm gonna start with a really quick overview of what's different about communications for edge applications and edge devices then we're gonna move on with an introduction to some technology called lora along with a network architecture based on it called lorawan about halfway through dion is going to take over with a talk on the drug cloud project followed by a demo hopefully you'll like the talk and if you do we're going to wrap up with details on how you can become a member of the kubernetes iot edge working group where we host ongoing discussions on subjects like what's in this talk edge applications are often isolated but they're generally going to be part of a bigger picture multi-tier architecture if kubernetes is involved you know if you're using stand-alone edge devices that don't talk to anything else you're unlikely to really have kubernetes involved but if you are connecting up ice edge devices to feed into applications and servers on a regional or global basis um that's going to be the scenario where it makes sense to utilize kubernetes and that's what we're going to be here to address today so if you try to do communications at edge the same way it's done in a large cloud data center be prepared for some challenges and even a few roadblocks particularly in mobile and in remote places that have wiring difficulties radio based communication is an alternative to hardwire and we're all familiar with the radio based options like wi-fi bluetooth and lte today we're going to talk about another wireless option lora lora by the way stands for long range of course this conference is also about kubernetes so we're also going to show how information or events can be collected from edge nodes to feed kubernetes hosted apps i'm going to start with a technical overview and then later dan will move on to cover the drogue project so we're all familiar with wi-fi which is an example of a local area network uh its reach is limited to per
