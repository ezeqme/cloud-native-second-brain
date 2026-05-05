---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ankur Singh", "Red Hat", "Satyam Bhardwaj", "Mirantis"]
sched_url: https://kccnceu2026.sched.com/event/2CW20/fusing-finops-forecasting-and-kubernetes-at-scale-ankur-singh-red-hat-satyam-bhardwaj-mirantis
youtube_search_url: https://www.youtube.com/results?search_query=Fusing+FinOps%2C+Forecasting%2C+and+Kubernetes+at+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Fusing FinOps, Forecasting, and Kubernetes at Scale - Ankur Singh, Red Hat & Satyam Bhardwaj, Mirantis

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ankur Singh, Red Hat, Satyam Bhardwaj, Mirantis
- Schedule: https://kccnceu2026.sched.com/event/2CW20/fusing-finops-forecasting-and-kubernetes-at-scale-ankur-singh-red-hat-satyam-bhardwaj-mirantis
- Busca YouTube: https://www.youtube.com/results?search_query=Fusing+FinOps%2C+Forecasting%2C+and+Kubernetes+at+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Fusing FinOps, Forecasting, and Kubernetes at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW20/fusing-finops-forecasting-and-kubernetes-at-scale-ankur-singh-red-hat-satyam-bhardwaj-mirantis
- YouTube search: https://www.youtube.com/results?search_query=Fusing+FinOps%2C+Forecasting%2C+and+Kubernetes+at+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=65TRuI5hvn4
- YouTube title: Fusing FinOps, Forecasting, and Kubernetes at Scale - Ankur Singh & Satyam Bhardwaj
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/fusing-finops-forecasting-and-kubernetes-at-scale/65TRuI5hvn4.txt
- Transcript chars: 23179
- Keywords: forecast, cluster, models, source, particular, talking, cost, around, recommendations, actually, solution, software, matrix, custom, recommendation, format, forecasted, finally

### Resumo baseado na transcript

Uh today we're going to talk about a painoint that we have in the Kubernetes part which is PHOPS and we are going to present a solution onto PHOPS where all the things that we can do in a Kubernetes native way and keep it open source as well. So before we start with what we're going to present today, let me first introduce ourselves, first is me. So we're going to leverage so yeah we're going to build the system and we are going to first talk about what's wrong with the phops today and then there's an architecture there's a pattern that we saw in this in building this project and We'll also see how you can extend this model to build your custom logic for your business solutions and we're going to see how it scales al together and finally we have a demo around it. So uh talking about phops we we know that this has been one of the things that we always want to consider when it comes to the cost for any organization and it has been there since we had virtual machines. But right now with Kubernetes taking the pace we it is more important than ever that we look at how we can do it in a more Kubernetes native way rather than relying on uh vendor locked in uh products or solutions.

### Excerpt da transcript

I hope everybody is having a good day. Uh today we're going to talk about a painoint that we have in the Kubernetes part which is PHOPS and we are going to present a solution onto PHOPS where all the things that we can do in a Kubernetes native way and keep it open source as well. So before we start with what we're going to present today, let me first introduce ourselves, first is me. My name is Ankur Singh. I am a senior site reliability engineer at Red Hat and I work for managing and building solutions for one of the cloud managed uh Open Shift solution called Azure Red Hat Open Shift. My day-to-day things include building all the features around ARO, making sure that the observability is in place and also troubleshooting any customer incidents that come to us with respect to ARO as well. Hello everyone, good morning. It's a big crowd. Thanks for being here. I am Satyam. I'm a software engineer with the open source program office at Mirantis. We contribute to a lot of open source projects. I have been involved actively in building open-source multi cloud management systems.

So I have been contributing towards um there's a project called cluster API from the kubernetes eggs and I've also been contributing towards cod and kzeros. These are all multicluster management solutions and kz is like a kubernetes distribution. So today, yeah, today we're going to build a solution whereby we're going to utilize some a IML models to um you know really time series models to do forecasting for the observed data from your clusters. And here's the you know agenda for today. So we're going to leverage so yeah we're going to build the system and we are going to first talk about what's wrong with the phops today and then there's an architecture there's a pattern that we saw in this in building this project and we have built a project around it so really a p around it and we'll showcase the pattern that is observing the state of the cluster using those matrix to uh feed it to a model and use that forecasted data for recommendations to optimize your Kubernetes infrastructure. We'll also see how you can extend this model to build your custom logic for your business solutions and we're going to see how it scales al together and finally we have a demo around it.

So uh talking about phops we we know that this has been one of the things that we always want to consider when it comes to the cost for any organization and it has been there since we had virtual machines. But right no
