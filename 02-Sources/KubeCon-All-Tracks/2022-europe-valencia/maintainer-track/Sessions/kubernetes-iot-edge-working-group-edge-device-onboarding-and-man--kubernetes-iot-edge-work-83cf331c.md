---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "VMware", "Kate Goldenring", "Microsoft", "Kilton Hopkins", "Edgeworx"]
sched_url: https://kccnceu2022.sched.com/event/ytoP/kubernetes-iot-edge-working-group-edge-device-onboarding-and-management-steven-wong-vmware-kate-goldenring-microsoft-kilton-hopkins-edgeworx
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+Working+Group%3A+Edge+Device+Onboarding+and+Management+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes IoT Edge Working Group: Edge Device Onboarding and Management - Steven Wong, VMware; Kate Goldenring, Microsoft; Kilton Hopkins, Edgeworx

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Steven Wong, VMware, Kate Goldenring, Microsoft, Kilton Hopkins, Edgeworx
- Schedule: https://kccnceu2022.sched.com/event/ytoP/kubernetes-iot-edge-working-group-edge-device-onboarding-and-management-steven-wong-vmware-kate-goldenring-microsoft-kilton-hopkins-edgeworx
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+Working+Group%3A+Edge+Device+Onboarding+and+Management+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes IoT Edge Working Group: Edge Device Onboarding and Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoP/kubernetes-iot-edge-working-group-edge-device-onboarding-and-management-steven-wong-vmware-kate-goldenring-microsoft-kilton-hopkins-edgeworx
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+IoT+Edge+Working+Group%3A+Edge+Device+Onboarding+and+Management+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CMthyqMhuq4
- YouTube title: Kubernetes IoT Edge Working Group: Edge Device Onboa... Steven Wong, Kate Goldenring, Kilton Hopkins
- Match score: 0.795
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-iot-edge-working-group-edge-device-onboarding-and-managemen/CMthyqMhuq4.txt
- Transcript chars: 34673
- Keywords: device, devices, server, firmware, working, manufacturer, upgrade, probably, cluster, onboard, secure, cameras, process, rendezvous, deploy, portainer, source, install

### Resumo baseado na transcript

hi welcome to cubecon 2022 in valencia this session is about supporting edge devices using kubernetes along with other open source tools i'm steve wong of vmware representing the kubernetes iot edge working group and i'm joined by kate goldenring of microsoft unfortunately kilton hopkins of edgeworks was also going to join us but he can't due to a death in the family and our deepest sympathies go out to him i'm going to cover a process for onboarding a host device to run kubernetes then kate will address onboarding

### Excerpt da transcript

hi welcome to cubecon 2022 in valencia this session is about supporting edge devices using kubernetes along with other open source tools i'm steve wong of vmware representing the kubernetes iot edge working group and i'm joined by kate goldenring of microsoft unfortunately kilton hopkins of edgeworks was also going to join us but he can't due to a death in the family and our deepest sympathies go out to him i'm going to cover a process for onboarding a host device to run kubernetes then kate will address onboarding of connected devices finally we believe that recent technology is going to be disruptive in edge it's going to be big really big and you can be a part of a community that changes the world and at the end we're going to tell you how to get involved devices don't just have a purchase price there's an added operational aspect onboard is the process of taking a new device and initializing it to begin using it i'm going to talk about secure device onboard this open source tool is specifically for putting a device in service at a remote location physical access can be challenging staff at edge can be untrained and untrusted what you'd like is to use existing logistics to ship a newer replacement device and put these in service using a random person trusted only to plug in the power and network cards and turn it on no logon or credentials needed secure device onboard does this even with headless or keyboard-less devices i'm i want to make it clear what problem space this covers and whip what it doesn't cover this is intended to do a one-time initial update or install of software the scope is the software running after a boot so from the os level on up through a container runtime a kubernetes distribution and other things that run above the os i suppose that if you had an executable that updated firmware without triggering an immediate reboot a one-time firmware update might be possible too the open source reference implementation of this uh has support for linux devices and a couple of embed arm devices uh using the spec i believe you could write an implementation for other platforms but this diagram covers what is out there today on github these are the players in history of the project intel originated this work uh and contributed it to the elf edge foundation secure device onboard and fido device on board are two names related to the same thing the fido alliance is shepherding the spec the lfh lf edge org is publishing reference open source implemen
