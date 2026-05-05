---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Animesh Singh", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV2s/serving-machine-learning-models-at-scale-using-kserve-animesh-singh-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Serving+Machine+Learning+Models+at+Scale+Using+KServe+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Serving Machine Learning Models at Scale Using KServe - Animesh Singh, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Animesh Singh, IBM
- Schedule: https://kccncna2021.sched.com/event/lV2s/serving-machine-learning-models-at-scale-using-kserve-animesh-singh-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Serving+Machine+Learning+Models+at+Scale+Using+KServe+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Serving Machine Learning Models at Scale Using KServe.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2s/serving-machine-learning-models-at-scale-using-kserve-animesh-singh-ibm
- YouTube search: https://www.youtube.com/results?search_query=Serving+Machine+Learning+Models+at+Scale+Using+KServe+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rmYXPlzU4H8
- YouTube title: Serving Machine Learning Models at Scale Using KServing - Animesh Singh, IBM
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/serving-machine-learning-models-at-scale-using-kserve/rmYXPlzU4H8.txt
- Transcript chars: 40489
- Keywords: models, essentially, actually, around, mesh, capabilities, running, single, requests, available, server, serving, started, deploy, cluster, production, number, inference

### Resumo baseado na transcript

hey thanks and thanks for being here uh in person uh seeing a lot of you uh after a long while very very excited face you know life is back to normal i've been too many coupons in the past so i think you know after almost a two year gap right this is this is uh starting field things are coming back to normal right uh a bit about myself my name is anime shing i'm the cto for watson ai and machine learning open technology and you know

### Excerpt da transcript

hey thanks and thanks for being here uh in person uh seeing a lot of you uh after a long while very very excited face you know life is back to normal i've been too many coupons in the past so i think you know after almost a two year gap right this is this is uh starting field things are coming back to normal right uh a bit about myself my name is anime shing i'm the cto for watson ai and machine learning open technology and you know today's session we are going to talk about you know how to serve machine learning models at scale using k-serve and for those of you who haven't heard of k-serve um you know i'll go into it a bit as we proceed through the talk right so to begin with one of the things which we are seeing that you know around 90 of the corporate ai initiatives are still struggling to move uh to production right and and not only move to production even if you know uh they are moving in production there is a lot of skepticism around you know are these models giving predictions which can be trusted how do we measure business kpis but large part of the leg up is essentially you know in terms of taking these experiments which are happening uh within you know large number of enterprises but then you know deploying them in production and i think as we can see right uh the proliferation of models is everywhere right more and more we are seeing them uh actually you know being used uh in for example when you are playing your next song on alexa right you are essentially you know behind the scenes there is there is a model which is determining okay what is the next song you will like right and then in some cases right even in uh very important situations like when example you're submitting your resume some companies have started employing right ai in terms of making sure that you know your resume is getting to the right person or not so these models are making you know and have started making and progressively will be making more and more life-changing decisions for us but you know how hard is actually to do production grade model inference right what are the things which are needed right one thing which you definitely need to consider at the very beginning is the cost right models run on expensive hardware gpus tpus and you want to make sure you know they're not over or under scale you want to be able to monitor their endpoints are they healthy right you want to be able to roll out new versions of the model because machine learning is very experimental and
