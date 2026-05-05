---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Savin Goyal", "Outerbounds", "Saravanan Balasubramanian", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182Fh/human-friendly-production-ready-data-science-stack-with-metaflow-kubernetes-savin-goyal-outerbounds-saravanan-balasubramanian-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Human-Friendly%2C+Production-Ready+Data+Science+Stack+With+Metaflow+%26+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Human-Friendly, Production-Ready Data Science Stack With Metaflow & Kubernetes - Savin Goyal, Outerbounds & Saravanan Balasubramanian, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Savin Goyal, Outerbounds, Saravanan Balasubramanian, Intuit
- Schedule: https://kccncna2022.sched.com/event/182Fh/human-friendly-production-ready-data-science-stack-with-metaflow-kubernetes-savin-goyal-outerbounds-saravanan-balasubramanian-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Human-Friendly%2C+Production-Ready+Data+Science+Stack+With+Metaflow+%26+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Human-Friendly, Production-Ready Data Science Stack With Metaflow & Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fh/human-friendly-production-ready-data-science-stack-with-metaflow-kubernetes-savin-goyal-outerbounds-saravanan-balasubramanian-intuit
- YouTube search: https://www.youtube.com/results?search_query=Human-Friendly%2C+Production-Ready+Data+Science+Stack+With+Metaflow+%26+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bLg5oHIjOpI
- YouTube title: Human-Friendly, Production-Ready Data Science Stack With Metaflow &... - Savin Goyal & Saravanan
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/human-friendly-production-ready-data-science-stack-with-metaflow-kuber/bLg5oHIjOpI.txt
- Transcript chars: 29545
- Keywords: workflow, argo, metaflow, learning, machine, running, application, scientist, production, memory, cluster, workflows, around, basically, resume, laptop, compute, course

### Resumo baseado na transcript

hi uh my name is seven and it in today's talk I'm going to talk about my experience building data science infrastructure for well over a decade now and some of the work that we have done very recently within the kubernetes community as part of this talk we also have a quick demo that my collaborator Bala from Intuit will be handling if you guys are interested you can also follow along this demo within your own browser as well we'll be sharing a handy link to access the

### Excerpt da transcript

hi uh my name is seven and it in today's talk I'm going to talk about my experience building data science infrastructure for well over a decade now and some of the work that we have done very recently within the kubernetes community as part of this talk we also have a quick demo that my collaborator Bala from Intuit will be handling if you guys are interested you can also follow along this demo within your own browser as well we'll be sharing a handy link to access the demo too now for those of you in the room who are either practicing data scientists or have built data science infrastructure in the past or currently as well this might be a familiar narrative but just imagine you know like let's say your organization wants to build a recommendation system so you have a data scientist who is tasked with that job and the first thing that they would like to do is maybe perhaps you know spin up an ID instance on the cloud so maybe a Jupiter Notebook on AWS or maybe it's sort of like some IDE pycharm on their local workstation their laptop and the very first activity that they want to do right after this is get access to some data so that they can start making sense of that data uh maybe your data is stored in some snowflake data warehouse some data breaks data Lake maybe you have sort of like you know stitched together your own data platform on top of S3 but there's usually sort of like some mechanism that's needed for this data scientist to now sort of like understand what data is available what is the quality of that data how to access that data so that all the security and data governance concerns are addressed and how to quickly and efficiently access that data so you are not waiting for like minutes and hours to get access to that so that you can start playing with that data you can start sort of like you know building an intuition around it but then as soon as you're sort of like you know across this first hurdle uh you're presented with the next one you know it could very well be the case that the kind of data analysis that you want to do or the kind of models that you want to train that's not possible on your local workstation not possible maybe perhaps on the notebook instance that you have in the cloud maybe you're doing some feature engineering step that requires huge amount of memory that's just not available on your laptop maybe you are training a model that requires GPU maybe you decided that maybe you want to train a model for every single count
