---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Kubernetes Core"]
speakers: ["Kubernetes Ecosystem in Azure"]
sched_url: https://kccnceu2021.sched.com/event/inNc/sponsored-session-microsoft-azure-kubernetes-ecosystem-in-azure
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Microsoft+Azure+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Session: Microsoft Azure - Kubernetes Ecosystem in Azure

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Kubernetes Ecosystem in Azure
- Schedule: https://kccnceu2021.sched.com/event/inNc/sponsored-session-microsoft-azure-kubernetes-ecosystem-in-azure
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Microsoft+Azure+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Session: Microsoft Azure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/inNc/sponsored-session-microsoft-azure-kubernetes-ecosystem-in-azure
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Microsoft+Azure+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-GAPujuS-h0
- YouTube title: Sponsored Session: Microsoft Azure - Kubernetes on Azure
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-session-microsoft-azure/-GAPujuS-h0.txt
- Transcript chars: 11481
- Keywords: policy, cluster, within, security, secret, created, create, resources, policies, volume, running, compliance, minutes, clusters, choose, external, secrets, manage

### Resumo baseado na transcript

hello and welcome to this kubernetes on azure overview in azure our goal is to make kubernetes an enterprise grade platform by design while building on an open source foundation that gives customers the maximum degree of flexibility we also look to take those innovations and enable them across both cloud and edge with azure arc in this session we'll be doing a number of demos looking at security best practices and threat detection and azure security center how you can do secrets management with the csi secret store driver

### Excerpt da transcript

hello and welcome to this kubernetes on azure overview in azure our goal is to make kubernetes an enterprise grade platform by design while building on an open source foundation that gives customers the maximum degree of flexibility we also look to take those innovations and enable them across both cloud and edge with azure arc in this session we'll be doing a number of demos looking at security best practices and threat detection and azure security center how you can do secrets management with the csi secret store driver applied policy and governance with the open policy agent in azure policy how you can consume kubernetes best practices with azure advisor and troubleshoot with azure diagnostics and then how you can manage heterogeneous kubernetes environments with azure arc so let's dive in when it comes to security a good place to start is azure security center which provides deep integration with aks to begin you'll want to look at asc's assessment of your cluster's security posture checking for security best practices in this case asc has identified that we have not limited network access to the kubernetes api server creating a broad attack vector in each case asc provides helpful pointers to documentation which help you take action on the recommendation in this case by providing a set of trusted sider ranges to access the api server once your environment is in production you'll want to be alerted about potential threats azure security center is continually monitoring the kubernetes audit log looking for suspicious activity that may suggest an attack in this case azure security center has identified that a pod is accessing a sensitive host volume it provides an assessment of the risk and suggested remediation steps again pointing out to the azure documentation to provide suggestions for next actions a critical part of securing any environment is proper management of secrets in partnership with hashicorp azure has built the csi secret store driver which enables mounting compatible key management stores into a kubernetes pod as a volume let's take a look at how that works here i have an azure key vault store that includes several secrets i'd like to use within my applications running in aks the secret store project is deployed as a daemon set and includes two components the secret store driver itself along with a compatible key store in this case azure key vault to mount a key vault into my application i'm going to create a secret provider class one of
