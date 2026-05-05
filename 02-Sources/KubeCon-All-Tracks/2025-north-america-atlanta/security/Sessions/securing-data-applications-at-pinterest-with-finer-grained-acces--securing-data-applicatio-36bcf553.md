---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security", "Storage Data", "Kubernetes Core"]
speakers: ["Soam Acharya", "William Tom", "Pinterest"]
sched_url: https://kccncna2025.sched.com/event/27Fdv/securing-data-applications-at-pinterest-with-finer-grained-access-control-on-kubernetes-soam-acharya-william-tom-pinterest
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Data+Applications+at+Pinterest+With+Finer+Grained+Access+Control+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Securing Data Applications at Pinterest With Finer Grained Access Control on Kubernetes - Soam Acharya & William Tom, Pinterest

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Soam Acharya, William Tom, Pinterest
- Schedule: https://kccncna2025.sched.com/event/27Fdv/securing-data-applications-at-pinterest-with-finer-grained-access-control-on-kubernetes-soam-acharya-william-tom-pinterest
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Data+Applications+at+Pinterest+With+Finer+Grained+Access+Control+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Securing Data Applications at Pinterest With Finer Grained Access Control on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fdv/securing-data-applications-at-pinterest-with-finer-grained-access-control-on-kubernetes-soam-acharya-william-tom-pinterest
- YouTube search: https://www.youtube.com/results?search_query=Securing+Data+Applications+at+Pinterest+With+Finer+Grained+Access+Control+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jPS6P3mTbqo
- YouTube title: Securing Data Applications at Pinterest With Finer Grained Access Cont... Soam Acharya & William Tom
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/securing-data-applications-at-pinterest-with-finer-grained-access-cont/jPS6P3mTbqo.txt
- Transcript chars: 22952
- Keywords: access, control, credentials, pinterest, request, policies, running, within, identity, security, wanted, actually, metadata, volance, platform, credential, policy, standard

### Resumo baseado na transcript

So today we're going to talk about securing data applications at Pinterest with finer grain access control on Kubernetes. We're both at Pinterest data engineering and we've worked on I guess the intersection of big data um data privacy and ML for quite a while. There's also third party data like say merchant catalogs stuff like that. know we'll kind of interchange Kubernetes and EKS we use AWS services within that a fair amount and that'll feature more as we kind of go forward. So here uh what you'll see is users will um compose jobs say using airflow or they'll submit interactive jobs via Jupiter or querybook and then um underneath the covers we'll decide whether to send it to Hadoop or to Mocha. um we were consolidating compute frameworks um cost efficiency was a factor.

### Excerpt da transcript

wanted to thank you for joining the uh next to last talk at CubeCon. So today we're going to talk about securing data applications at Pinterest with finer grain access control on Kubernetes. Um I'm S and I'm joined by my partner in crime will. We're both at Pinterest data engineering and we've worked on I guess the intersection of big data um data privacy and ML for quite a while. And so uh um we're just going to talk about um how we built this very large scale nextG uh big data platform and how we resolve some of these security data access issues. Okay. So our talk is divided into four parts. The first part we're going to give you a little bit of the landscape of data at Pinterest. So talk a little bit about uh the data platform, talk about Mocha which is our Spark on EKS. um based batch processing system and then shift on to some of the finer grain access control uh concepts and then I'll hand it over to Will to talk about more about the implementation of finer grain access control or FGAC that we call for short and then we'll have some conclusions and next steps.

So Pinterest um if you think about it, one way of thinking of Pinterest is it's a very large um ML-based recommendation engine. Users deal with pins and boards and uh Pinterest will make recommendations based on their activities. So what you're seeing here is a very datacentric view of how you know Pinterest collects data and processes and makes it available. Right? So you have apps, browsers kind of starting at the top. You have user activities and then there's a API service running at the back end, right? Very large scale collecting user activity information. There's also third party data like say merchant catalogs stuff like that. And then it further flows downstream. it's picked up by say either uh uh our change capture system CDC or Apache Kafka from which it can either go directly into S3 or it'll go into our big data platform. So there are two parts there is the streaming part and then there is the batch processing part. Uh we'll focus more on the batch processing this time around but a lot of the conclusions and the techniques we use will apply to streaming as well.

And then the output of all of this would be recommendations um building cleansing data for data warehouse um models and signals. So zooming in even further. So this is Mocha our batch processing platform to uh at at at Pinterest. So we're in the middle of a or almost maybe towards the end of a transition from our previous
