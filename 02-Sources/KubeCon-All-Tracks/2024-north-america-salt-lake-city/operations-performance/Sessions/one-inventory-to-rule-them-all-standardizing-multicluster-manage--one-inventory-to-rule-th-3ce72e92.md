---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Corentin Debains", "Google", "Ryan Zhang", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7o5/one-inventory-to-rule-them-all-standardizing-multicluster-management-corentin-debains-google-ryan-zhang-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=One+Inventory+to+Rule+Them+All%3A+Standardizing+Multicluster+Management+CNCF+KubeCon+2024
slides: []
status: parsed
---

# One Inventory to Rule Them All: Standardizing Multicluster Management - Corentin Debains, Google & Ryan Zhang, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Corentin Debains, Google, Ryan Zhang, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7o5/one-inventory-to-rule-them-all-standardizing-multicluster-management-corentin-debains-google-ryan-zhang-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=One+Inventory+to+Rule+Them+All%3A+Standardizing+Multicluster+Management+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre One Inventory to Rule Them All: Standardizing Multicluster Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7o5/one-inventory-to-rule-them-all-standardizing-multicluster-management-corentin-debains-google-ryan-zhang-microsoft
- YouTube search: https://www.youtube.com/results?search_query=One+Inventory+to+Rule+Them+All%3A+Standardizing+Multicluster+Management+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6c8Rh_vrIA4
- YouTube title: One Inventory to Rule Them All: Standardizing Multicluster Management - Corentin Debains, Ryan Zhang
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/one-inventory-to-rule-them-all-standardizing-multicluster-management/6c8Rh_vrIA4.txt
- Transcript chars: 26474
- Keywords: cluster, profile, clusters, actually, multicluster, application, argo, little, another, standard, support, manager, source, applications, basically, everybody, properties, secret

### Resumo baseado na transcript

thank you uh for coming to our talk uh one infantry to rule the mo um the standardizing multicluster management and uh good I'm cor theas I'm a software engineer at Google I work on GK Fleet oh sorry I did to go to that that page um and I'm ryen I'm working on uh Microsoft Azure Fleet so in this talk uh we're going to give you a quick brief overview of multicluster history and the current status and then we will spend some time uh describe our new

### Excerpt da transcript

thank you uh for coming to our talk uh one infantry to rule the mo um the standardizing multicluster management and uh good I'm cor theas I'm a software engineer at Google I work on GK Fleet oh sorry I did to go to that that page um and I'm ryen I'm working on uh Microsoft Azure Fleet so in this talk uh we're going to give you a quick brief overview of multicluster history and the current status and then we will spend some time uh describe our new and new shining new API called cluster infantry SL profile API and uh and and we also are going to give you uh some live demos uh hope the live guard is tremely good today and at the end uh we are going to uh ask for help from the community in those Future Works uh hopefully we can get more more help and uh uh we can hear more feedbacks from this group so without further Ado uh let's start so if you're here either um you have many clusters how many of you are actually running multiple clusters more than one cluster damn wow great now the here's the real question how many of you are actually running them together in a sense that you're not having a whole just the pets like your could be sit here into one into another into another and they are all like different uh types and shapes but you actually managing them together oh cool cool and how many of you are uh writing tools to run applications onto multi clusters so in a sense that you are not having uh this deployment to this cluster to that clust but you actually manage them kind of like together not bad great is there contributors maybe of like multiq or Argo that actually write applications for everyone OSS for this also man cluster managers like kamada cluster net ocm could be Stella could be something okay uh we'll see and if if you didn't raise your hand at all uh just uh come here for the lord of rings theme uh you wait till the end we have uh Easter egg for you okay it all started simple right with one one applications your deployment is running in uh your one sing single cluster that works well but then eventually you realize that you need that application to run onto multiple clusters and in that case uh like Argo multiq they all invented their own ways to have a list of clusters and and most likely currently they are using a list of uh Secrets or some sort of like that and that still works okayish not the best practice but it's okayish and then you have multiple applications multiple multicluster applications C there they they both needs to uh manage or
