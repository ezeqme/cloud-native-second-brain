---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Andre Jay Marcelo-Tanner", "Ada Support"]
sched_url: https://kccnceu2023.sched.com/event/1Hye8/disaster-recovery-bringing-back-production-from-scratch-in-under-1-hour-using-kops-argocd-and-velero-andre-jay-marcelo-tanner-ada-support
youtube_search_url: https://www.youtube.com/results?search_query=Disaster+Recovery%3A+Bringing+Back+Production+from+Scratch+in+Under+1+Hour+Using+KOps%2C+ArgoCD+and+Velero+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Disaster Recovery: Bringing Back Production from Scratch in Under 1 Hour Using KOps, ArgoCD and Velero - Andre Jay Marcelo-Tanner, Ada Support

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Andre Jay Marcelo-Tanner, Ada Support
- Schedule: https://kccnceu2023.sched.com/event/1Hye8/disaster-recovery-bringing-back-production-from-scratch-in-under-1-hour-using-kops-argocd-and-velero-andre-jay-marcelo-tanner-ada-support
- Busca YouTube: https://www.youtube.com/results?search_query=Disaster+Recovery%3A+Bringing+Back+Production+from+Scratch+in+Under+1+Hour+Using+KOps%2C+ArgoCD+and+Velero+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Disaster Recovery: Bringing Back Production from Scratch in Under 1 Hour Using KOps, ArgoCD and Velero.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hye8/disaster-recovery-bringing-back-production-from-scratch-in-under-1-hour-using-kops-argocd-and-velero-andre-jay-marcelo-tanner-ada-support
- YouTube search: https://www.youtube.com/results?search_query=Disaster+Recovery%3A+Bringing+Back+Production+from+Scratch+in+Under+1+Hour+Using+KOps%2C+ArgoCD+and+Velero+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oPQW99NiV_0
- YouTube title: Disaster Recovery: Bringing Back Production from Scratch in Under 1 Hour Using... - Marcelo-Tanner
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/disaster-recovery-bringing-back-production-from-scratch-in-under-1-hou/oPQW99NiV_0.txt
- Transcript chars: 27950
- Keywords: cluster, argo, running, process, clusters, valero, disaster, deploy, applications, recovery, working, production, actually, stores, secrets, create, everything, restore

### Resumo baseado na transcript

how's everybody today this is the last Talk of the day thank you for coming this is bring back production from scratch in under one hour using cops Argo CD and Valero my name is Andre Marcelo Tanner a little bit about me I'm a Staff devops engineer which really means like distinguished yaml engineer you can find me on these slack groups um I have taken the cka and cks exam how many people here have taken these exams all right awesome for anybody who hasn't I'd really recommend

### Excerpt da transcript

how's everybody today this is the last Talk of the day thank you for coming this is bring back production from scratch in under one hour using cops Argo CD and Valero my name is Andre Marcelo Tanner a little bit about me I'm a Staff devops engineer which really means like distinguished yaml engineer you can find me on these slack groups um I have taken the cka and cks exam how many people here have taken these exams all right awesome for anybody who hasn't I'd really recommend these exams they're really practical examples that test you under pressure and how to repair kubernetes clusters and that'll become relevant in the coming slides also I'm originally from the Philippines so my boys and I now live and work in Canada eh I work for a company named Ada and we're AI powered customer service automation company we've been around since 2016. we help Enterprises resolve their customer service inquiries in any language or Channel you know uh WhatsApp Facebook text email browser Ada has automated more than 4 billion customer conversations for companies like meta Verizon AirAsia Yeti Square and we serve companies and their customers across 85 countries how is that relevant so we've been running kubernetes in production for almost like six years and I've been there just for like four so I've seen a lot and a lot has changed um and about a year ago we had an incident that gave birth to this talk so picture this it's the end of the day you're on call you're about to you know go home log off turn off your laptop and suddenly one of the teams contacts you but hey we've got a problem we're trying to deploy our service to this one production cluster it's not working so I give my typical reply have you tried running it again and they do that and they come back it's not working so then I say we'll have you open the ticket because we we don't do work with Algeria tickets right well no so I started investigating right I go on I go on the cluster I try to see what's going on and the pods they're not coming up they're pending it seems like it's been this way for a few days which is strange uh so the current deployment is rather old but it's still running right it's kubernetes it's highly available and I go and look into our Auto scaling infrastructure okay it's bringing up new nodes that's working and I go check those out in our Cloud infrastructure ah they come up and then they go away they're not connecting to the cluster that's strange why is it doing that not supposed to
