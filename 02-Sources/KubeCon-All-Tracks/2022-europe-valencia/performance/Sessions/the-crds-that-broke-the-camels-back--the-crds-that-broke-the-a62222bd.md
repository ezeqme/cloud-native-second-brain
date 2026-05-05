---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Alper Rifat Ulucinar", "Upbound"]
sched_url: https://kccnceu2022.sched.com/event/ytnR/the-crds-that-broke-the-camels-back-alper-rifat-ulucinar-upbound
youtube_search_url: https://www.youtube.com/results?search_query=The+CRDs+that+Broke+the+Camel%27s+Back+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The CRDs that Broke the Camel's Back - Alper Rifat Ulucinar, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Alper Rifat Ulucinar, Upbound
- Schedule: https://kccnceu2022.sched.com/event/ytnR/the-crds-that-broke-the-camels-back-alper-rifat-ulucinar-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=The+CRDs+that+Broke+the+Camel%27s+Back+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The CRDs that Broke the Camel's Back.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytnR/the-crds-that-broke-the-camels-back-alper-rifat-ulucinar-upbound
- YouTube search: https://www.youtube.com/results?search_query=The+CRDs+that+Broke+the+Camel%27s+Back+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jYiLN0vmncw
- YouTube title: The CRDs that Broke the Camel's Back - Alper Rifat Ulucinar, Upbound
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-crds-that-broke-the-camels-back/jYiLN0vmncw.txt
- Transcript chars: 23271
- Keywords: server, client, resource, custom, discovery, available, issues, version, definitions, provider, profiling, parameter, providers, bucket, utilization, running, requests, aggregated

### Resumo baseado na transcript

thank you for coming to listen to my presentation so let's start so in this talk i'd like to you know give a brief introduction how we encounter these issues uh so upon is one of the main maintainers of the crossplane project and i will talk about a little bit about cross plane and you know uh how we hit these issues and then i'd like to briefly mention you know the client side see the scaling issues that we have hit and also i'd like to talk about

### Excerpt da transcript

thank you for coming to listen to my presentation so let's start so in this talk i'd like to you know give a brief introduction how we encounter these issues uh so upon is one of the main maintainers of the crossplane project and i will talk about a little bit about cross plane and you know uh how we hit these issues and then i'd like to briefly mention you know the client side see the scaling issues that we have hit and also i'd like to talk about the server side issues that we have identified and you know how we identified them specifically you know the high resource utilization we have observed with the api server and how we profile the api server what windings we have and also i'd like to briefly mention you know how you can profile the api server so it's really straightforward so i'd like to you know talk a little bit about it it's helped us a lot in this respect and also you know i'd like to talk about you know the kubernetes scalability dimensions and you know about crd scaling in that respect and you know this will conclude to talk so uh apan is one of the you know core maintainers of the cross plane project in the cross plane project we are working on you know generating sometimes you know custom resource definitions which correspond to actual cloud provider resources and as you would imagine why this custom resource says you know you can manage the infrastructure so and as you know there are you know hundreds of uh different resource types in its cloud provider and uh crossplane is a multi-vendor multi-platform project so that you know either your resources are in aws azure or gcp you can have a cross-plain provider and many stores providers this also you know means that in a single kubernetes cluster you may want to install multiple you know cross plane providers so recently we have introduced a terajet a cogeneration framework where you can generate you know crossplane providers on top of terraform providers this also means that in a single provider like we have generated provider jet aws jet ager and gcp pro we have these providers and uh on top of these you know you can have hundreds of custom resources and this is where we first observed our issues because you know in a single for example provider jet aws cross plane provider we have over 700 custom resource definitions and in the other azure and gcp providers we have again hundreds of custom resource definitions and if you would like to install one of them or you know multiple of them in a
