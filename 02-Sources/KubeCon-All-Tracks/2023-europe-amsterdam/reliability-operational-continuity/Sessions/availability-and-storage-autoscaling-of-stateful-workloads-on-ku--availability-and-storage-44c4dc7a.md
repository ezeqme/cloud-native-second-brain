---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Leila Vayghan", "Shopify"]
sched_url: https://kccnceu2023.sched.com/event/1HyXG/availability-and-storage-autoscaling-of-stateful-workloads-on-kubernetes-leila-vayghan-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Availability+and+Storage+Autoscaling+of+Stateful+Workloads+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Availability and Storage Autoscaling of Stateful Workloads on Kubernetes - Leila Vayghan, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Leila Vayghan, Shopify
- Schedule: https://kccnceu2023.sched.com/event/1HyXG/availability-and-storage-autoscaling-of-stateful-workloads-on-kubernetes-leila-vayghan-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Availability+and+Storage+Autoscaling+of+Stateful+Workloads+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Availability and Storage Autoscaling of Stateful Workloads on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXG/availability-and-storage-autoscaling-of-stateful-workloads-on-kubernetes-leila-vayghan-shopify
- YouTube search: https://www.youtube.com/results?search_query=Availability+and+Storage+Autoscaling+of+Stateful+Workloads+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=a0aNdOUDqhA
- YouTube title: Availability and Storage Autoscaling of Stateful Workloads on Kubernetes - Leila Vayghan
- Match score: 0.991
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/availability-and-storage-autoscaling-of-stateful-workloads-on-kubernet/a0aNdOUDqhA.txt
- Transcript chars: 23389
- Keywords: stateful, storage, controller, custom, elasticsearch, scaling, volume, availability, search, delete, shopify, replica, expanded, provide, update, object, number, called

### Resumo baseado na transcript

uh good afternoon thanks for coming this session is about availability and storage Auto scaling of stateful workloads running on kubernetes my name is Leila I work at Shopify as an infrastructure engineer I'm on a team of 10 Engineers called the search platform who develop and maintain the infrastructure that powers search at Shopify this is the agenda for this talk in the next 20 minutes or so we'll learn how the search infrastructure team at Shopify hosts a stateful workload which is searched on top of kubernetes we'll

### Excerpt da transcript

uh good afternoon thanks for coming this session is about availability and storage Auto scaling of stateful workloads running on kubernetes my name is Leila I work at Shopify as an infrastructure engineer I'm on a team of 10 Engineers called the search platform who develop and maintain the infrastructure that powers search at Shopify this is the agenda for this talk in the next 20 minutes or so we'll learn how the search infrastructure team at Shopify hosts a stateful workload which is searched on top of kubernetes we'll talk about the obstacles of providing High availability and storage Auto scaling and scaling in general for stateful workloads that run on kubernetes and how my team address those challenges and I also have a pre-recorded demo at the end and will conclude the presentation with a q a so a little bit about Shopify for those who don't know about us Shopify is a cloud-based Commerce platform that lets you start and manage a business by allowing you to create and customize an online store and manage inventory payments and Etc currently we have more than 3 million Merchants that sell a lot of products with us and they collectively have sold over 700 billion dollars in Gross merchandise volume so just to give a better sense of the scale only during the Black Friday Cyber Monday weekend of 2022 which is a high like which is a major high volume Commerce event that kicks off the uh holiday shopping season our Merchants sold over seven billion dollars in GMB search is a fundamental part of any Commerce platform that allows buyers to search and filter for the products that they're looking for it also allows Merchants to fulfill the orders that they have received when you go to any online Store and search for a certain product your request goes to a search engine that's backed by a secondary data store which is different from traditional databases uh we call this secondary data store the search infrastructure at Shopify we use elasticsearch to provide search and filtering services to Shopify core which Powers all of our Merchant shops as well as their storefronts as well as the development teams who need search services we run shopify's search on top of kubernetes on Google Cloud platform and deploy and maintain these elasticsearch instances by using a custom kubernetes controller that we have built so let's catch up on some definitions stateful Services unlike stateless ones rely on persistent data and respond to the same inputs in different ways depe
