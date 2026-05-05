---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["John Belamaric", "Google", "Yong Tang", "Ivanti"]
sched_url: https://kccnceu2024.sched.com/event/1YeOU/stop-leaking-kubernetes-service-information-via-dns-john-belamaric-google-yong-tang-ivanti
youtube_search_url: https://www.youtube.com/results?search_query=Stop+Leaking+Kubernetes+Service+Information+via+DNS%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Stop Leaking Kubernetes Service Information via DNS! - John Belamaric, Google & Yong Tang, Ivanti

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: John Belamaric, Google, Yong Tang, Ivanti
- Schedule: https://kccnceu2024.sched.com/event/1YeOU/stop-leaking-kubernetes-service-information-via-dns-john-belamaric-google-yong-tang-ivanti
- Busca YouTube: https://www.youtube.com/results?search_query=Stop+Leaking+Kubernetes+Service+Information+via+DNS%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Stop Leaking Kubernetes Service Information via DNS!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOU/stop-leaking-kubernetes-service-information-via-dns-john-belamaric-google-yong-tang-ivanti
- YouTube search: https://www.youtube.com/results?search_query=Stop+Leaking+Kubernetes+Service+Information+via+DNS%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Nfc4CiLUxUU
- YouTube title: Stop Leaking Kubernetes Service Information via DNS! - John Belamaric, Google & Yong Tang, Ivanti
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/stop-leaking-kubernetes-service-information-via-dns/Nfc4CiLUxUU.txt
- Transcript chars: 23745
- Keywords: cluster, actually, information, little, plugin, metadata, company, access, shared, default, record, request, course, another, growth, change, running, firewall

### Resumo baseado na transcript

so I'm I'm John B from Google this is y Tang uh from Avanti and we'll talk to you a little bit about how uh you may or may not realize you're leaking some of your service information uh in your kubernetes clusters and and what you might be able to do about it so Yang will take over from here okay to to get started before we talk about uh Co service information and the DNS Let's uh just briefly reveal role based Access Control in kues so what looc zone so I own this query so I'm going to resolve it and it goes and it query it actually has a cache of the services it finds that in the the cache but it sees that the metadata plug-in is enabled and so an NX domain instead of sending uh the actual response so that is actually what we I'll show the configuration and I'll I'll show that demo uh in a moment or just now actually so let's take another look here um so I exited out the kubernetes API server works is right you have a way say CNS works with it and all other controllers is they create a persistent connection to the API server and they say I'm interested in this information send me any send me all that

### Excerpt da transcript

so I'm I'm John B from Google this is y Tang uh from Avanti and we'll talk to you a little bit about how uh you may or may not realize you're leaking some of your service information uh in your kubernetes clusters and and what you might be able to do about it so Yang will take over from here okay to to get started before we talk about uh Co service information and the DNS Let's uh just briefly reveal role based Access Control in kues so what is robas Access Control robas access control is to Define uh which user can do what in a kuet cluster uh the principles of arack is to have list privilege that means you only want to expose information to users that absolutely need to know uh the good thing about roadbed access controling kubernetes is that it a wide interference in a shared environment let's assume you have a shared cluster with teams each team has their own agenda has their own like features has their own service me and uh uh let's say someday some one team decided to make some deployment and they break up certain things and of course in whole clust you uh in a nonworking State then everything will suffer right that's the so-called shared environment but in Ro SE control you actually want to have a separation so if one team messed up it will not uh of course a trouble to another team uh Ro based Access Control has been available in kubernetes since 1.8 so it has been adopted by uh by many companies uh across the board however uh in today's session I'm going to discuss a little bit about a special information that is DS related information uh the uniqueness about DS is that DS is actually uh outlier in commity environment so how is that so first of all DNS information in Comm is always going to be public that is DNS by itself serve as entry point for all the services because they serve the purpose of service Discovery the services in kumes uh will be exposed to our clients through DNS DNS uh have a DNS relies on UDP protocol which makes things even worse because with UDP you'll have no authentication or authorization uh this is in great conflict with the least privilege principle we discussed just a moment ago so you have to fix that uh so how do you fix that there are several ways to fix and depending on your scenario there may be some very easy way to fix let's just hypothetically say you work for small startup you have some great product you try to push and because it's a small startup the growth uh uh the growth of the company is very high let's s
