---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Yuchen Zhou", "Google", "Uttam Kumar", "Salesforce"]
sched_url: https://kccncna2025.sched.com/event/27FXC/upgrade-nightmare-to-uptime-dream-the-cloud-providers-playbook-for-critical-kubernetes-work-yuchen-zhou-google-uttam-kumar-salesforce
youtube_search_url: https://www.youtube.com/results?search_query=Upgrade+Nightmare+To+Uptime+Dream%3A+The+Cloud+Provider%27s+Playbook+for+Critical+Kubernetes+Work+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Upgrade Nightmare To Uptime Dream: The Cloud Provider's Playbook for Critical Kubernetes Work - Yuchen Zhou, Google & Uttam Kumar, Salesforce

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Yuchen Zhou, Google, Uttam Kumar, Salesforce
- Schedule: https://kccncna2025.sched.com/event/27FXC/upgrade-nightmare-to-uptime-dream-the-cloud-providers-playbook-for-critical-kubernetes-work-yuchen-zhou-google-uttam-kumar-salesforce
- Busca YouTube: https://www.youtube.com/results?search_query=Upgrade+Nightmare+To+Uptime+Dream%3A+The+Cloud+Provider%27s+Playbook+for+Critical+Kubernetes+Work+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Upgrade Nightmare To Uptime Dream: The Cloud Provider's Playbook for Critical Kubernetes Work.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXC/upgrade-nightmare-to-uptime-dream-the-cloud-providers-playbook-for-critical-kubernetes-work-yuchen-zhou-google-uttam-kumar-salesforce
- YouTube search: https://www.youtube.com/results?search_query=Upgrade+Nightmare+To+Uptime+Dream%3A+The+Cloud+Provider%27s+Playbook+for+Critical+Kubernetes+Work+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xc4MU3HiHnY
- YouTube title: Upgrade Nightmare To Uptime Dream: The Cloud Provider's Playbook for... Yuchen Zhou & Uttam Kumar
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/upgrade-nightmare-to-uptime-dream-the-cloud-providers-playbook-for-cri/xc4MU3HiHnY.txt
- Transcript chars: 34481
- Keywords: version, upgrade, cluster, basically, platform, control, support, testing, add-ons, emulator, question, component, change, performance, environment, customers, clusters, functionality

### Resumo baseado na transcript

Uh my name is Utam Kumar and I am a director of infrastructure engineering at Salesforce. uh over the more than a decade I've been doing uh uh system engineering, DevOps uh s sur platform engineering and for the past 5 years I've been managing uh platform engineering teams uh on Kubernetes and today maybe I'll >> yeah hi everyone I'm Since we are leveraging Kubernetes, we use multicloud uh uh Kubernetes offering from Google cloud and other public cloud vendors. Uh we also provide a bunch of Kubernetes add-on functionality on our compute platform which includes uh like networking and storage CSI add-ons uh on our compute platform and we also provide uh a a bunch of controllers and component that provide autoscaling features on our cluster that for example cluster autoscaler carpenter uh horizontal pod autoscaler vertical pod autoscaler right and an ingress layer that manages the traffic internally and externally uh for our Kubernetes cluster. Our middle layer is our custom Salesforce integration services that provides functionality like certificate management, secret management, workload identity, monitoring, security services that are leveraged by the the services that runs on our compute platform and the top two layer fleet management and APIs are

### Excerpt da transcript

Good afternoon everyone. Uh my name is Utam Kumar and I am a director of infrastructure engineering at Salesforce. Uh just a quick introduction about myself. uh over the more than a decade I've been doing uh uh system engineering, DevOps uh s sur platform engineering and for the past 5 years I've been managing uh platform engineering teams uh on Kubernetes and today maybe I'll >> yeah hi everyone I'm from Google so I've been working on Kubernetes around like six year so recently I started focusing on reliable uh Kubernetes cluster upgrade Today we are here to talk about Kubernetes upgrade. Uh it's a very relatable topic since you are here at CubeCon and how Salesforce and Google have basically turned Kubernetes minor version upgrade from a nightmare to an uptime dream. So we'll talk about the Salesforce Hyperforce platform. Uh so Hyperforce uh is basically a next generation Salesforce infrastructure architecture that basically allows us uh to ship uh CRM critical CRM services for Salesforce customers more rapidly and reliably and at the same time it gives our customers more choices over data residency right it's a foundation for all Salesforce a cloud across marketing industry sales etc and if you look at the scale scale of our hyperforce compute platform.

It's not just big, it's massive. Like we have thousand plus Kubernetes clusters and on on this platform we have millions of Kubernetes pod that are the smallest deployable unit that runs the CRM workload and which runs on this platform which is like highly scalable, available, fall tolerant and secured. We'll just quickly deep dive into our tech stack for our compute layer. Since we are leveraging Kubernetes, we use multicloud uh uh Kubernetes offering from Google cloud and other public cloud vendors. On the top of it, we provide ST standard capabilities that include STTO which is a unified and cloud agnostic service mesh layer. Uh we also provide a bunch of Kubernetes add-on functionality on our compute platform which includes uh like networking and storage CSI add-ons uh on our compute platform and we also provide uh a a bunch of controllers and component that provide autoscaling features on our cluster that for example cluster autoscaler carpenter uh horizontal pod autoscaler vertical pod autoscaler right and an ingress layer that manages the traffic internally and externally uh for our Kubernetes cluster.

Our middle layer is our custom Salesforce integration services that provides functionality lik
