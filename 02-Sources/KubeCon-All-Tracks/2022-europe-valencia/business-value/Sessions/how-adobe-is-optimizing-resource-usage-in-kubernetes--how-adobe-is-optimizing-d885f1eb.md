---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Business Value"
themes: ["Kubernetes Core"]
speakers: ["Carlos Sanchez", "Adobe"]
sched_url: https://kccnceu2022.sched.com/event/yts2/how-adobe-is-optimizing-resource-usage-in-kubernetes-carlos-sanchez-adobe
youtube_search_url: https://www.youtube.com/results?search_query=How+Adobe+is+Optimizing+Resource+Usage+in+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Adobe is Optimizing Resource Usage in Kubernetes - Carlos Sanchez, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Business Value]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Carlos Sanchez, Adobe
- Schedule: https://kccnceu2022.sched.com/event/yts2/how-adobe-is-optimizing-resource-usage-in-kubernetes-carlos-sanchez-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=How+Adobe+is+Optimizing+Resource+Usage+in+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Adobe is Optimizing Resource Usage in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yts2/how-adobe-is-optimizing-resource-usage-in-kubernetes-carlos-sanchez-adobe
- YouTube search: https://www.youtube.com/results?search_query=How+Adobe+is+Optimizing+Resource+Usage+in+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iVD5YI1-U_M
- YouTube title: How Adobe is Optimizing Resource Usage in Kubernetes - Carlos Sanchez, Adobe
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-adobe-is-optimizing-resource-usage-in-kubernetes/iVD5YI1-U_M.txt
- Transcript chars: 26770
- Keywords: cluster, memory, requests, resources, request, number, limits, running, deployment, workloads, resource, whatever, environments, clusters, business, customer, customers, always

### Resumo baseado na transcript

thank you so i'm here to talk to you about how we are optimizing resources in kubernetes uh how can you reduce costs how can you improve utilization on your kubernetes clusters and i'll show you what you can do with open source kubernetes i'll show you what we have built on top further business use cases and hopefully you'll get some ideas that you can go back and use i used yourself so that's what uh you already said i one thing that people know me for for good cluster size and this was because of a bug that triggered out the scalar to to scale up so you see how at some point the two scalar went crazy and uh because we have the limit set up uh this didn't keep going but you see once we figure out what was happening the the number of machines just started stabilizing and going down the other typical option you're going to have is the horizontal polarity scale who's using our horizontal button scaler a lot of people using so

### Excerpt da transcript

thank you so i'm here to talk to you about how we are optimizing resources in kubernetes uh how can you reduce costs how can you improve utilization on your kubernetes clusters and i'll show you what you can do with open source kubernetes i'll show you what we have built on top further business use cases and hopefully you'll get some ideas that you can go back and use i used yourself so that's what uh you already said i one thing that people know me for for good or bad things is i restarted the junkies kubernetes plugin and but i'm happy that you all made it here right after lunch instead of going and take a siesta which would be the proper thing i hope you got coffee because we're going to be here for the next two hours just kidding um so i work at one team at adobe we use kubernetes at adobe a lot of people ask me oh i didn't know adobe use is kubernetes yes we do use a lot of kubernetes stuff and we're hiring by the way and i work at the experience manager product uh is a bit of an introduction so you understand what type of application we run it's an existing java osdi application with all the things that happen with java and the jvm it was already distributed before running on kubernetes it uses a lot of open source components from the apache software foundation we use a lot of open source and we contribute back it has a huge marker for extensions developers that write their own extensions plugin well components that run on adobe experience manager and they write modules that uh that run in process on am so this is an interesting use case because we run customer code in our multi-tenant clusters so on kubernetes on the cloud service am cloud service specifically there's also on-prem and managed services but on on on the cloud service we have more than 25 clusters and we keep growing every month because this is a content management system people want to run this in multiple regions so they want to run close to their customers so we're we have u.s europe australia japan and we keep adding new regions as needed and because customers can run their own code we also have limited permissions for security reasons we use namespace to provide the scope so different customers cannot see each other's data networking and all that so network isolation we use make use of quotas and permissions to to isolate tenants i like to refer it as a micro monolith because it's not our use case is not the the typical use case i have one deployment and i scale up to 200 pods or
