---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9E/kubeslice-migrate-kubernetes-services-with-confidence-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=KubeSlice%3A+Migrate+Kubernetes+Services+With+Confidence%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# KubeSlice: Migrate Kubernetes Services With Confidence! | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9E/kubeslice-migrate-kubernetes-services-with-confidence-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=KubeSlice%3A+Migrate+Kubernetes+Services+With+Confidence%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre KubeSlice: Migrate Kubernetes Services With Confidence! | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9E/kubeslice-migrate-kubernetes-services-with-confidence-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=KubeSlice%3A+Migrate+Kubernetes+Services+With+Confidence%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xkl7EnILe-o
- YouTube title: KubeSlice: Migrate Kubernetes Services With Confidence! | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubeslice-migrate-kubernetes-services-with-confidence-project-lightnin/Xkl7EnILe-o.txt
- Transcript chars: 4975
- Keywords: across, clusters, access, connectivity, gpu, private, export, whatever, deploy, allocation, migrate, manage, sandbox, network, import, create, specific, slides

### Resumo baseado na transcript

hi so my name is prali co-founder of aesa and maintainer of cube slice just get this right get rid of this all right so let's go here all right so in your Cloud Journey our kubernetes journey there comes a time when you will be asked to do one thing I want to move some of my services from one cloud from one cluster in the or one or more clusters in the cloud to another Cloud for whatever the reason could it be lower compute lower erress lower

### Excerpt da transcript

hi so my name is prali co-founder of aesa and maintainer of cube slice just get this right get rid of this all right so let's go here all right so in your Cloud Journey our kubernetes journey there comes a time when you will be asked to do one thing I want to move some of my services from one cloud from one cluster in the or one or more clusters in the cloud to another Cloud for whatever the reason could it be lower compute lower erress lower like ha Dr governance a number of reasons you will be asked to move the the services to another Cloud right so the tricky part is most clusters in one cloud will have some chaing to manage services in that cloud like could it be like in a database or cues um whatever like you know a lot of different Services now most of the time these services will be accessed with the private end points and you want to keep that aspect of it not exposing the private fqdn to anywhere else and then okay oh here we know we want to migrate but we are going to hit a roadblock no public access points allowed no changes to application and I want a secure access right so what do we do now right we hit a roadblock and here comes the solution so cncf sandbox project Cube slice solve this in in a very elegant way so what is Cube slice right so Cube slice is a multicloud multicluster multi- Chate secure seamless service connectivity solution so the connectivity service connectivity as at the communities service level not including any service mesh so it's a simplified east west across the cluster connectivity and slice acts as a a network um layer it's agnostic um warly Network connects across the Clusters you can do import export uh services for connectivity across the slid so how does it work right so in a a quick uh nutshell so we have a controller we have clusters like you know Cloud one cloud two or region one region two so you register clusters create a slice so it creates an a VPN Channel um f compliant especially if you're worried about the the compliance um create a slice add name spaces to the slice deploy Services then export once you want to export to the other side export the service import the service connect the services so this whole thing can be done without any service mesh complexity built into it and it's a a a specific isolation now you want more sizes you can create every specific slide so every slice has its own specific overlay Network so that they there's an isolation between that like you can do distributed um other one
