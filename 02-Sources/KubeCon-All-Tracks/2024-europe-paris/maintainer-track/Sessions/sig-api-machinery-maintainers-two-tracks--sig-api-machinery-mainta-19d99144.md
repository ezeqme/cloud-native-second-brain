---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Abu Kashem", "Red Hat", "Mike Spreitzer", "IBM"]
sched_url: https://kccnceu2024.sched.com/event/1YhjC/sig-api-machinery-maintainers-two-tracks-abu-kashem-red-hat-mike-spreitzer-ibm
youtube_search_url: https://www.youtube.com/results?search_query=SIG+API+Machinery+Maintainers+%28Two+Tracks%29+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG API Machinery Maintainers (Two Tracks) - Abu Kashem, Red Hat & Mike Spreitzer, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Abu Kashem, Red Hat, Mike Spreitzer, IBM
- Schedule: https://kccnceu2024.sched.com/event/1YhjC/sig-api-machinery-maintainers-two-tracks-abu-kashem-red-hat-mike-spreitzer-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+API+Machinery+Maintainers+%28Two+Tracks%29+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG API Machinery Maintainers (Two Tracks).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhjC/sig-api-machinery-maintainers-two-tracks-abu-kashem-red-hat-mike-spreitzer-ibm
- YouTube search: https://www.youtube.com/results?search_query=SIG+API+Machinery+Maintainers+%28Two+Tracks%29+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YpQxxZ1Izek
- YouTube title: SIG API Machinery Maintainers (Two Tracks) - Abu Kashem, Red Hat & Mike Spreitzer, IBM
- Match score: 0.758
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-api-machinery-maintainers-two-tracks/YpQxxZ1Izek.txt
- Transcript chars: 28934
- Keywords: request, server, priority, requests, concurrency, number, basically, schema, client, cluster, objects, second, nominal, levels, controller, configured, matches, configuration

### Resumo baseado na transcript

all right so let's start so we are in the sick API Machinery talk today and um we have two speakers it's Abu who's here and um Mike spryer who prepared a video which Abu will play and it's about priority and fairness and for those of you who have no idea what this means a few years ago when we didn't have that one controller could basically kill the API server by sending two any requests and basically we depended on client side throttling to be configured correctly and

### Excerpt da transcript

all right so let's start so we are in the sick API Machinery talk today and um we have two speakers it's Abu who's here and um Mike spryer who prepared a video which Abu will play and it's about priority and fairness and for those of you who have no idea what this means a few years ago when we didn't have that one controller could basically kill the API server by sending two any requests and basically we depended on client side throttling to be configured correctly and we are in a different world today 2024 and the work for that is basically in PRI and fairness and this feature on the C server and Abu and Mike are the ones who have basically pushed that and imple implemented that so let's welcome Abu thank you Stefan um hello everyone welcome to the IPA machinary seek dip dive um so um my Curr beh in person um we have a pre-recorded video from him um so I'll start uh by playing his video hi I'm Mike spritzer here to give you a brief overview of the API priority and fairness feature in kubernetes this is a feature in the C API server and in the generic API server library that we use to build similar API servers this feature regulates the load of API server in terms of the number of requests that is actively serving at a given moment the purpose of this feature is to protect the API server from the clients and to protect the clients from each other this feature is based on the on attributes of a request that participate in authentication and access control so that it cannot be easily fooled this feature thus is taking into account both the request rate and the time it takes to serve each request because the product of these two is on average the number of concurrent requests this is one-dimensional regulation this is an approximate technique it's a good approximation and there are a few TW tweaks to make it better which you'll see later this feature replaces the Max and flight filter which is an earlier filter that is simpler it classifies each request into one of just two categories mutating or read only and treats all request of a given category of the same APF is more granular it's also configur and it introduces queuing and APF introduces some fairness between clients like the Max and flight filter APF uh rejects request using in the standard HTTP way which is the status code 429 let's look at where the APF feature fits into the API server Stephan shimansky gave a good talk a few years ago at cpcom about the overall structure of the coup API server here
